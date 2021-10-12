import aws_cdk.aws_iam as iam
import constructs


def invoke_lambda(scope: constructs.Construct) -> iam.ManagedPolicy:
    return iam.ManagedPolicy(
        scope=scope,
        id="AllowLambdaInvoke",
        managed_policy_name="AllowLambdaInvoke",
        document=iam.PolicyDocument(
            statements=[
                iam.PolicyStatement(
                    resources=["arn:aws:lambda:::function:*"],
                    effect=iam.Effect.ALLOW,
                    actions=["lambda:InvokeFunction"],
                )
            ]
        ),
    )


def cloud_watch_log(
    scope: constructs.Construct, log_group_arn: str
) -> iam.ManagedPolicy:
    return iam.ManagedPolicy(
        scope=scope,
        id="CloudWatchLogAccess",
        managed_policy_name="CloudWatchLogAccess",
        document=iam.PolicyDocument(
            statements=[
                iam.PolicyStatement(
                    resources=[log_group_arn],
                    effect=iam.Effect.ALLOW,
                    actions=[
                        "logs:CreateLogDelivery",
                        "logs:GetLogDelivery",
                        "logs:UpdateLogDelivery",
                        "logs:DeleteLogDelivery",
                        "logs:ListLogDeliveries",
                        "logs:PutResourcePolicy",
                        "logs:DescribeResourcePolicies",
                        "logs:DescribeLogGroups",
                    ],
                )
            ]
        ),
    )
