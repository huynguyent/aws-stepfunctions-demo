import aws_cdk.aws_iam as iam
import constructs


def invoke_lambda_functions(
    scope: constructs.Construct, function_arns: list[str]
) -> iam.ManagedPolicy:
    return iam.ManagedPolicy(
        scope=scope,
        id="AllowLambdaInvoke",
        managed_policy_name="AllowLambdaInvoke",
        document=iam.PolicyDocument(
            statements=[
                iam.PolicyStatement(
                    resources=function_arns,
                    effect=iam.Effect.ALLOW,
                    actions=["lambda:InvokeFunction"],
                )
            ]
        ),
    )


def cloud_watch_log(
    scope: constructs.Construct, log_group_arns: list[str]
) -> iam.ManagedPolicy:
    return iam.ManagedPolicy(
        scope=scope,
        id="CloudWatchLogAccess",
        managed_policy_name="CloudWatchLogAccess",
        document=iam.PolicyDocument(
            statements=[
                iam.PolicyStatement(
                    resources=log_group_arns,
                    effect=iam.Effect.ALLOW,
                    actions=[
                        "logs:CreateLogGroup",
                        "logs:CreateLogStream",
                        "logs:PutLogEvents",
                    ],
                )
            ]
        ),
    )
