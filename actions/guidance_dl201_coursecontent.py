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
###################        2.) GUIDANCE: DL-201 COURSE CONTENT       ################### 
########################################################################################

class ActionFindUtterGuidanceCC(Action):

    def name(self) -> Text:
        return "action_utter_guidance_cc"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        if intent=="find_guidance_cc":

            find_dl201_m1_title = ("SELECT topic FROM digital_tutor_buttons WHERE intent = 'find_dl201_m1_title'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_dl201_m1_title) 
            find_dl201_m1_title = cursor.fetchone()
            
            find_dl201_m2_title = ("SELECT topic FROM digital_tutor_buttons WHERE intent = 'find_dl201_m2_title'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_dl201_m2_title) 
            find_dl201_m2_title = cursor.fetchone()
                
            find_dl201_m3_title = ("SELECT topic FROM digital_tutor_buttons WHERE intent = 'find_dl201_m3_title'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_dl201_m3_title) 
            find_dl201_m3_title = cursor.fetchone()  

            find_dl201_m4_title = ("SELECT topic FROM digital_tutor_buttons WHERE intent = 'find_dl201_m4_title'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_dl201_m4_title) 
            find_dl201_m4_title = cursor.fetchone()
            
            find_dl201_m5_title = ("SELECT topic FROM digital_tutor_buttons WHERE intent = 'find_dl201_m5_title'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_dl201_m5_title) 
            find_dl201_m5_title = cursor.fetchone()
                
            find_dl201_m6_title = ("SELECT topic FROM digital_tutor_buttons WHERE intent = 'find_dl201_m6_title'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_dl201_m6_title) 
            find_dl201_m6_title = cursor.fetchone()  

            find_dl201_m7_title = ("SELECT topic FROM digital_tutor_buttons WHERE intent = 'find_dl201_m7_title'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_dl201_m7_title) 
            find_dl201_m7_title = cursor.fetchone()
            
            find_dl201_m8_title = ("SELECT topic FROM digital_tutor_buttons WHERE intent = 'find_dl201_m8_title'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_dl201_m8_title) 
            find_dl201_m8_title = cursor.fetchone()
            
            find_dl201_m9_title = ("SELECT topic FROM digital_tutor_buttons WHERE intent = 'find_dl201_m9_title'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_dl201_m9_title) 
            find_dl201_m9_title = cursor.fetchone()
                
            find_dl201_m10_title = ("SELECT topic FROM digital_tutor_buttons WHERE intent = 'find_dl201_m10_title'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_dl201_m10_title) 
            find_dl201_m10_title = cursor.fetchone()    

            find_dl201_m11_title = ("SELECT topic FROM digital_tutor_buttons WHERE intent = 'find_dl201_m11_title'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_dl201_m11_title) 
            find_dl201_m11_title = cursor.fetchone()
            
            find_dl201_m12_title = ("SELECT topic FROM digital_tutor_buttons WHERE intent = 'find_dl201_m12_title'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_dl201_m12_title) 
            find_dl201_m12_title = cursor.fetchone()
                
            find_dl201_m13_title = ("SELECT topic FROM digital_tutor_buttons WHERE intent = 'find_dl201_m13_title'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_dl201_m13_title) 
            find_dl201_m13_title = cursor.fetchone()  

            buttons = []

            buttons = [{"title": find_dl201_m1_title, "payload": "/find_dl201_m1_disctopics"},{"title": find_dl201_m2_title, "payload": "/find_dl201_m2_disctopics"},
                        {"title": find_dl201_m3_title, "payload": "/find_dl201_m3_disctopics"},{"title": find_dl201_m4_title, "payload": "/find_dl201_m4_disctopics"},
                        {"title": find_dl201_m5_title, "payload": "/find_dl201_m5_disctopics"},{"title": find_dl201_m6_title, "payload": "/find_dl201_m6_disctopics"},
                        {"title": find_dl201_m7_title, "payload": "/find_dl201_m7_disctopics"},{"title": find_dl201_m8_title, "payload": "/find_dl201_m8_disctopics"},
                        {"title": find_dl201_m9_title, "payload": "/find_dl201_m9_disctopics"},{"title": find_dl201_m10_title, "payload": "/find_dl201_m10_disctopics"},
                        {"title": find_dl201_m11_title, "payload": "/find_dl201_m11_disctopics"},{"title": find_dl201_m12_title, "payload": "/find_dl201_m12_disctopics"},
                        {"title": find_dl201_m13_title, "payload": "/find_dl201_m13_disctopics"}]

            utter_guidance_cc_1 = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_guidance_cc_1'")  
            cursor.execute(utter_guidance_cc_1)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''), buttons=buttons) 

        return []

class ActionFindUtterGuidanceCCInfo(Action):

    def name(self) -> Text:
        return "action_utter_guidance_cc_info"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        if intent=="find_dl201_m1_disctopics":
            find_dl201_m1_disctopics = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_dl201_m1_disctopics'")
            cursor.execute(find_dl201_m1_disctopics)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

            find_dl201_m1_q1 = ("SELECT question FROM digital_tutor_chatbot WHERE intent = 'find_dl201_m1_q1'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_dl201_m1_q1) 
            find_dl201_m1_q1 = cursor.fetchone()  

            find_dl201_m1_q2 = ("SELECT question FROM digital_tutor_chatbot WHERE intent = 'find_dl201_m1_q2'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_dl201_m1_q2) 
            find_dl201_m1_q2 = cursor.fetchone()  
            
            find_dl201_m1_q3 = ("SELECT question FROM digital_tutor_chatbot WHERE intent = 'find_dl201_m1_q3'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_dl201_m1_q3) 
            find_dl201_m1_q3 = cursor.fetchone()            

            buttons = []

            buttons = [{"title": find_dl201_m1_q1, "payload": "/find_dl201_m1_q1"},{"title": find_dl201_m1_q2, "payload": "/find_dl201_m1_q2"},
                        {"title": find_dl201_m1_q3, "payload": "/find_dl201_m1_q3"}]

            utter_dl201_m1_sampleqs = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_dl201_m1_sampleqs'")
            cursor.execute(utter_dl201_m1_sampleqs)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)               

        elif intent=="find_dl201_m2_disctopics":
            find_dl201_m2_disctopics = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_dl201_m2_disctopics'")
            cursor.execute(find_dl201_m2_disctopics)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
            utter_dl201_m2_sampleqs = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_dl201_m2_sampleqs'")
            cursor.execute(utter_dl201_m2_sampleqs)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))   
                
        elif intent=="find_dl201_m3_disctopics":
            find_dl201_m3_disctopics = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_dl201_m3_disctopics'")
            cursor.execute(find_dl201_m3_disctopics)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
            utter_dl201_m3_sampleqs = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_dl201_m3_sampleqs'")
            cursor.execute(utter_dl201_m3_sampleqs)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))  

        elif intent=="find_dl201_m4_disctopics":
            find_dl201_m4_disctopics = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_dl201_m4_disctopics'")
            cursor.execute(find_dl201_m4_disctopics)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
            utter_dl201_m4_sampleqs = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_dl201_m4_sampleqs'")
            cursor.execute(utter_dl201_m4_sampleqs)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))   

        elif intent=="find_dl201_m5_disctopics":
            find_dl201_m5_disctopics = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_dl201_m5_disctopics'")
            cursor.execute(find_dl201_m5_disctopics)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
            utter_dl201_m5_sampleqs = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_dl201_m5_sampleqs'")
            cursor.execute(utter_dl201_m5_sampleqs)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))   

        elif intent=="find_dl201_m6_disctopics":
            find_dl201_m6_disctopics = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_dl201_m6_disctopics'")
            cursor.execute(find_dl201_m6_disctopics)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
            utter_dl201_m6_sampleqs = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_dl201_m6_sampleqs'")
            cursor.execute(utter_dl201_m6_sampleqs)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))   

        elif intent=="find_dl201_m7_disctopics":
            find_dl201_m7_disctopics = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_dl201_m7_disctopics'")
            cursor.execute(find_dl201_m7_disctopics)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
            utter_dl201_m7_sampleqs = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_dl201_m7_sampleqs'")
            cursor.execute(utter_dl201_m7_sampleqs)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))   

        elif intent=="find_dl201_m8_disctopics":
            find_dl201_m8_disctopics = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_dl201_m8_disctopics'")
            cursor.execute(find_dl201_m8_disctopics)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

            find_dl201_m8_q1 = ("SELECT question FROM digital_tutor_chatbot WHERE intent = 'find_dl201_m8_q1'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_dl201_m8_q1) 
            find_dl201_m8_q1 = cursor.fetchone()  

            find_dl201_m8_q2 = ("SELECT question FROM digital_tutor_chatbot WHERE intent = 'find_dl201_m8_q2'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_dl201_m8_q2) 
            find_dl201_m8_q2 = cursor.fetchone()  
            
            find_dl201_m8_q3 = ("SELECT question FROM digital_tutor_chatbot WHERE intent = 'find_dl201_m8_q3'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_dl201_m8_q3) 
            find_dl201_m8_q3 = cursor.fetchone()            

            buttons = []

            buttons = [{"title": find_dl201_m8_q1, "payload": "/find_dl201_m8_q1"},{"title": find_dl201_m8_q2, "payload": "/find_dl201_m8_q2"},
                        {"title": find_dl201_m8_q3, "payload": "/find_dl201_m8_q3"}]

            utter_dl201_m8_sampleqs = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_dl201_m8_sampleqs'")
            cursor.execute(utter_dl201_m8_sampleqs)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)   

        elif intent=="find_dl201_m9_disctopics":
            find_dl201_m9_disctopics = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_dl201_m9_disctopics'")
            cursor.execute(find_dl201_m9_disctopics)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
            utter_dl201_m9_sampleqs = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_dl201_m9_sampleqs'")
            cursor.execute(utter_dl201_m9_sampleqs)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))   

        elif intent=="find_dl201_m10_disctopics":
            find_dl201_m10_disctopics = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_dl201_m10_disctopics'")
            cursor.execute(find_dl201_m10_disctopics)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
            utter_dl201_m10_sampleqs = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_dl201_m10_sampleqs'")
            cursor.execute(utter_dl201_m10_sampleqs)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))   

        elif intent=="find_dl201_m11_disctopics":
            find_dl201_m11_disctopics = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_dl201_m11_disctopics'")
            cursor.execute(find_dl201_m11_disctopics)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
            utter_dl201_m11_sampleqs = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_dl201_m11_sampleqs'")
            cursor.execute(utter_dl201_m11_sampleqs)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))   

        elif intent=="find_dl201_m12_disctopics":
            find_dl201_m12_disctopics = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_dl201_m12_disctopics'")
            cursor.execute(find_dl201_m12_disctopics)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
            utter_dl201_m12_sampleqs = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_dl201_m12_sampleqs'")
            cursor.execute(utter_dl201_m12_sampleqs)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))   

        elif intent=="find_dl201_m13_disctopics":
            find_dl201_m13_disctopics = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_dl201_m13_disctopics'")
            cursor.execute(find_dl201_m13_disctopics)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
            utter_dl201_m13_sampleqs = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_dl201_m13_sampleqs'")
            cursor.execute(utter_dl201_m13_sampleqs)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))   

        return []