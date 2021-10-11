from typing import Any

import aws_cdk.aws_logs as aws_logs
import aws_cdk.aws_stepfunctions as sfn
from aws_cdk import core as cdk

from .state_machine_definition import create_state_machine


class StepFunctionsStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)

        stepfunctions_log_group = aws_logs.LogGroup(
            scope=self,
            id="stepfunctions-log-group",
            log_group_name="/aws/stepfunctions/ExampleStepFunctions",
        )

        example_state_machine = sfn.StateMachine(
            scope=self,
            id="example-state-machine",
            state_machine_name="ExampleStateMachine",
            logs=sfn.LogOptions(
                destination=stepfunctions_log_group,
                level=sfn.LogLevel.ALL,
            ),
            definition=create_state_machine(self),
        )
