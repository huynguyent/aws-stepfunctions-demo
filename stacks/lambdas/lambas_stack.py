from typing import Any

import aws_cdk.aws_lambda as lambda_
from aws_cdk import core as cdk


class LambdasStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)

        base_lambda = lambda_.Function(
            self,
            id="ExampleLambda",
            function_name="ExampleLambda",
            handler="handlers.hello",
            runtime=lambda_.Runtime.PYTHON_3_7,
            code=lambda_.Code.from_asset("functions"),
        )
