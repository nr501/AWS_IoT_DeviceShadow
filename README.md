# AWS_IoT_DeviceShadow

## Summary

This project walks you through the process of building an application to mirror the status of IoT devices. The project contains a frontend which displays the current status of your device as well as establishing a connection to AWS IoT. After going through this README you will have the following frontend written in REACT, which you can use to monitor your IoT Device in form of a digital shadow.


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
  1. Sign in to your AWS administrator account
  2. Specify AWS Region you want to deploy the Amplify application
  3. Specify the username of the IAM User that you will create in the next step 
  4. Click on the link provided to log into the AWS Management Console
  5. Select AWS access type (access key for programmatic access is sufficient) - Next: Permissions
  6. Verify the Policy name "AdministratorAccess-Amplify" is preselected - if not -> select the checkbox 
  7. Next: Tags and Next: Review
  8. Create User and copy the Access key ID and secret access key to a local NotePad
  9. Back in your Cloud9 environment enter the secret key ID and secret access key and press enter 
  10. Congratulation ! You setup your Amplify environment and created the Amplify User 
  
  
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
  
  1. ```bash amplify add hosting``` 

     Follow the steps accordingly: 
     Hosting with Amplify console 
     Manuel deployment
     
     
  2. ```bash amplify publish```



  
