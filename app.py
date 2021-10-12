from aws_cdk import core as cdk

from stack.step_function_stack import StepFunctionsStack

app = cdk.App()

step_functions_stack = StepFunctionsStack(
    scope=app,
    construct_id="StepFunctionsDemo",
)


app.synth()
