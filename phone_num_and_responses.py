from flask import Flask, request
from message_lists import ISSS_list_dict


app = Flask(__name__)
app.config.from_object(__name__)


def get_sender_name():
    """
    Function that references a dictionary of available names (key)
    and phone numbers (value) which is passed to the sms_responses() function
    for custom greetings for each user.
    ::returns dict key as var name
    """
    from_number = request.values.get('From')

    if from_number in ISSS_list_dict:
        name = ISSS_list_dict[from_number]
    else:
        name = "Friend"
    return name


def sms_responses():
    """
    Function that returns a dictionary of available sms responses to be used
    by the send_sms_response() function
    """
    inbound_message = request.form.get('Body')

    menu = f" Hello, {get_sender_name()}! This is ISSS's chat messenger " \
        f"service. You can text questions or chat with this number to help " \
        f"you find answers to questions common among international students. " \
        f"\n\nTry typing ''make an appointment'' or ''register for a workshop.''" \
        f" You can also ask questions about OPT and CPT." \
        f"\n\n*Your response is not case-sensitive"

    appt = f"Sure thing, {get_sender_name()}! Click here to make an " \
        f"appointment with your advisor: https://isss.checkappointments.com/"
    isss_request = f'Hi, {get_sender_name()}! Thanks for asking about, ' \
        f'"{inbound_message}". In order to best help you, please submit an ' \
        f'online request: ' \
        f'https://form.jotform.com/USFISSS/isss-request-form'
    disclaimer = "Document uploads may be required to complete your request."
    opt = f"Many students have question about OPT, {get_sender_name()}! Not " \
        f"to worry, please click here to learn more about OPT: " \
        f"https://myusf.usfca.edu/isss/students/f-1/employment/opt "
    cpt = f"So you'd like to learn more about CPT, {get_sender_name()}, " \
        f"correct? Great! Please click here to learn about CPT: " \
        f"https://myusf.usfca.edu/isss/students/f-1/employment/cpt"
    isss = f'Hello, {get_sender_name()}! Thank you for inquiring more about ' \
        f'ISSS. To get in touch with ISSS please contact: isss@usfca.edu, ' \
        f'call us at: 415-422-2654, or visit our office on Main Campus ' \
        f'- UC 5th floor. Our normal business hours are Monday-Friday from' \
        f' 9am-5pm. \nTo schedule an appointment with ' \
        f'your advisor click: https://isss.checkappointments.com/'
    loa_wd = f"Good day, {get_sender_name()}. You've indicated that you would " \
        f"like information about taking a leave of absence or withdrawing " \
        f"from USF. Click here to learn what you will need to do: " \
        f"https://myusf.usfca.edu/isss/students/f-1/leave-of-absence-withdrawal"

    call = '4154222654'
    email = 'isss@usfca.edu'

    website = 'https://myusf.usfca.edu/isss'
    contact_isss = f'Hi {get_sender_name()}, you can get a quicker answer if ' \
        f'you call or email ISSS. ' \
        f'\n\nCall: 415-422-2654' \
        f'\nEmail: isss@usfca.edu'
    employment = f"Hi, {get_sender_name()}, I think you're asking about " \
        f"employment as an F-1 student. There are several types of employment " \
        f"available to international students. Please visit our employment page" \
        f" for more information: " \
        f"\nhttps://myusf.usfca.edu/isss/students/f-1/employment"
    processing_time_requests = f'As a reminder, ISSS has a 5-day processing ' \
        f'time for complete student requests.'
    workshop = f"Great to hear you'd like more information about our workshops, " \
        f"{get_sender_name()}. You can learn more or register for a workshop " \
        f"here: \nhttps://isss.checkappointments.com/"
    register_workshop = f'You can register here: ' \
        f'https://isss.checkappointments.com/'
    opt_processing_times_general = 'ISSS has a 5-day processing time for ' \
       'complete student requests. After you mail your OPT application, it ' \
       'will take USCIS between 90-110 days to process OPT applications. ' \
       'Please be sure to plan your employment or travel carefully.'
    opt_travel = f'There are very specific guidelines you must be aware of while' \
        f' traveling on OPT, {get_sender_name()}. Please see the ' \
        f'ISSS guidelines for travel while on OPT:' \
        f'\n\nhttps://myusf.usfca.edu/isss/students/f-1/employment/opt/after-mailing-application'
    transfer = f'{get_sender_name()}, if you would like to transfer to ' \
        f'another university you will need to ask ISSS to transfer your SEVIS ' \
        f'record. Please request a transfer out here: ' \
        f'\nhttps://form.jotform.com/USFISSS/isss-request-form'
    sentiment_resp1 = f"That's great to hear, {get_sender_name()}! " \
        f"Is there anything else ISSS can help you with today?"
    sentiment_resp2 = f"Oh no - we're sorry to hear that {get_sender_name()}! " \
        f"Let's bring you back to the main menu so we can better assist you..."
    sentiment_resp3 = f"Thanks for letting us know about that, " \
        f"{get_sender_name()}. You can access ISSS services or get information " \
        f"with by communicating with this chat service. " \
        f'\n\nTry asking a question about OPT or scheduling an appointment. ' \
        f'You can also return to the main ISSS menu by typing "menu". '
    renew_session_response = f"We sincerely apologize, {get_sender_name()}. " \
        f"We could not understand your response. Please contact ISSS directly " \
        f"if you cannot find your answer here." \
        f"\nCall: 415-422-2654 \nEmail: isss@usfca.edu"
    gen_intl_student_life = f"Hello, {get_sender_name()}! Thank you for asking " \
        f"about this. You can find more information about this topic on our " \
        f"website: \nhttps://myusf.usfca.edu/isss/students/living-in-the-us"
    visa_response = f"For visa related questions, {get_sender_name()}, it " \
        f"is best to contact ISSS directly. \n\nCall: 415-422-2654 " \
        f"\nEmail: isss@usfca.edu"
    program_extension_1 = f'Hello, {get_sender_name()}! Thank you for asking about ' \
        f'a program extension. '
    program_extension_2 = f'In order to be eligible for a program extension' \
        f' you will have to have your program advisor complete the ISSS program' \
        f' extension form. ' \
        f'\nhttps://myusf.usfca.edu/isss/departments-faculty/program-extension-overview'
    program_extension_3 = f'We also recommend scheduling an appointment with your ' \
        f'ISSS advisor.'
    opt_apply = f'Thanks for asking about this, {get_sender_name()}. Students ' \
        f'can apply for OPT as early as 90 days before their I-20 program end' \
        f' date through their 60 day grace period after they complete their ' \
        f'program.'
    how_apply_opt = f'Good question! The first step is to attend an OPT ' \
        f'workshop. Completing the workshop, students become eligible to apply' \
        f' for OPT through ISSS.'
    academic_advising = f'Hi {get_sender_name()}! This seems like a question ' \
        f'that may be more appropriate for your academic or program advisor. ' \
        f'Please direct this question to your program advisor and let us know ' \
        f'if there is anything else we can do.'
    full_time_reminder = f'As a reminder, F1 students are required to be ' \
        f'enrolled full-time unless they have received authorization to study ' \
        f'below full-time through ISSS.'
    taxes = f'Thank you for asking about taxes, {get_sender_name()}. ' \
        f'Please see our ISSS tax page for more tax information: ' \
        f'\nhttps://myusf.usfca.edu/isss/taxes'
    who_is_advisor = f'Great question, {get_sender_name()}! ' \
        f'\n\nWe will need to know your ' \
        f'education level: "grad / undergrad" or "bachelors / masters" in ' \
        f'and your major. '
    major_response = f'\n\nPlease tell us your education level and major: '
    Nina = f'You stated that your major is "{inbound_message}." ' \
        f'Your ISSS advisor is Nina Lopes: nlopes@usfca.edu'
    Nathan = f'You stated that your major is "{inbound_message}." ' \
        'Your ISSS advisor is Nathan Benzschawel: nbenzschawel@usfca.edu'
    Marcella = f'You stated that your major is "{inbound_message}." ' \
        'Your ISSS advisor is Marcella Deproto: mjdeproto@usfca.edu'
    Cynthia = f'You stated that your major is "{inbound_message}." ' \
        'Your ISSS advisor is Cynthia Lai: ylai9@usfca.edu'
    travel_1 = f'Hi {get_sender_name()}, thank you for asking about F-1 travel ' \
        f'requirements. In order to travel and re-enter you will need the ' \
        f'following documents: '
    travel_2 = f'*Valid passport: expiration at least 6-months into the future' \
        f'\n*A valid F-1 or J-1 visa \n*A valid I-20 or DS-2019 form with ' \
        f'travel endorsement'
    travel_3 = 'For current students, an I-20 or DS-2019 travel endorsement ' \
        'is valid for 12 months, or until the expiration of the document, ' \
        'whichever is first.'
    rcl = f'Students may be authorized for part-time study while maintaining ' \
        f'their F-1 status. For more information on when students can study ' \
        f'part-time, please click here: '
    rcl_link = f'\n\nhttps://myusf.usfca.edu/isss/students/f-1/change-program'
    full_time = f"Excellent question, {get_sender_name()}! Full-time status " \
        f"is considered 12 or more credits the undergraduate level and 6 or " \
        f"more units at the graduate level."

    return \
        {
            'menu': menu,
            'appt': appt,
            'isss_request': isss_request,
            'disclaimer': disclaimer,
            'opt': opt,
            'cpt': cpt,
            'isss': isss,
            'loa_wd': loa_wd,
            'nina': Nina,
            'nathan': Nathan,
            'marcella': Marcella,
            'cynthia': Cynthia,
            'call': call,
            'email': email,
            'transfer': transfer,
            'processing_time': processing_time_requests,
            'opt_processing_time': opt_processing_times_general,
            'opt_travel': opt_travel,
            'website': website,
            'workshop': workshop,
            'visa': visa_response,
            'employment': employment,
            'opt_apply': opt_apply,
            'how_opt_apply': how_apply_opt,
            'register_workshop': register_workshop,
            'rcl': rcl,
            'rcl_link': rcl_link,
            'taxes': taxes,
            'travel_1':travel_1,
            'travel_2': travel_2,
            'travel_3': travel_3,
            'full_time': full_time,
            'gen_student_life': gen_intl_student_life,
            'academic': academic_advising,
            'sentiment_resp1': sentiment_resp1,
            'sentiment_resp2': sentiment_resp2,
            'sentiment_resp3': sentiment_resp3,
            'contact_isss': contact_isss,
            'who_is_advisor': who_is_advisor,
            'major': major_response,
            'renew_session': renew_session_response,
            'p_extension_1': program_extension_1,
            'p_extension_2': program_extension_2,
            'p_extension_3': program_extension_3,
            'full_time_reminder': full_time_reminder
        }

