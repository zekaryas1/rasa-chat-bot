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
###################      1.) ASK QUESTION: DL-201 COURSE CONTENT     ################### 
########################################################################################

class ActionUtterAskQuestionCC1(Action):

    def name(self) -> Text:
        return "action_utter_askquestion_cc_1"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        if intent=="find_askquestion_cc":
            utter_askquestion_cc_1 = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_askquestion_cc_1'")  
            cursor.execute(utter_askquestion_cc_1)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionUtterAskQuestionCC2(Action):

    def name(self) -> Text:
        return "action_utter_askquestion_cc_2"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        cursor = connection.cursor(buffered=True)

        utter_askquestion_cc_2 = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_askquestion_cc_2'")  
        cursor.execute(utter_askquestion_cc_2)       
        for (response) in cursor:
            dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []