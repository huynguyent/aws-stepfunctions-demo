import aws_cdk.aws_dynamodb as dynamodb
import aws_cdk.aws_stepfunctions as sfn
import aws_cdk.aws_stepfunctions_tasks as tasks
import constructs

from .lambdas import LambdaFunctions


def create_state_machine(
    scope: constructs.Construct,
    lambda_functions: LambdaFunctions,
    data_table: dynamodb.Table,
) -> sfn.IChainable:
    clean_text_step = tasks.LambdaInvoke(
        scope=scope,
        id="CleanTextStep",
        lambda_function=lambda_functions.clean_text,
        payload=sfn.TaskInput.from_object({"html_text.$": "$.html_text"}),
        result_selector={"result.$": "$.Payload"},
        result_path="$.cleaned_text",
    )

    create_embedding_step = tasks.LambdaInvoke(
        scope=scope,
        id="CreateEmbeddingStep",
        lambda_function=lambda_functions.create_embedding,
        payload=sfn.TaskInput.from_object({"cleaned_text.$": "$.cleaned_text.result"}),
        result_selector={"result.$": "$.Payload"},
        result_path="$.embedding",
    )

    predict_salary_step = tasks.LambdaInvoke(
        scope=scope,
        id="PredictSalaryStep",
        lambda_function=lambda_functions.predict_salary,
        payload=sfn.TaskInput.from_object({"embedding.$": "$.embedding.result"}),
        result_selector={"result.$": "$.Payload"},
        result_path="$.predicted_salary",
    )

    store_job_data_step = tasks.DynamoPutItem(
        scope=scope,
        id="StoreJobData",
        table=data_table,
        item={
            "job_id": tasks.DynamoAttributeValue.from_string(
                sfn.JsonPath.string_at("$.job_id")
            ),
            "html_text": tasks.DynamoAttributeValue.from_string(
                sfn.JsonPath.string_at("$.html_text")
            ),
            "cleaned_text": tasks.DynamoAttributeValue.from_string(
                sfn.JsonPath.string_at("$.cleaned_text.result")
            ),
        },
    )

    return (
        clean_text_step.next(create_embedding_step)
        .next(predict_salary_step)
        .next(store_job_data_step)
    )
