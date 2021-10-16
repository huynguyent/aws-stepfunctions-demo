import aws_cdk.aws_stepfunctions as sfn
import aws_cdk.aws_stepfunctions_tasks as tasks
import constructs

from .lambdas import LambdaFunctions


def create_state_machine(
    scope: constructs.Construct, lambda_functions: LambdaFunctions
) -> sfn.IChainable:
    clean_text_step = tasks.LambdaInvoke(
        scope=scope,
        id="CleanTextStep",
        lambda_function=lambda_functions.clean_text,
        payload=sfn.TaskInput.from_object({"html_text.$": "$.html_text"}),
        result_selector={"result.$": "$.Payload"},
        result_path="$.CleanText",
    )

    create_embedding_step = tasks.LambdaInvoke(
        scope=scope,
        id="CreateEmbeddingStep",
        lambda_function=lambda_functions.create_embedding,
        payload=sfn.TaskInput.from_object({"cleaned_text.$": "$.CleanText.result"}),
        result_selector={"result.$": "$.Payload"},
        result_path="$.CreateEmbedding",
    )

    predict_salary_step = tasks.LambdaInvoke(
        scope=scope,
        id="PredictSalaryStep",
        lambda_function=lambda_functions.predict_salary,
        payload=sfn.TaskInput.from_object({"embedding.$": "$.CreateEmbedding.result"}),
        result_selector={"result.$": "$.Payload"},
        result_path="$.PredictSalary",
    )

    return clean_text_step.next(create_embedding_step).next(predict_salary_step)
