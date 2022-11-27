from aws_cdk import (Duration, Stack, aws_sqs as sqs, aws_events as events, aws_events_targets as targets)
from constructs import Construct

class RostrumStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here!

        # example resource
        queue = sqs.Queue(
            self, "RostrumQueue",
            visibility_timeout=Duration.seconds(300),
        )

        # Create an EventBus 
        bus = events.EventBus(self, "RostrumEventBus",
            event_bus_name="RostrumEventBus",
        )

        # Create a rule
        rule = events.Rule(self, "FiveMinutes",
            schedule=events.Schedule.rate(Duration.minutes(5)),
        )

        # Grant put events
        #bus.grant_put_events_to(rule)

        # Add EventBridge target to rule
        #rule.add_target(targets.EventBus(bus))
