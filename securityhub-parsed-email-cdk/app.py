#!/usr/bin/env python3

import aws_cdk as cdk

from stacks.security_notification import SecurityEventNotificationStack


app = cdk.App()
SecurityEventNotificationStack(app, "SecurityEventNotificationStack")

app.synth()
