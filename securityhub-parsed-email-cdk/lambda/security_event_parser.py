import logging
import boto3
import os
from dataclasses import dataclass
from typing import List, Dict


@dataclass
class SecurityHubFindings:
    version: str
    id: str
    detail_type: str
    source: str
    account: str
    time: str
    region: str
    resources: List[str]
    detail: Dict[str, List[Dict]]


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def render_message(finding: SecurityHubFindings):
    response = \
      f"""Detail Type: {finding.detail_type}
      Source: {finding.source}
      Account: {finding.account}
      Region: {finding.region}
      Time: {finding.time}
      Resources: {finding.resources}
      Detail: {finding.detail}
      """
    return response


def lambda_handler(event, context):
    logging.info(repr(event))
    event["detail_type"] = event.pop("detail-type", "")
    finding = SecurityHubFindings(**event)

    _message = render_message(finding=finding)
    client = boto3.client('sns')
    client.publish(
        TopicArn=os.environ["TopicArn"],
        Subject=f"[SecurityHub] {finding.detail_type}",
        Message=_message
    )
    logging.info(_message)
