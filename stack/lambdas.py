from dataclasses import dataclass

import aws_cdk.aws_lambda as lambda_
import constructs


@dataclass
class LambdaFunctions:
    hello_world: lambda_.Function

    def items(self) -> list[lambda_.Function]:
        return list(self.__dict__.values())


def create_functions(scope: constructs.Construct) -> LambdaFunctions:
    return LambdaFunctions(
        hello_world=lambda_.Function(
            scope,
            id="ExampleLambda",
            function_name="ExampleLambda",
            handler="handlers.hello",
            runtime=lambda_.Runtime.PYTHON_3_9,
            code=lambda_.Code.from_asset("functions"),
        )
    )
