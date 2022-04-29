from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.forms import FormAction
from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.events import AllSlotsReset
from .database_connectivity import FeedbackUpdate
import mysql.connector
from mysql.connector import Error
from PIL import Image

try:
    connection = mysql.connector.connect(host='10.12.129.200',
                                         database='welc_dev',
                                         port = 3306,
                                         user='mdevusr',
                                         password='q4828uru99kk')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor(buffered=True)
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)

########################################################################################
###################                QUESTIONS - M8                    ################### 
########################################################################################

class ActionFindDL201m8Q1(Action):

    def name(self) -> Text:
        return "action_find_dl201_m8_q1"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        if intent=="find_dl201_m8_q1":
            utter_dl201_q1 = ("SELECT answer FROM digital_tutor_chatbot WHERE intent = 'find_dl201_m8_q1'")  
            cursor.execute(utter_dl201_q1)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

            utter_dl201_cs1 = ("SELECT digital_tutor_case_summaries.case_summary_pdf, digital_tutor_chatbot.case_summary_1_reason FROM digital_tutor_case_summaries INNER JOIN digital_tutor_chatbot ON digital_tutor_chatbot.case_summary_1 = digital_tutor_case_summaries.intent AND digital_tutor_chatbot.intent = 'find_dl201_m8_q1'") 
            cursor.execute(utter_dl201_cs1)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

            utter_dl201_sr1 = ("SELECT digital_tutor_readings.reading_title, digital_tutor_chatbot.suggested_reading_1_reason FROM digital_tutor_readings INNER JOIN digital_tutor_chatbot ON digital_tutor_chatbot.suggested_reading_1 = digital_tutor_readings.intent AND digital_tutor_chatbot.intent = 'find_dl201_m8_q1'") 
            cursor.execute(utter_dl201_sr1)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindDL201m8Q1CS(Action):

    def name(self) -> Text:
        return "action_find_dl201_m8_q1_cs"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        if intent=="find_dl201_m8_q1_cs2":
            utter_dl201_m8_q1_cs2 = ("SELECT digital_tutor_case_summaries.case_summary_pdf, digital_tutor_chatbot.case_summary_2_reason FROM digital_tutor_case_summaries INNER JOIN digital_tutor_chatbot ON digital_tutor_chatbot.case_summary_2 = digital_tutor_case_summaries.intent AND digital_tutor_chatbot.intent = 'find_dl201_m8_q1'")  
            cursor.execute(utter_dl201_m8_q1_cs2)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_dl201_m8_q1_cs3":
            utter_dl201_m8_q1_cs3 = ("SELECT digital_tutor_case_summaries.case_summary_pdf, digital_tutor_chatbot.case_summary_3_reason FROM digital_tutor_case_summaries INNER JOIN digital_tutor_chatbot ON digital_tutor_chatbot.case_summary_3 = digital_tutor_case_summaries.intent AND digital_tutor_chatbot.intent = 'find_dl201_m8_q1'")  
            cursor.execute(utter_dl201_m8_q1_cs3)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindDL201m8Q1SR(Action):

    def name(self) -> Text:
        return "action_find_dl201_m8_q1_sr"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        if intent=="find_dl201_m8_q1_sr2":
            utter_dl201_m8_q1_sr2 = ("SELECT digital_tutor_readings.reading_link, digital_tutor_chatbot.suggested_reading_2_reason FROM digital_tutor_readings INNER JOIN digital_tutor_chatbot ON digital_tutor_chatbot.suggested_reading_2 = digital_tutor_readings.intent AND digital_tutor_chatbot.intent = 'find_dl201_m8_q1'")  
            cursor.execute(utter_dl201_m8_q1_sr2)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_dl201_m8_q1_sr3":
            utter_dl201_m8_q1_sr3 = ("SELECT digital_tutor_readings.reading_link, digital_tutor_chatbot.suggested_reading_3_reason FROM digital_tutor_readings INNER JOIN digital_tutor_chatbot ON digital_tutor_chatbot.suggested_reading_3 = digital_tutor_readings.intent AND digital_tutor_chatbot.intent = 'find_dl201_m8_q1'")  
            cursor.execute(utter_dl201_m8_q1_sr3)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindMoreInfoButtonsCS2SR2(Action):

    def name(self) -> Text:
        return "action_find_moreinfo_buttons_cs2sr2"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:
        
        find_casesummary_moreinfo = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_casesummary_moreinfo'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_casesummary_moreinfo) 
        find_casesummary_moreinfo = cursor.fetchone()
            
        find_casesummary_add = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_casesummary_add'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_casesummary_add) 
        find_casesummary_add = cursor.fetchone()
            
        find_reading_add = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_reading_add'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_reading_add) 
        find_reading_add = cursor.fetchone()
            
        find_inthe_classroom = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_inthe_classroom'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_inthe_classroom) 
        find_inthe_classroom = cursor.fetchone()
            
        utter_find_moreinfo_buttons = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_find_moreinfo_buttons'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_moreinfo_buttons) 
        utter_find_moreinfo_buttons = cursor.fetchone()    

        find_rollback = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_casesummary_moreinfo, "payload": "/find_casesummary_moreinfo"},{"title": find_casesummary_add, "payload": "/find_dl201_m8_q1_cs2"},
                    {"title": find_reading_add, "payload": "/find_dl201_m8_q1_sr2"},{"title": find_inthe_classroom, "payload": "/find_inthe_classroom"},
                    {"title": find_rollback, "payload": "/back"}]
            
        dispatcher.utter_message(str(utter_find_moreinfo_buttons).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindMoreInfoButtonsCS3SR2(Action):

    def name(self) -> Text:
        return "action_find_moreinfo_buttons_cs3sr2"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:
        
        find_casesummary_moreinfo = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_casesummary_moreinfo'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_casesummary_moreinfo) 
        find_casesummary_moreinfo = cursor.fetchone()
            
        find_casesummary_add = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_casesummary_add'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_casesummary_add) 
        find_casesummary_add = cursor.fetchone()
            
        find_reading_add = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_reading_add'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_reading_add) 
        find_reading_add = cursor.fetchone()
            
        find_inthe_classroom = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_inthe_classroom'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_inthe_classroom) 
        find_inthe_classroom = cursor.fetchone()
            
        utter_find_moreinfo_buttons = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_find_moreinfo_buttons'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_moreinfo_buttons) 
        utter_find_moreinfo_buttons = cursor.fetchone()    

        find_rollback = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_casesummary_moreinfo, "payload": "/find_casesummary_moreinfo"},{"title": find_casesummary_add, "payload": "/find_dl201_m8_q1_cs3"},
                    {"title": find_reading_add, "payload": "/find_dl201_m8_q1_sr2"},{"title": find_inthe_classroom, "payload": "/find_inthe_classroom"},
                    {"title": find_rollback, "payload": "/back"}]
            
        dispatcher.utter_message(str(utter_find_moreinfo_buttons).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindMoreInfoButtonsSR2(Action):

    def name(self) -> Text:
        return "action_find_moreinfo_buttons_sr2"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        find_casesummary_moreinfo = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_casesummary_moreinfo'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_casesummary_moreinfo) 
        find_casesummary_moreinfo = cursor.fetchone()

        find_reading_add = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_reading_add'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_reading_add) 
        find_reading_add = cursor.fetchone()
            
        find_inthe_classroom = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_inthe_classroom'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_inthe_classroom) 
        find_inthe_classroom = cursor.fetchone()
            
        utter_find_moreinfo_buttons = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_find_moreinfo_buttons'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_moreinfo_buttons) 
        utter_find_moreinfo_buttons = cursor.fetchone()    

        find_rollback = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_casesummary_moreinfo, "payload": "/find_casesummary_moreinfo"},{"title": find_reading_add, "payload": "/find_dl201_m8_q1_sr2"},
                   {"title": find_inthe_classroom, "payload": "/find_inthe_classroom"},
                    {"title": find_rollback, "payload": "/back"}]
            
        dispatcher.utter_message(str(utter_find_moreinfo_buttons).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []      

class ActionFindMoreInfoButtonsSR3MI(Action):

    def name(self) -> Text:
        return "action_find_moreinfo_buttons_sr3_mi"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        find_casesummary_moreinfo = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_casesummary_moreinfo'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_casesummary_moreinfo) 
        find_casesummary_moreinfo = cursor.fetchone()

        find_reading_add = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_reading_add'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_reading_add) 
        find_reading_add = cursor.fetchone()
            
        find_inthe_classroom = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_inthe_classroom'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_inthe_classroom) 
        find_inthe_classroom = cursor.fetchone()
            
        utter_find_moreinfo_buttons = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_find_moreinfo_buttons'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_moreinfo_buttons) 
        utter_find_moreinfo_buttons = cursor.fetchone()    

        find_rollback = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_casesummary_moreinfo, "payload": "/find_casesummary_moreinfo"},{"title": find_reading_add, "payload": "/find_dl201_m8_q1_sr3"},
                   {"title": find_inthe_classroom, "payload": "/find_inthe_classroom"},
                    {"title": find_rollback, "payload": "/back"}]
            
        dispatcher.utter_message(str(utter_find_moreinfo_buttons).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return [] 

class ActionFindMoreInfoButtonsSR3(Action):

    def name(self) -> Text:
        return "action_find_moreinfo_buttons_sr3"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:
            
        find_reading_add = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_reading_add'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_reading_add) 
        find_reading_add = cursor.fetchone()
            
        find_inthe_classroom = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_inthe_classroom'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_inthe_classroom) 
        find_inthe_classroom = cursor.fetchone()
            
        utter_find_moreinfo_buttons = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_find_moreinfo_buttons'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_moreinfo_buttons) 
        utter_find_moreinfo_buttons = cursor.fetchone()    

        find_rollback = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_reading_add, "payload": "/find_dl201_m8_q1_sr3"},{"title": find_inthe_classroom, "payload": "/find_inthe_classroom"},
                    {"title": find_rollback, "payload": "/back"}]
            
        dispatcher.utter_message(str(utter_find_moreinfo_buttons).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []      

class ActionFindMoreInfoButtonsNoCSSR1(Action):

    def name(self) -> Text:
        return "action_find_moreinfo_buttons_nocssr_1"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:
        
        find_inthe_classroom = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_inthe_classroom'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_inthe_classroom) 
        find_inthe_classroom = cursor.fetchone()
            
        utter_find_moreinfo_buttons = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_find_moreinfo_buttons'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_moreinfo_buttons) 
        utter_find_moreinfo_buttons = cursor.fetchone()    

        find_rollback = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_inthe_classroom, "payload": "/find_inthe_classroom"},
                    {"title": find_rollback, "payload": "/back"}]
            
        dispatcher.utter_message(str(utter_find_moreinfo_buttons).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []      

class ActionFindMoreInfoButtonsCS2SR3(Action):

    def name(self) -> Text:
        return "action_find_moreinfo_buttons_cs2sr3"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:
            
        find_casesummary_add = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_casesummary_add'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_casesummary_add) 
        find_casesummary_add = cursor.fetchone()
            
        find_reading_add = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_reading_add'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_reading_add) 
        find_reading_add = cursor.fetchone()
            
        find_inthe_classroom = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_inthe_classroom'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_inthe_classroom) 
        find_inthe_classroom = cursor.fetchone()
            
        utter_find_moreinfo_buttons = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_find_moreinfo_buttons'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_moreinfo_buttons) 
        utter_find_moreinfo_buttons = cursor.fetchone()    

        find_rollback = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_casesummary_add, "payload": "/find_dl201_m8_q1_cs2"},{"title": find_reading_add, "payload": "/find_dl201_m8_q1_sr3"},
                   {"title": find_inthe_classroom, "payload": "/find_inthe_classroom"},
                    {"title": find_rollback, "payload": "/back"}]
            
        dispatcher.utter_message(str(utter_find_moreinfo_buttons).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []                    

class ActionFindMoreInfoButtonsCS3SR3MI(Action):

    def name(self) -> Text:
        return "action_find_moreinfo_buttons_cs3sr3_mi"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        find_casesummary_moreinfo = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_casesummary_moreinfo'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_casesummary_moreinfo) 
        find_casesummary_moreinfo = cursor.fetchone()

        find_casesummary_add = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_casesummary_add'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_casesummary_add) 
        find_casesummary_add = cursor.fetchone()
            
        find_reading_add = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_reading_add'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_reading_add) 
        find_reading_add = cursor.fetchone()
            
        find_inthe_classroom = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_inthe_classroom'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_inthe_classroom) 
        find_inthe_classroom = cursor.fetchone()
            
        utter_find_moreinfo_buttons = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_find_moreinfo_buttons'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_moreinfo_buttons) 
        utter_find_moreinfo_buttons = cursor.fetchone()    

        find_rollback = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_casesummary_moreinfo, "payload": "/find_casesummary_moreinfo"},{"title": find_casesummary_add, "payload": "/find_dl201_m8_q1_cs3"},
                   {"title": find_reading_add, "payload": "/find_dl201_m8_q1_sr3"},{"title": find_inthe_classroom, "payload": "/find_inthe_classroom"},
                    {"title": find_rollback, "payload": "/back"}]
            
        dispatcher.utter_message(str(utter_find_moreinfo_buttons).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []  

class ActionFindMoreInfoButtonsCS3SR3(Action):

    def name(self) -> Text:
        return "action_find_moreinfo_buttons_cs3sr3"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        find_casesummary_add = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_casesummary_add'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_casesummary_add) 
        find_casesummary_add = cursor.fetchone()
            
        find_reading_add = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_reading_add'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_reading_add) 
        find_reading_add = cursor.fetchone()
            
        find_inthe_classroom = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_inthe_classroom'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_inthe_classroom) 
        find_inthe_classroom = cursor.fetchone()
            
        utter_find_moreinfo_buttons = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_find_moreinfo_buttons'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_moreinfo_buttons) 
        utter_find_moreinfo_buttons = cursor.fetchone()    

        find_rollback = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_casesummary_add, "payload": "/find_dl201_m8_q1_cs3"},{"title": find_reading_add, "payload": "/find_dl201_m8_q1_sr3"},
                   {"title": find_inthe_classroom, "payload": "/find_inthe_classroom"},
                    {"title": find_rollback, "payload": "/back"}]
            
        dispatcher.utter_message(str(utter_find_moreinfo_buttons).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindMoreInfoButtonsCS2(Action):

    def name(self) -> Text:
        return "action_find_moreinfo_buttons_cs2"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:
            
        find_casesummary_add = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_casesummary_add'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_casesummary_add) 
        find_casesummary_add = cursor.fetchone()
            
        find_inthe_classroom = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_inthe_classroom'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_inthe_classroom) 
        find_inthe_classroom = cursor.fetchone()
            
        utter_find_moreinfo_buttons = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_find_moreinfo_buttons'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_moreinfo_buttons) 
        utter_find_moreinfo_buttons = cursor.fetchone()    

        find_rollback = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_casesummary_add, "payload": "/find_dl201_m8_q1_cs2"},{"title": find_inthe_classroom, "payload": "/find_inthe_classroom"},
                    {"title": find_rollback, "payload": "/back"}]
            
        dispatcher.utter_message(str(utter_find_moreinfo_buttons).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []  

class ActionFindMoreInfoButtonsCS3MI(Action):

    def name(self) -> Text:
        return "action_find_moreinfo_buttons_cs3_mi"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        find_casesummary_moreinfo = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_casesummary_moreinfo'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_casesummary_moreinfo) 
        find_casesummary_moreinfo = cursor.fetchone()
             
        find_casesummary_add = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_casesummary_add'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_casesummary_add) 
        find_casesummary_add = cursor.fetchone()
            
        find_inthe_classroom = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_inthe_classroom'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_inthe_classroom) 
        find_inthe_classroom = cursor.fetchone()
            
        utter_find_moreinfo_buttons = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_find_moreinfo_buttons'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_moreinfo_buttons) 
        utter_find_moreinfo_buttons = cursor.fetchone()    

        find_rollback = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_casesummary_moreinfo, "payload": "/find_casesummary_moreinfo"},{"title": find_casesummary_add, "payload": "/find_dl201_m8_q1_cs3"}, 
                   {"title": find_inthe_classroom, "payload": "/find_inthe_classroom"},
                    {"title": find_rollback, "payload": "/back"}]
            
        dispatcher.utter_message(str(utter_find_moreinfo_buttons).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []  

class ActionFindMoreInfoButtonsCS3(Action):

    def name(self) -> Text:
        return "action_find_moreinfo_buttons_cs3"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        find_casesummary_add = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_casesummary_add'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_casesummary_add) 
        find_casesummary_add = cursor.fetchone()
            
        find_inthe_classroom = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_inthe_classroom'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_inthe_classroom) 
        find_inthe_classroom = cursor.fetchone()
            
        utter_find_moreinfo_buttons = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_find_moreinfo_buttons'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_moreinfo_buttons) 
        utter_find_moreinfo_buttons = cursor.fetchone()    

        find_rollback = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_casesummary_add, "payload": "/find_dl201_m8_q1_cs3"}, {"title": find_inthe_classroom, "payload": "/find_inthe_classroom"},
                    {"title": find_rollback, "payload": "/back"}]
            
        dispatcher.utter_message(str(utter_find_moreinfo_buttons).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []                     

class ActionFindMoreInfoButtonsNoCSSR2(Action):

    def name(self) -> Text:
        return "action_find_moreinfo_buttons_nocssr_2"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:
        
        find_casesummary_moreinfo = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_casesummary_moreinfo'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_casesummary_moreinfo) 
        find_casesummary_moreinfo = cursor.fetchone()
        
        find_inthe_classroom = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_inthe_classroom'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_inthe_classroom) 
        find_inthe_classroom = cursor.fetchone()
            
        utter_find_moreinfo_buttons = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_find_moreinfo_buttons'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_moreinfo_buttons) 
        utter_find_moreinfo_buttons = cursor.fetchone()    

        find_rollback = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_casesummary_moreinfo, "payload": "/find_casesummary_moreinfo"},{"title": find_inthe_classroom, "payload": "/find_inthe_classroom"},
                    {"title": find_rollback, "payload": "/back"}]
            
        dispatcher.utter_message(str(utter_find_moreinfo_buttons).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return [] 