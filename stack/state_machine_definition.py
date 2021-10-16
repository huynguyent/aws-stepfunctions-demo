import aws_cdk.aws_stepfunctions as sfn
import aws_cdk.aws_stepfunctions_tasks as tasks
import constructs

from .lambdas import LambdaFunctions


def create_state_machine(
    scope: constructs.Construct, lambda_functions: LambdaFunctions
) -> sfn.IChainable:
    return tasks.LambdaInvoke(
        scope=scope,
        id="CleanTextStep",
        lambda_function=lambda_functions.clean_text,
        payload=sfn.TaskInput.from_object({"html_text.$": "$.html_text"}),
        result_selector={
            "result.$": "$.Payload"
        },
        result_path="$.CleanText"
    )
