#/bin/bash
aws securityhub batch-import-findings --findings '[{
        "AwsAccountId": "$ACCOUNT_ID",
        "CreatedAt": "2023-01-13T14:53:33.832Z",
        "Description": "Vulnerability Check Test4",
        "GeneratorId": "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/2.2",
        "Id": "Id1",
        "ProductArn": "arn:aws:securityhub:$REGION:$ACCOUNT_ID:product/$ACCOUNT_ID/default",
        "Resources": [
            {
                "Id": "arn:aws:cloudtrail:$REGION:$ACCOUNT_ID:trail/TrailName3",
                "Partition": "aws",
                "Region": "$REGION",
                "Type": "AwsCloudTrailTrail"
            }
        ],
        "SchemaVersion": "2018-10-08",
        "Title": "CloudTrail trail vulnerability55",
        "UpdatedAt": "2023-01-13T14:53:33.832Z",
        "Types": [
            "Software and Configuration Checks/Vulnerabilities/CVE"
        ],
        "Severity": {
            "Label": "INFORMATIONAL",
            "Original": "0"
        }
    }]'