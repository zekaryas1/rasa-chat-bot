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
###################                OVERALL FUNCTIONALITY             ################### 
########################################################################################

class ActionResetAllSlots(Action):

    def name(self) -> Text:
        return "action_reset_all_slots"

    def run(self, dispatcher, tracker, domain):

        return [AllSlotsReset()]

class ActionFindGreetMenu(Action):

    def name(self) -> Text:
        return "action_find_greet_menu"

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

        find_greet_menu = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_greet_menu'")  
        cursor.execute(find_greet_menu)       
        for (response) in cursor:
            dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []