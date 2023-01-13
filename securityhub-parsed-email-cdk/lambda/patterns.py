from dataclasses import dataclass, Field
from typing import List, Dict

sample = {
   "version":"0",
   "id":"CWE-event-id",
   "detail-type":"Security Hub Findings - Imported",
   "source":"aws.securityhub",
   "account":"111122223333",
   "time":"2019-04-11T21:52:17Z",
   "region":"us-west-2",
   "resources":[
      "arn:aws:securityhub:us-west-2::product/aws/macie/arn:aws:macie:us-west-2:111122223333:integtest/trigger/6294d71b927c41cbab915159a8f326a3/alert/f2893b211841"
   ],
   "detail":{
      "findings": [{}]
   }
}


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


@dataclass
class SecurityHubFindingsCustomAction(SecurityHubFindings):
    detail: {

    }


sample["detail_type"] = sample.pop("detail-type", "")
print(SecurityHubFindings(**sample))
