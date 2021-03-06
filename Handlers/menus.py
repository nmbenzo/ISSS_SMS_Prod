import time
import Handlers.menu_selection_options as menu_options
import Handlers.import_modules as func


global_menu = menu_options.GLBL_USER_CHOICE


class Menu:
    """
    This class organizes the various menu options into methods and where the
    global_menu option is returned as an class attribute in each method
    """
    def __init__(self, global_menu):
        """Initializes the global_menu parameter"""
        self.global_menu = global_menu

    def sms(self):
        """
        Menu where users can select to send a text to a student or sms blast
        multiple students with custom text or pre-selected templates
        """
        user_input = input(menu_options.SMS_MESSAGE).lower()
        while user_input != 'q':
            if user_input == 's':
                func.send_singular_sms(func.client,
                func.get_message_content(func.content_list))
            elif user_input == 'b':
                func.banner_query_sms_blast(func.client,
                (func.banner_ODSP_tele(func.banner_odsp_handler(),
                                       func.active_cell_phone)),
                func.get_message_content(func.content_list))
            elif user_input == 'cb':
                func.send_blast_sms(func.client,
                func.get_blast_list(func.group_list),
                func.get_message_content(func.content_list))
            elif user_input == 'ts':
                func.banner_query_sms_single(func.client,
                func.get_message_content(func.content_list))
            elif user_input == 'tb':
                func.banner_query_sms_blast(func.client,
                (func.banner_ODSP_tele(func.banner_odsp_handler(),
                func.blast_test)), func.get_message_content(func.content_list))

            return global_menu

    def emails(self):
        """
        Menu where users can elect to send emails to students individually
        or email blast a group of students.
        """
        user_input = input(menu_options.EMAIL_TO_STUDENT_template).lower()
        while user_input != 'q':
            if user_input == 'e':
                func.singular_email(
                func.get_email_message_content(func.e_content_list))
                time.sleep(0.5)
            elif user_input == 'm':
                func.multiple_emails(
                func.get_email_blast_list(func.e_group_list),
                func.get_email_message_content(func.e_content_list))
                time.sleep(0.5)
            elif user_input == 'es':
                func.banner_query_singular_email(
                func.get_message_content(func.content_list))
            elif user_input == 'eb':
                func.banner_query_blast_email(
                func.get_message_content(func.content_list))
                time.sleep(0.5)
            return global_menu

