from typing import Any

import aws_cdk.aws_dynamodb as dynamodb
import aws_cdk.aws_iam as iam
import aws_cdk.aws_logs as aws_logs
import aws_cdk.aws_stepfunctions as sfn
from aws_cdk import core as cdk

from . import lambdas, policies
from .state_machine_definition import create_state_machine


class StepFunctionsStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_functions = lambdas.create_functions(self)

        job_data_table = dynamodb.Table(
            scope=self,
            id="JobDataTable",
            partition_key=dynamodb.Attribute(
                name="job_id", type=dynamodb.AttributeType.STRING
            ),
        )

        stepfunctions_log_group = aws_logs.LogGroup(
            scope=self,
            id="stepfunctions-log-group",
            log_group_name="/aws/stepfunctions/ExampleStepFunctions",
        )

        state_machine_role = iam.Role(
            scope=self,
            id="ExampleStateMachineRole",
            role_name="ExampleStateMachineRole",
            assumed_by=iam.ServicePrincipal("states.amazonaws.com"),
            managed_policies=[
                policies.Lambda.invoke_functions(
                    scope=self,
                    function_arns=[
                        function.function_arn for function in lambda_functions.items()
                    ],
                ),
                policies.CwLog.write_logs(
                    scope=self, log_group_arns=[stepfunctions_log_group.log_group_arn]
                ),
                policies.DynamoDb.write_access(
                    scope=self, table_arn=job_data_table.table_arn
                ),
            ],
        )

        example_state_machine = sfn.StateMachine(
            scope=self,
            id="example-state-machine",
            state_machine_name="ExampleStateMachine",
            role=state_machine_role,
            logs=sfn.LogOptions(
                destination=stepfunctions_log_group,
                level=sfn.LogLevel.ALL,
            ),
            definition=create_state_machine(
                self, lambda_functions=lambda_functions, data_table=job_data_table
            ),
        )

        state_machine_role.node.add_dependency(
            *lambda_functions.items(), job_data_table, stepfunctions_log_group
        )
        example_state_machine.node.add_dependency(state_machine_role)
