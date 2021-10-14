import aws_cdk.aws_iam as iam
import constructs


class Lambda:
    @staticmethod
    def invoke_functions(
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


class CwLog:
    @staticmethod
    def write_logs(
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
