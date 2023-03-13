#!/usr/bin/env python3

import aws_cdk as cdk

from stacks.inventory_management_stack import InventoryManagementStack
from stacks.vpc_setup_stack import VPCSetupStack
from stacks.secuirty_report_stack import DailyEmailReportStack


app = cdk.App()
VPCSetupStack(app, "DemoVPCStack")
InventoryManagementStack(app, "InventoryManagementStack")
DailyEmailReportStack(app, "SecurityReportStack")
app.synth()
