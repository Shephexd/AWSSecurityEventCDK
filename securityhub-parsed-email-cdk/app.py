#!/usr/bin/env python3

import aws_cdk as cdk

from stacks.security_notification import SecurityEventNotificationStack
from stacks.vpc_setup_stack import VPCSetupStack


app = cdk.App()
# SecurityEventNotificationStack(app, "SecurityEventNotificationStack")
VPCSetupStack(app, "DemoVPC")

app.synth()
