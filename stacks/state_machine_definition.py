import aws_cdk.aws_stepfunctions as sfn
import constructs


def create_state_machine(scope: constructs.Construct) -> sfn.IChainable:
    return sfn.Pass(scope=scope, id="test_task")
