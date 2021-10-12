from aws_cdk import core as cdk

from stacks.lambdas.lambas_stack import LambdasStack
from stacks.step_functions.step_function_stack import StepFunctionsStack

app = cdk.App()
lambdas_stack = LambdasStack(
    scope=app,
    construct_id="ExampleLambdas",
)
step_functions_stack = StepFunctionsStack(
    scope=app,
    construct_id="StepFunctionsDemo",
)

step_functions_stack.add_dependency(lambdas_stack)

app.synth()
