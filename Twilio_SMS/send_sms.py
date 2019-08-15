from twilio.rest import Client
from auth_token import account_sid, auth_token, myTwilionum
from Twilio_SMS.message_lists import isss_list, test_list, k_b
from Twilio_SMS.sms_templates import SV_body, General_ISSS_response, \
General_response, Test_response
from Banner_Connections.Initialize_Oracle_Connection import \
banner_odsp_handler, banner_ODSP_tele
import Banner_Connections.queries as query


client = Client(account_sid, auth_token)

call_back = 'https://postb.in/sGF3chFo'

content_list = {
    's': SV_body,
    't': Test_response,
    'g': General_ISSS_response,
    'gr': General_response
}

group_list = {'is': isss_list, 'ts': test_list, 'kb': k_b}

group_choices = ['is - ISSS Staff','ts - Test']

content_choices = [
    's - Status Verification Incomplete',
    't - Test',
    'g - General ISSS','gr - General Response',
    '\nHit Enter to skip and create a custom message'
]


def get_message_content(content_list):
    print('\nWhich message would you like to send: ')
    for choice in content_choices:
        print(choice)
    content = input('\nYour Choice: ')
    for x in content_list.keys():
        if x == content:
            return content_list[x]


def get_blast_list(group_list):
    print('\nPick a target group:')
    for choice in group_choices:
        print(choice)
    which_list = input('\nInput a group you like to blast message: ')
    for x in group_list.keys():
        if x == which_list:
            return group_list[x]


def send_singular_sms(client, get_message_content):
    try:
        receiver = input('Phone Number: ')
        if get_message_content != None:
            message = client.messages. \
            create(body=get_message_content, from_=myTwilionum,
                   status_callback = call_back, to=receiver)
            print(message.sid)
            print(f'Message Sent to {receiver}')

        if get_message_content == None:
            content = input('Please type your message: ')
            message = client.messages. \
            create(body=content, from_=myTwilionum,
                       status_callback=call_back, to=receiver)
            print(message.sid)
            print(f'Message Sent to {receiver}')
    except:
        print('You must have a body or content in this function.')


def send_blast_sms(client, get_blast_list, body):
    try:
        if body != None:
            for number in get_blast_list:
                message = client.messages. \
                create(body=body, from_=myTwilionum, to=number)
                print(message.sid)
                print(f'Message Sent to {number} in requested list')

        if body == None:
            content = input('Please type your message: ')
            for number in get_blast_list:
                message = client.messages. \
                    create(body=content, from_=myTwilionum, to=number)
                print(message.sid)
                print(f'Messages sent to {number} in requested list')
    except:
        print('You must have a body or content in this function.')


def banner_query_sms_single(client, get_message_content):
    try:
        receiver = banner_ODSP_tele(banner_odsp_handler(),
                                    query.run_single_tele_query())
        if get_message_content != None:
            message = client.messages. \
            create(body=get_message_content, from_=myTwilionum,
                   status_callback = call_back, to=receiver)
            print(message.sid)
            print(f'Message Sent to {receiver}')

        if get_message_content == None:
            content = input('Please type your message: ')
            message = client.messages. \
                create(body=content, from_=myTwilionum,
                       status_callback=call_back, to=receiver)
            print(message.sid)
            print(f'Message Sent to {receiver}')
    except:
        print('You must have a body or content in this function.')


def banner_query_sms_blast(client, Banner_list, body):
    try:
        if body != None:
            for number in Banner_list:
                message = client.messages. \
                create(body=body, from_=myTwilionum, to=number)
                print(message.sid)
                print(f'Message Sent to {number} in requested list')

        if body == None:
            content = input('Please type your message: ')
            for number in Banner_list:
                message = client.messages. \
                    create(body=content, from_=myTwilionum, to=number)
                print(message.sid)
                print(f'Messages sent to {number} in requested list')
    except:
        print('You must have a body or content in this function.')



