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
###################                       INTRO                      ################### 
########################################################################################

class ActionFindGreet1(Action):

    def name(self) -> Text:
        return "action_find_greet_1"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        if intent=="greet":
            utter_greet_1 = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_greet_1'")  
            cursor.execute(utter_greet_1)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindGreet2(Action):

    def name(self) -> Text:
        return "action_find_greet_2"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        cursor = connection.cursor(buffered=True)

        find_askquestion_cc = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_askquestion_cc'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_askquestion_cc) 
        find_askquestion_cc = cursor.fetchone()
        
        find_guidance_cc = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_guidance_cc'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_guidance_cc) 
        find_guidance_cc = cursor.fetchone()
            
        find_askquestion_cs = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_askquestion_cs'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_askquestion_cs) 
        find_askquestion_cs = cursor.fetchone()    

        buttons = []

        buttons = [{"title": find_askquestion_cc, "payload": "/find_askquestion_cc"},{"title": find_guidance_cc, "payload": "/find_guidance_cc"},
                    {"title": find_askquestion_cs, "payload": "/find_askquestion_cs"}]

        utter_greet_2 = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_greet_2'")  
        cursor.execute(utter_greet_2)       
        for (response) in cursor:
            dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

