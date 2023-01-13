from aws_cdk import (
    aws_events,
    aws_eventschemas,
    aws_lambda,
    aws_lambda_destinations,
    aws_securityhub,
    aws_events_targets,
    aws_iam,
    aws_sns,
    Stack,
    NestedStack,
    CfnParameter
)
from constructs import Construct


class SecurityEventNotificationStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        email_address = CfnParameter(self, "TargetEmail", type="String",
                                     description="The name of the Amazon S3 bucket where uploaded files will be stored.")

        self.init_security_hub()
        sns_notification = SNSEmailForSecurityEvent(scope=self, construct_id="SNSForSecurityEvent",
                                                    email=email_address.value_as_string)
        email_parser = self.create_lambda_email_parser(sns_topic=sns_notification.topic)
        event_bridge = EventBridgeForSecurityStack(scope=self,
                                                   construct_id="EventBridgeForSecurityStack", parser=email_parser)

    def init_security_hub(self):
        security_hub = aws_securityhub.CfnHub(self, "MyCfnHub")
        return security_hub

    def create_lambda_email_parser(self, sns_topic):
        event_policy = aws_iam.PolicyStatement(effect=aws_iam.Effect.ALLOW,
                                               resources=['*'], actions=['events:PutEvents'])
        lambda_event_parser = aws_lambda.Function(self, "eventProducerLambda",
                                                  runtime=aws_lambda.Runtime.PYTHON_3_8,
                                                  handler="security_event_parser.lambda_handler",
                                                  code=aws_lambda.Code.from_asset("lambda"),
                                                  on_success=aws_lambda_destinations.SnsDestination(sns_topic)
                                                  )
        lambda_event_parser.add_to_role_policy(event_policy)
        return lambda_event_parser


class EventBridgeForSecurityStack(NestedStack):
    def __init__(self, scope: Construct, construct_id: str, parser: aws_lambda.Function, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        event_bus = self.create_event_bus()
        event_rule = self.create_rule(rule_name="SecurityHubInsightRule", event_bus=event_bus, parser=parser)

        event_rule.add_target(
            target=aws_events_targets.LambdaFunction(handler=parser)
        )

    def create_event_bus(self):
        event_bus = aws_events.EventBus(self, "SecurityEventBus")
        return event_bus

    def create_rule(self, rule_name: str, event_bus: aws_events.EventBus, parser: aws_lambda.Function):
        _event_pattern = {
            "source": ["aws.securityhub"]
        }
        _rule = aws_events.Rule(self, rule_name,
                                event_bus=event_bus,
                                event_pattern=aws_events.EventPattern(**_event_pattern))
        return _rule


class SNSEmailForSecurityEvent(NestedStack):
    def __init__(self, scope: Construct, construct_id: str, email: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.topic = aws_sns.Topic(self, id="security-alert-event")
        self.email_subscription =\
            aws_sns.Subscription(self,
                                 "security-event-subscription",
                                 topic=self.topic,
                                 endpoint=email,
                                 protocol=aws_sns.SubscriptionProtocol.EMAIL)
