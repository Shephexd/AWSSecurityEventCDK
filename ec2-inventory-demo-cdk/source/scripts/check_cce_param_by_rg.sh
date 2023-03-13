#!/bin/bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
TARGET_RESOURCE_GROUP="DevWASInstances"
echo "Run CCE Check, ResourceGroup=$TARGET_RESOURCE_GROUP"

aws ssm send-command --document-name "AWS-RunShellScript" --document-version "1" \
--targets "[{\"Key\":\"resource-groups:Name\",\"Values\":[\"$TARGET_RESOURCE_GROUP\"]}]" \
--parameters "$(cat $SCRIPT_DIR/cce_check_commands.json)" \
--timeout-seconds 600 --max-concurrency "50" --max-errors "0" \
--output-s3-bucket-name "inventory-demo-cce" \
--cloud-watch-output-config '{"CloudWatchLogGroupName":"cce-result","CloudWatchOutputEnabled":true}' \
--region ap-northeast-2