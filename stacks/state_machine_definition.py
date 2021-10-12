import aws_cdk.aws_stepfunctions as sfn
import aws_cdk.aws_stepfunctions_tasks as tasks
import constructs

from stacks.lambdas import LambdaFunctions


def create_state_machine(
    scope: constructs.Construct, lambda_functions: LambdaFunctions
) -> sfn.IChainable:
    return tasks.LambdaInvoke(
        scope=scope, id="hello_world", lambda_function=lambda_functions.hello_world
    ).next(sfn.Pass(scope=scope, id="test_task"))
