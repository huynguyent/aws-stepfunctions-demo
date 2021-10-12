from aws_cdk import core as cdk

from stacks.step_functions.step_function_stack import StepFunctionsStack

app = cdk.App()

step_functions_stack = StepFunctionsStack(
    scope=app,
    construct_id="StepFunctionsDemo",
)


app.synth()
