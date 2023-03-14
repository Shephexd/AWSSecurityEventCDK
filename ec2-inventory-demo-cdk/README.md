# Inventory Management for EC2



## What is Inventory Management for EC2?

Amazon Elastic Compute Cloud (EC2) is a popular cloud computing service offered by Amazon Web Services (AWS) that allows users to rent virtual machines (VMs) in the cloud. Managing inventory for Amazon EC2 involves tracking the various components that make up EC2 instances, including the VMs themselves, the storage volumes, and the networking components.



## AWS Services in Demo

**Inventory Management**

- Amazon EC2
- AWS Systems Manager
- Amazon Inspector



**Monitoring Services and Notification**

- Amazon SecurityHub
- Amazon SNS
- Amazon SES (Simple Eamil Services)



## Requirements

- AWS CDK (python) - [CDK Install Guide](https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-python.html)
- AWS CLI - [AWS CLI Install Guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)



## DemoArchitecture

![FullInventoryManagement](https://github.com/Shephexd/aws-iac-samples/blob/develop/static/inventory-management/FullInventoryManagement.png?raw=true)



## Demo Steps



### Before start

### Git Clone Repository

```bash
git clone https://github.com/Shephexd/aws-iac-samples/tree/develop
cd security-
```



### 1. DemoVPCStack

![demoVPC](https://github.com/Shephexd/aws-iac-samples/blob/develop/static/inventory-management/demoVPC.png?raw=true)



#### 1-a. Deploy DemoVPCStack

```bash
cdk deploy DemoVPCStack
```



### 2. InventoryManagementStack

![InventoryManagementWithInspector](https://github.com/Shephexd/aws-iac-samples/blob/develop/static/inventory-management/InventoryManagementWithInspector.png?raw=true)




#### 2-a. Deploy InventoryManagementStack

```bash
cdk deploy InventoryManagementStack --parameters TargetEmail=YOUR_EMAIL@DOMAIN.COM
```



#### 2-b. Enable Inspector

```bash
aws inspector2 enable --resource-types EC2
```



### 3. SecurityReportStack



#### 3-a. Deploy SecurityReportStack

```bash
cdk deploy SecurityReportStack --parameters TargetEmail=YOUR_EMAIL@DOMAIN.COM
```

![FullInventoryManagement](https://github.com/Shephexd/aws-iac-samples/blob/develop/static/inventory-management/FullInventoryManagement.png?raw=True)



## Conclusion
