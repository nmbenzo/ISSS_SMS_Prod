import os
os.getcwd()

GLBL_USER_CHOICE = """
Please select one of the following to begin workflow:
- 'm' - Send SMS Message
- 'e' - Send Emails
- 'q' - Quit
"""

EMAIL_TO_STUDENT_template = """
Choose an email template to send to the student: 
- 'e' - Email to Singular Student
- 'm' - Email to Multiple Students
- 'es' - Send single email message from Banner Query
- 'eb' - Send blast email message from Banner Query
"""

EMAIL_TO_STUDENT_type = """
Which which email would you like to send: 
- 'f' - Students who have not paid the I-901 fee
- 'u' - Students who are underenrolled 
- 'p' - Students who have a bad phone number in ISSM
- 'a' - Students who have a bad address in ISSM
"""


SMS_MESSAGE = """
Please select one of the following:
- 's' - Send singular SMS Message
- 'b' - Send SMS Blast from Banner Query
- 'cb' - Send SMS Blast from custom list
- 'ts' - Send single test message from Banner Query
- 'tb' - Send blast test message from Banner Query
"""
