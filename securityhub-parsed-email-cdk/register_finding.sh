aws securityhub batch-import-findings --findings '[{
        "AwsAccountId": "770789602014",
        "CreatedAt": "2023-01-13T14:53:33.832Z",
        "Description": "Vulnerability Check Test4",
        "GeneratorId": "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/2.2",
        "Id": "Id1",
        "ProductArn": "arn:aws:securityhub:us-east-1:770789602014:product/770789602014/default",
        "Resources": [
            {
                "Id": "arn:aws:cloudtrail:us-east-1:770789602014:trail/TrailName3",
                "Partition": "aws",
                "Region": "us-east-1",
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