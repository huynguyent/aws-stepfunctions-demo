from aws_cdk import core as cdk

from stacks.step_function_stack import StepFunctionsStack

app = cdk.App()
StepFunctionsStack(
    scope=app,
    construct_id="StepFunctionsDemo",
    env=cdk.Environment(region="ap-southeast-2"),
)

app.synth()
