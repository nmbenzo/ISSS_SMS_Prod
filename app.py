from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from auth_token import SECRET_KEY
from Dialogflow import smart_message
import phone_num_and_responses as responses
import major_advisor as major_advisor
from textblob import TextBlob
import logging


logging.basicConfig(format='%(asctime)s %(levelname)-8s '
    '[%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y:%H:%M:%S',
    level=logging.DEBUG,
    filename='logs.txt')

logger = logging.getLogger('Message Logger')

SECRET_KEY = SECRET_KEY
app = Flask(__name__)
app.config.from_object(__name__)


def set_session_response():
    """
    Get message response from user
    ::returns counter as an int
    """
    counter = session.get('counter', 0)
    counter += 1

    return counter


def find_isss_advisor():
    """find_isss_advisor is a function that checks for a specific
    majors in a list of majors and returns a string of the advisor's name if
    an inbound message for a major and a level of education match a major in
    the advisor's list
    """
    INBOUND_MESSAGE = request.form.get('Body').lower().strip()

    for i in major_advisor.Nina:
        if i.lower() in INBOUND_MESSAGE \
            and ('undergrad' in INBOUND_MESSAGE):
            return 'Nina'
        else:
            if i.lower() in INBOUND_MESSAGE and ('bachelor' in INBOUND_MESSAGE):
                return 'Nina'
    for i in major_advisor.Nathan:
        if i.lower() in INBOUND_MESSAGE \
            and ('undergrad' in INBOUND_MESSAGE) \
            or ('bachelor' in INBOUND_MESSAGE):
            return 'Nathan'
        else:
            if i.lower() in INBOUND_MESSAGE and ('bachelor' in INBOUND_MESSAGE):
                return 'Nathan'
    for i in major_advisor.Marcella:
        if i.lower() in INBOUND_MESSAGE \
            and ('master' in INBOUND_MESSAGE):
            return 'Marcella'
        else:
            if i.lower() in INBOUND_MESSAGE and ('grad' in INBOUND_MESSAGE):
                return 'Marcella'
    for i in major_advisor.Cynthia:
        if i.lower() in INBOUND_MESSAGE \
            and ('grad' in INBOUND_MESSAGE):
            return 'Cynthia'
        else:
            if i.lower() in INBOUND_MESSAGE and ('master' in INBOUND_MESSAGE):
                return 'Cynthia'


