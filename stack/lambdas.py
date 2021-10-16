from dataclasses import dataclass

import aws_cdk.aws_lambda as lambda_
import constructs


@dataclass
class LambdaFunctions:
    clean_text: lambda_.Function
    create_embedding: lambda_.Function
    predict_salary: lambda_.Function

    def items(self) -> list[lambda_.Function]:
        return list(self.__dict__.values())


def create_functions(scope: constructs.Construct) -> LambdaFunctions:
    return LambdaFunctions(
        clean_text=lambda_.Function(
            scope,
            id="CleanText",
            function_name="CleanText",
            handler="handlers.clean_text",
            runtime=lambda_.Runtime.PYTHON_3_9,
            code=lambda_.Code.from_asset("functions"),
        ),
        create_embedding=lambda_.Function(
            scope,
            id="CreateEmbedding",
            function_name="CreateEmbedding",
            handler="handlers.create_embedding",
            runtime=lambda_.Runtime.PYTHON_3_9,
            code=lambda_.Code.from_asset("functions"),
        ),
        predict_salary=lambda_.Function(
            scope,
            id="PredictSalary",
            function_name="PredictSalary",
            handler="handlers.predict_salary",
            runtime=lambda_.Runtime.PYTHON_3_9,
            code=lambda_.Code.from_asset("functions"),
        ),
    )
