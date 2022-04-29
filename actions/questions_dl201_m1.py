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
###################                QUESTIONS - M1                    ################### 
########################################################################################

class ActionFindDL201m1Q9(Action):

    def name(self) -> Text:
        return "action_find_dl201_m1_q9"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        self.dispatcher = dispatcher
        self.dictionary = {
            "find_dl201_m1_q9": self.find_dl201_m1_q9,
            "find_dl201_m1_q10": self.find_dl201_m1_q10
        }
        blockOfCode = self.dictionary.get(intent, lambda : print("the intent doesn't exist in the dictionary"))
        blockOfCode()
    
    def find_dl201_m1_q10(self):
        ## write the select statement for question 10 here
        pass
    
    def find_dl201_m1_q9(self):
        utter_dl201_q1 = ("SELECT answer FROM digital_tutor_chatbot WHERE intent = 'find_dl201_m1_q9'")
        cursor = connection.cursor(buffered=True)  
        cursor.execute(utter_dl201_q1)       
        for response in cursor:
            self.dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        ## CASE SUMMARIES TITLES ##

        dl201_m1_q9_cs1_title = ("SELECT digital_tutor_case_summaries.title_of_case FROM digital_tutor_case_summaries INNER JOIN digital_tutor_chatbot ON digital_tutor_chatbot.case_summary_1 = digital_tutor_case_summaries.intent AND digital_tutor_chatbot.intent = 'find_dl201_m1_q9'") 
        cursor = connection.cursor(buffered=True)
        cursor.execute(dl201_m1_q9_cs1_title) 
        dl201_m1_q9_cs1_title = cursor.fetchone()

        dl201_m1_q9_cs2_title = ("SELECT digital_tutor_case_summaries.title_of_case FROM digital_tutor_case_summaries INNER JOIN digital_tutor_chatbot ON digital_tutor_chatbot.case_summary_2 = digital_tutor_case_summaries.intent AND digital_tutor_chatbot.intent = 'find_dl201_m1_q9'") 
        cursor = connection.cursor(buffered=True)
        cursor.execute(dl201_m1_q9_cs2_title) 
        dl201_m1_q9_cs2_title = cursor.fetchone()

        dl201_m1_q9_cs3_title = ("SELECT digital_tutor_case_summaries.title_of_case FROM digital_tutor_case_summaries INNER JOIN digital_tutor_chatbot ON digital_tutor_chatbot.case_summary_3 = digital_tutor_case_summaries.intent AND digital_tutor_chatbot.intent = 'find_dl201_m1_q9'") 
        cursor = connection.cursor(buffered=True)
        cursor.execute(dl201_m1_q9_cs3_title) 
        dl201_m1_q9_cs3_title = cursor.fetchone()

        ## CASE SUMMARIES REASONS ##

        dl201_m1_q9_cs1 = ("SELECT digital_tutor_chatbot.case_summary_1_reason FROM digital_tutor_chatbot WHERE digital_tutor_chatbot.intent = 'find_dl201_m1_q9'") 
        cursor = connection.cursor(buffered=True)
        cursor.execute(dl201_m1_q9_cs1) 
        dl201_m1_q9_cs1 = cursor.fetchone()

        dl201_m1_q9_cs2 = ("SELECT digital_tutor_chatbot.case_summary_2_reason FROM digital_tutor_chatbot WHERE digital_tutor_chatbot.intent = 'find_dl201_m1_q9'") 
        cursor = connection.cursor(buffered=True)
        cursor.execute(dl201_m1_q9_cs2) 
        dl201_m1_q9_cs2 = cursor.fetchone()

        dl201_m1_q9_cs3 = ("SELECT digital_tutor_chatbot.case_summary_3_reason FROM digital_tutor_chatbot WHERE digital_tutor_chatbot.intent = 'find_dl201_m1_q9'") 
        cursor = connection.cursor(buffered=True)
        cursor.execute(dl201_m1_q9_cs3) 
        dl201_m1_q9_cs3 = cursor.fetchone()

        data = [ { "title": dl201_m1_q9_cs1_title, "description": dl201_m1_q9_cs1}, 
                     { "title": dl201_m1_q9_cs2_title, "description": dl201_m1_q9_cs2}, 
                     { "title": dl201_m1_q9_cs3_title, "description": dl201_m1_q9_cs3}]

        message = { "payload": "collapsible", "data": data }

        self.dispatcher.utter_message(text="Please find below relevant IP Case Summaries that are linked to the question you have asked, and a reason as to why they are associated.", json_message=message)

            ## SUGGESTED READINGS TITLES ##

        dl201_m1_q9_sr1_title = ("SELECT digital_tutor_readings.reading_title FROM digital_tutor_readings INNER JOIN digital_tutor_chatbot ON digital_tutor_chatbot.suggested_reading_1 = digital_tutor_readings.intent AND digital_tutor_chatbot.intent = 'find_dl201_m1_q9'") 
        cursor = connection.cursor(buffered=True)
        cursor.execute(dl201_m1_q9_sr1_title) 
        dl201_m1_q9_sr1_title = cursor.fetchone()

        dl201_m1_q9_sr2_title = ("SELECT digital_tutor_readings.reading_title FROM digital_tutor_readings INNER JOIN digital_tutor_chatbot ON digital_tutor_chatbot.suggested_reading_2 = digital_tutor_readings.intent AND digital_tutor_chatbot.intent = 'find_dl201_m1_q9'") 
        cursor = connection.cursor(buffered=True)
        cursor.execute(dl201_m1_q9_sr2_title) 
        dl201_m1_q9_sr2_title = cursor.fetchone()

        dl201_m1_q9_sr3_title = ("SELECT digital_tutor_readings.reading_title FROM digital_tutor_readings INNER JOIN digital_tutor_chatbot ON digital_tutor_chatbot.suggested_reading_3 = digital_tutor_readings.intent AND digital_tutor_chatbot.intent = 'find_dl201_m1_q9'") 
        cursor = connection.cursor(buffered=True)
        cursor.execute(dl201_m1_q9_sr3_title) 
        dl201_m1_q9_sr3_title = cursor.fetchone()

        ## SUGGESTED READINGS REASONS ##

        dl201_m1_q9_sr1 = ("SELECT digital_tutor_chatbot.suggested_reading_1_reason FROM digital_tutor_chatbot WHERE digital_tutor_chatbot.intent = 'find_dl201_m1_q9'") 
        cursor = connection.cursor(buffered=True)
        cursor.execute(dl201_m1_q9_sr1) 
        dl201_m1_q9_sr1 = cursor.fetchone()

        dl201_m1_q9_sr2 = ("SELECT digital_tutor_chatbot.suggested_reading_2_reason FROM digital_tutor_chatbot WHERE digital_tutor_chatbot.intent = 'find_dl201_m1_q9'") 
        cursor = connection.cursor(buffered=True)
        cursor.execute(dl201_m1_q9_sr2) 
        dl201_m1_q9_sr2 = cursor.fetchone()

        dl201_m1_q9_sr3 = ("SELECT digital_tutor_chatbot.suggested_reading_3_reason FROM digital_tutor_chatbot WHERE digital_tutor_chatbot.intent = 'find_dl201_m1_q9'") 
        cursor = connection.cursor(buffered=True)
        cursor.execute(dl201_m1_q9_sr3) 
        dl201_m1_q9_sr3 = cursor.fetchone()

        data = [ { "title": dl201_m1_q9_sr1_title, "description": dl201_m1_q9_sr1}, 
                     { "title": dl201_m1_q9_sr2_title, "description": dl201_m1_q9_sr2}, 
                     { "title": dl201_m1_q9_sr3_title, "description": dl201_m1_q9_sr3}]

        message = { "payload": "collapsible", "data": data }

        self.dispatcher.utter_message(text="Please find below suggested readings that are linked to the question you have asked, and a reason as to why they are associated.", json_message=message)

        return []