@app.route('/', methods=['POST'])
def send_sms_response():
    """
    Responds to an incoming message with a custom SMS response from the trained
    intents within DialogFlow
    ::returns sms response as a string
    """
    INBOUND_MESSAGE = request.form.get('Body').lower().strip()

    resp = MessagingResponse()
    menu_resp = responses.sms_responses()
    logger.info(INBOUND_MESSAGE)

    try:
        if INBOUND_MESSAGE:
            dialogflow_response = \
            smart_message.detect_intent_response(INBOUND_MESSAGE)
            resp.message(dialogflow_response)
            logger.info(f'{resp}')
            return str(resp)
    except:
        """
        If the DialogFlow API times out or fails to return a valid response,
        the code within the except block will run to maintain response 
        continuity.
        """
        # Save the new counter value in the session
        cookie = session['counter'] = set_session_response()

        # Use the body of the user's text message to create a new TextBlob object.
        text_blob = TextBlob(INBOUND_MESSAGE)

        # Get sentiment of the user's statement.
        # >>> sentiment = text_blob.sentiment
        # >>> sentiment.polarity
        # 0.0
        sentiment = text_blob.sentiment

        if ('who' in INBOUND_MESSAGE) and ('advisor' in INBOUND_MESSAGE):
            resp.message(menu_resp['who_is_advisor'])
            resp.message(menu_resp['major'])
            logger.info(f'{resp}')
            return str(resp)
        if INBOUND_MESSAGE != None:
            if find_isss_advisor() == 'Nina':
                resp.message(menu_resp['nina'])
                return str(resp)
            elif find_isss_advisor() == 'Nathan':
                resp.message(menu_resp['nathan'])
                return str(resp)
            elif find_isss_advisor() == 'Marcella':
                resp.message(menu_resp['marcella'])
                return str(resp)
            elif find_isss_advisor() is 'Cynthia':
                resp.message(menu_resp['cynthia'])
                return str(resp)
        if ('appointment' in INBOUND_MESSAGE) or ('advisor' in INBOUND_MESSAGE):
            resp.message(menu_resp['appt'])
            logger.info(f'{resp}')
            return str(resp)
        elif ('how' in INBOUND_MESSAGE) \
            and ('opt' not in INBOUND_MESSAGE) \
            and ('workshop' not in INBOUND_MESSAGE) \
            and ('leave' not in INBOUND_MESSAGE) \
            and ('unit' not in INBOUND_MESSAGE) \
            and ('transfer' not in INBOUND_MESSAGE) \
            and ('absence' not in INBOUND_MESSAGE) \
            and ('apply' not in INBOUND_MESSAGE) \
            and ('itin' not in INBOUND_MESSAGE) \
            and ('taxes' not in INBOUND_MESSAGE) \
            and ('extension' not in INBOUND_MESSAGE) \
            and ('internship' not in INBOUND_MESSAGE) \
            and ('social' not in INBOUND_MESSAGE) \
            and ('class' not in INBOUND_MESSAGE) \
            and ('travel' not in INBOUND_MESSAGE) \
            and ('ssn' not in INBOUND_MESSAGE) \
            and ('visa' not in INBOUND_MESSAGE) \
            and ('credit' not in INBOUND_MESSAGE) \
            and ('extend' not in INBOUND_MESSAGE) \
            or ('ready' in INBOUND_MESSAGE):
            resp.message(menu_resp['contact_isss'])
            resp.message((menu_resp['processing_time']))
            logger.info(f'{resp}')
            return str(resp)
        elif ('when' in INBOUND_MESSAGE) \
            and ('opt' not in INBOUND_MESSAGE) \
            and ('workshop' not in INBOUND_MESSAGE) \
            and ('leave' not in INBOUND_MESSAGE) \
            and ('transfer' not in INBOUND_MESSAGE) \
            and ('absence' not in INBOUND_MESSAGE) \
            and ('apply' not in INBOUND_MESSAGE) \
            and ('itin' not in INBOUND_MESSAGE) \
            and ('taxes' not in INBOUND_MESSAGE) \
            or ('ready' in INBOUND_MESSAGE):
            resp.message(menu_resp['contact_isss'])
            resp.message((menu_resp['processing_time']))
            logger.info(f'{resp}')
            return str(resp)
        elif 'transfer' in INBOUND_MESSAGE:
            resp.message(menu_resp['transfer'])
            logger.info(f'{resp}')
            return str(resp)
        elif 'call' in INBOUND_MESSAGE:
            resp.message(menu_resp['call'])
            logger.info(f'{resp}')
            return str(resp)
        elif 'email' in INBOUND_MESSAGE:
            resp.message(menu_resp['email'])
            logger.info(f'{resp}')
            return str(resp)
        elif ('workshop' in INBOUND_MESSAGE) and ('opt' in INBOUND_MESSAGE):
            resp.message(menu_resp['workshop'])
            logger.info(f'{resp}')
            return str(resp)
        elif ('workshop' in INBOUND_MESSAGE) and ('tax' in INBOUND_MESSAGE):
            resp.message(menu_resp['workshop'])
            logger.info(f'{resp}')
            return str(resp)
        elif ('workshop' in INBOUND_MESSAGE):
            resp.message(menu_resp['workshop'])
            logger.info(f'{resp}')
            return str(resp)
        elif ('tax' in INBOUND_MESSAGE) or ('taxes' in INBOUND_MESSAGE) \
            or ('itin' in INBOUND_MESSAGE):
            resp.message(menu_resp['taxes'])
            logger.info(f'{resp}')
            return str(resp)
        elif ('visa' in INBOUND_MESSAGE) and ('apply' not in INBOUND_MESSAGE) \
            and ('letter' not in INBOUND_MESSAGE):
            resp.message(menu_resp['visa'])
            logger.info(f'{resp}')
            return str(resp)
        elif ('opt' in INBOUND_MESSAGE) and ('travel' in INBOUND_MESSAGE):
            resp.message(menu_resp['opt_travel'])
            logger.info(f'{resp}')
            return str(resp)
        elif ('travel' in INBOUND_MESSAGE) and ('apply' not in INBOUND_MESSAGE) \
            and ('request' not in INBOUND_MESSAGE):
            resp.message(menu_resp['travel_1'])
            resp.message(menu_resp['travel_2'])
            resp.message(menu_resp['travel_3'])
            logger.info(f'{resp}')
            return str(resp)
        elif ('how' in INBOUND_MESSAGE) and ('credit' in INBOUND_MESSAGE) \
            or ('full time' in INBOUND_MESSAGE) or ('credit' in INBOUND_MESSAGE) \
            or ('unit' in INBOUND_MESSAGE):
            resp.message(menu_resp['full_time'])
            resp.message(menu_resp['full_time_reminder'])
            logger.info(f'{resp}')
            return str(resp)
        elif ('opt' in INBOUND_MESSAGE) and \
            ('how' in INBOUND_MESSAGE) and ('apply' not in INBOUND_MESSAGE):
            resp.message(menu_resp['opt_processing_time'])
            logger.info(f'{resp}')
            return str(resp)
        elif ('opt' in INBOUND_MESSAGE) and \
            ('how' in INBOUND_MESSAGE) and ('apply' in INBOUND_MESSAGE):
            resp.message(menu_resp['how_opt_apply'])
            resp.message(menu_resp['register_workshop'])
            logger.info(f'{resp}')
            return str(resp)
        elif ('when' in INBOUND_MESSAGE) and \
            ('opt' in INBOUND_MESSAGE) and ('apply' in INBOUND_MESSAGE):
            resp.message(menu_resp['opt_apply'])
            logger.info(f'{resp}')
            return str(resp)
        elif ('when' in INBOUND_MESSAGE) and ('opt' in INBOUND_MESSAGE):
            resp.message(menu_resp['opt_processing_time'])
            logger.info(f'{resp}')
            return str(resp)
        elif ('opt' in INBOUND_MESSAGE) and ('apply' not in INBOUND_MESSAGE):
            resp.message(menu_resp['opt'])
            logger.info(f'{resp}')
            return str(resp)
        elif ('cpt' in INBOUND_MESSAGE) and ('apply' not in INBOUND_MESSAGE):
            resp.message(menu_resp['cpt'])
            logger.info(f'{resp}')
            return str(resp)
        elif ('intern' in INBOUND_MESSAGE) or ('work' in INBOUND_MESSAGE) \
            or ('off campus' in INBOUND_MESSAGE) or ('job' in INBOUND_MESSAGE) \
            or ('extern' in INBOUND_MESSAGE) or \
            ('employment' in INBOUND_MESSAGE):
            resp.message(menu_resp['employment'])
            logger.info(f'{resp}')
            return str(resp)
        elif ('ssn' in INBOUND_MESSAGE) or \
            ('social security' in INBOUND_MESSAGE) \
            or ('financial aid' in INBOUND_MESSAGE):
            resp.message(menu_resp['gen_student_life'])
            logger.info(f'{resp}')
            return str(resp)
        elif ('extension' in INBOUND_MESSAGE) or ('extend' in INBOUND_MESSAGE):
            resp.message(menu_resp['p_extension_1'])
            resp.message(menu_resp['p_extension_2'])
            resp.message(menu_resp['p_extension_3'])
            logger.info(f'{resp}')
            return str(resp)
        elif ('rcl' in INBOUND_MESSAGE) and ('apply' not in INBOUND_MESSAGE) \
            or ('reduced' in INBOUND_MESSAGE) \
            or ('reduced course load' in INBOUND_MESSAGE):
            resp.message(menu_resp['rcl'])
            resp.message(menu_resp['rcl_link'])
            resp.message(menu_resp['full_time_reminder'])
            logger.info(f'{resp}')
            return str(resp)
        elif ('leave of absence' in INBOUND_MESSAGE) \
            or ('loa' in INBOUND_MESSAGE) or ('leave' in INBOUND_MESSAGE) \
            or ('withdraw' in INBOUND_MESSAGE):
            resp.message(menu_resp['loa_wd'])
            logger.info(f'{resp}')
            return str(resp)
        elif ('apply' in INBOUND_MESSAGE) or ('travel' in INBOUND_MESSAGE) \
            or ('cpt' in INBOUND_MESSAGE) or ('letter' in INBOUND_MESSAGE) \
            or ('request' in INBOUND_MESSAGE) or ('i20' in INBOUND_MESSAGE) \
            or ('i-20' in INBOUND_MESSAGE) or ('rcl' in INBOUND_MESSAGE) \
            or ('reduced course load' in INBOUND_MESSAGE):
            resp.message(menu_resp['isss_request'])
            resp.message(menu_resp['disclaimer'])
            logger.info(f'{resp}')
            return str(resp)
        elif ('class' in INBOUND_MESSAGE) or ('course' in INBOUND_MESSAGE) \
            or ('drop' in INBOUND_MESSAGE):
            resp.message(menu_resp['academic'])
            resp.message(menu_resp['full_time_reminder'])
            logger.info(f'{resp}')
            return str(resp)
        elif ('hello' in INBOUND_MESSAGE) or ('hey' in INBOUND_MESSAGE) \
            or ('hi' in INBOUND_MESSAGE):
            resp.message(menu_resp['menu'])
            logger.info(f'{resp}')
            return str(resp)
        elif 'isss' in INBOUND_MESSAGE:
            resp.message(menu_resp['isss'])
            logger.info(f'{resp}')
            return str(resp)
        elif 'website' in INBOUND_MESSAGE:
            resp.message(menu_resp['website'])
            logger.info(f'{resp}')
            return str(resp)
        elif 'menu' in INBOUND_MESSAGE:
            resp.message(menu_resp['menu'])
            logger.info(f'{resp}')
            return str(resp)

        # If the polarity of the sentiment is greater than zero, the statement is
        # positive.  Highest positivity is 1.0
        elif sentiment.polarity > 0:
            resp.message(menu_resp['sentiment_resp1'])
            return str(resp)

        # If the polarity of the sentiment is less than zero, the statement is
        # negative.  Lowest negativity is -1.0.
        elif sentiment.polarity < 0:
            resp.message(menu_resp['sentiment_resp2'])
            resp.message(menu_resp['menu'])
            logger.info(f'{resp}')
            return str(resp)

        # If the polarity is 0.0, TextBlob was unable to determine the sentiment
        # of the statement.  In this case, we'll return a neutral response in turn.
        elif INBOUND_MESSAGE != None and cookie <= 1:
            cookie += 1
            resp.message(menu_resp['sentiment_resp3'])
            return str(resp)
        else:
            resp.message((menu_resp['renew_session']))
            session['counter'] = 0
            return str(resp)



if __name__ == "__main__":
    app.run(debug=True)