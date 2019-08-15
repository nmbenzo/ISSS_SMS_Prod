# ISSS SMS Prod
A chatbot for international students at the University of San Francisco to communicate with. 

This service allows students to chat with a bot and ask a variety of questions common to F-1 international students 
studying at the University of San Francisco. 

The SMS Project has now been updated to integrate with Google DialogFlow via the
dialogflow v2 API.  

See the requirements.txt file for the code dependencies. 

The project has been deployed to AWS Lambda via the Zappa package for Python 3.6. In order to host on AWS, you'll need to first create an AWS account:https://aws.amazon.com/, and then create an IAM role and credentials for your project: https://aws.amazon.com/blogs/security/a-new-and-standardized-way-to-manage-credentials-in-the-aws-sdks/ Please see the Zappa docs for how to do this: https://github.com/Miserlou/Zappa#installation-and-configuration

Zappa requires a virtual environment to operate properly, so be sure to be in a env when you setup and deploy. 

---Recent Additions---

***Added Twilio SMS integration

***Added Gmail emailing capabilities

***Added Oracle SQL querying capabilities for ODSP

