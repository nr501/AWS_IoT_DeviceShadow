# AWS_IoT_DeviceShadow

## Summary

This project walks you through the process of building an application to mirror the status of IoT devices. The project contains a frontend which displays the current status of your device as well as establishing a connection to AWS IoT. After going through this README you will have the following frontend written in REACT, which you can use to monitor your IoT Device in form of a digital shadow.

![IoT_Frontend](./src/assets/Frontend.png)
## Prerequesites:

Note: For a standardized development environment, consider following our [Cloud9 setup](https://docs.aws.amazon.com/cloud9/latest/user-guide/setting-up.html) guide instead.


This sample depends on AWS services that might not yet be available in all regions. Please make sure to run this sample in the regions for following AWS services:
  - AWS Amplify - [supported regions](https://docs.aws.amazon.com/general/latest/gr/amplify.html)
  - AWS Cognito - [supported regions](https://docs.aws.amazon.com/general/latest/gr/amplify.html)

## Deploying the IoT Frontend 

1. Install libraries
  
  ```bash
     #Install the Amplify CLI 
     npm install -g @aws-amplify/cli
  ```

  ```bash
     #Pull this Git repository
     git clone https://github.com/nr501/AWS_IoT_DeviceShadow.git
     
     cd AWS_IoT_DeviceShadow
  ```

2. Create Amplify User
  The Amplify User needs permissions in order call the Amplify service
  ```bash
     amplify configure
  ```
  Follow the steps:
  a) Sign in to your AWS administrator account
  b) Specify AWS Region you want to deploy the Amplify application
  c) Specify the username of the IAM User that you will create in the next step 
  d) Click on the link provided to log into the AWS Management Console
  e) Select AWS access type (access key for programmatic access is sufficient) - Next: Permissions
  f) Verify the Policy name "AdministratorAccess-Amplify" is preselected - if not -> select the checkbox 
  g) Next: Tags and Next: Review
  h) Create User and copy the Access key ID and secret access key to a local NotePad
  i) Back in your Cloud9 environment enter the secret key ID and secret access key and press enter 
  Congratulation ! You setup your Amplify environment and created the Amplify User 
   
3. Initialize Amplify project 

  ```bash
     amplify init
  ```
  Note: This step will create AWS resources (S3 Bucket, IAM Role) 
  
  ```bash
     amplify push
     npm init
  ```
  
  In the next step you will set up the frontend by hosting it with Amplify 
  
  ```bash 
     amplify add hosting
  ```
  
When prompted: 
a) Hosting with Amplify console - 
b) Manuel deployment
     
  ```bash 
     amplify publish
  ```

In case the command was successfull you can open the URL provided which will redirect you to the Sign In of your frontend 


4. Create User for Frontend in Amazon Cognito 

Amazon Cognito lets you add user sign-up, sign-in, and access control to your web and mobile apps quickly and easily. Log into the AWS Manamgenet Console and search in the services for Amazon Cognito. Open the existing User Pool and edit the option "User sign ups allowed?" to "Only allow administrators to create users". On the left tab click on "Users and groups" and "create user". Switch to the URL from the previous step and log in with the credentials of the User you've just created

5. Create IAM Policiy for AWS IoT

Switch to the AWS Manamgement Console and follow Step 1 described [here](https://docs.amplify.aws/lib/pubsub/getting-started/q/platform/js/#aws-iot). Once created switch to your Cloud9 environment and attach the policy with: 

```bash 
   aws iot attach-policy --policy-name <policy name step 5> --target <Cognito identity pool ID>
  ```
  
 The Congito Identity Pool ID can be found in the in the Idenetity pool in Amazon Congito 

6. 


