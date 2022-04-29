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
###################       3.) ASK QUESTION: DL-201 CASE SUMMARY      ################### 
########################################################################################

class ActionUtterAskQuestionCS(Action):

    def name(self) -> Text:
        return "action_utter_askquestion_cs"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        if intent=="find_askquestion_cs":

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

            buttons = [{"title": find_dl201_m1_title, "payload": "/find_dl201_m1_cs"},{"title": find_dl201_m2_title, "payload": "/find_dl201_m2_cs"},
                        {"title": find_dl201_m3_title, "payload": "/find_dl201_m3_cs"},{"title": find_dl201_m4_title, "payload": "/find_dl201_m4_cs"},
                        {"title": find_dl201_m5_title, "payload": "/find_dl201_m5_cs"},{"title": find_dl201_m6_title, "payload": "/find_dl201_m6_cs"},
                        {"title": find_dl201_m7_title, "payload": "/find_dl201_m7_cs"},{"title": find_dl201_m8_title, "payload": "/find_dl201_m8_cs"},
                        {"title": find_dl201_m9_title, "payload": "/find_dl201_m9_cs"},{"title": find_dl201_m10_title, "payload": "/find_dl201_m10_cs"},
                        {"title": find_dl201_m11_title, "payload": "/find_dl201_m11_cs"},{"title": find_dl201_m12_title, "payload": "/find_dl201_m12_cs"},
                        {"title": find_dl201_m13_title, "payload": "/find_dl201_m13_cs"}]

            utter_askquestion_cs_1 = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_askquestion_cs_1'")  
            cursor.execute(utter_askquestion_cs_1)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionUtterAskQuestionCSInfo(Action):

    def name(self) -> Text:
        return "action_utter_askquestion_cs_info"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        if intent=="find_dl201_m1_cs":

            find_m1_c1 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m1_c1'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m1_c1) 
            find_m1_c1 = cursor.fetchone()  

            find_m1_c2 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m1_c2'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m1_c2) 
            find_m1_c2 = cursor.fetchone()  
            
            find_m1_c3 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m1_c3'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m1_c3) 
            find_m1_c3 = cursor.fetchone()         

            buttons = []

            buttons = [{"title": find_m1_c1, "payload": "/find_m1_c1"},{"title": find_m1_c2, "payload": "/find_m1_c2"},
                        {"title": find_m1_c3, "payload": "/find_m1_c3"}]

            utter_dl201_m1_cs_list = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_dl201_m1_cs_list'")
            cursor.execute(utter_dl201_m1_cs_list)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)        

        elif intent=="find_dl201_m2_cs":

            find_m2_c1 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m2_c1'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m2_c1) 
            find_m2_c1 = cursor.fetchone()  

            find_m2_c2 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m2_c2'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m2_c2) 
            find_m2_c2 = cursor.fetchone()  

            find_m2_c3 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m2_c3'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m2_c3) 
            find_m2_c3 = cursor.fetchone()  

            find_m2_c4 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m2_c4'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m2_c4) 
            find_m2_c4 = cursor.fetchone()  
            
            find_m2_c5 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m2_c5'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m2_c5) 
            find_m2_c5 = cursor.fetchone()         

            buttons = []

            buttons = [{"title": find_m2_c1, "payload": "/find_m2_c1"},{"title": find_m2_c2, "payload": "/find_m2_c2"},
                        {"title": find_m2_c3, "payload": "/find_m2_c3"},{"title": find_m2_c4, "payload": "/find_m2_c4"},
                        {"title": find_m2_c5, "payload": "/find_m2_c5"}]

            utter_dl201_m2_cs_list = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_dl201_m2_cs_list'")
            cursor.execute(utter_dl201_m2_cs_list)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        elif intent=="find_dl201_m3_cs":

            find_m3_c1 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m3_c1'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m3_c1) 
            find_m3_c1 = cursor.fetchone()  

            find_m3_c2 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m3_c2'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m3_c2) 
            find_m3_c2 = cursor.fetchone()  

            find_m3_c3 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m3_c3'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m3_c3) 
            find_m3_c3 = cursor.fetchone()  

            find_m3_c4 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m3_c4'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m3_c4) 
            find_m3_c4 = cursor.fetchone()  
            
            find_m3_c5 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m3_c5'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m3_c5) 
            find_m3_c5 = cursor.fetchone()         

            buttons = []

            buttons = [{"title": find_m3_c1, "payload": "/find_m3_c1"},{"title": find_m3_c2, "payload": "/find_m3_c2"},
                        {"title": find_m3_c3, "payload": "/find_m3_c3"},{"title": find_m3_c4, "payload": "/find_m3_c4"},
                        {"title": find_m3_c5, "payload": "/find_m3_c5"}]

            utter_dl201_m3_cs_list = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_dl201_m3_cs_list'")
            cursor.execute(utter_dl201_m3_cs_list)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        elif intent=="find_dl201_m4_cs":

            find_m4_c1 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m4_c1'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m4_c1) 
            find_m4_c1 = cursor.fetchone()  

            find_m4_c2 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m4_c2'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m4_c2) 
            find_m4_c2 = cursor.fetchone()  

            find_m4_c3 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m4_c3'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m4_c3) 
            find_m4_c3 = cursor.fetchone()  

            find_m4_c4 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m4_c4'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m4_c4) 
            find_m4_c4 = cursor.fetchone()  
            
            find_m4_c5 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m4_c5'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m4_c5) 
            find_m4_c5 = cursor.fetchone()         

            find_m4_c6 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m4_c6'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m4_c6) 
            find_m4_c6 = cursor.fetchone()  

            buttons = []

            buttons = [{"title": find_m4_c1, "payload": "/find_m4_c1"},{"title": find_m4_c2, "payload": "/find_m4_c2"},
                        {"title": find_m4_c3, "payload": "/find_m4_c3"},{"title": find_m4_c4, "payload": "/find_m4_c4"},
                        {"title": find_m4_c5, "payload": "/find_m4_c5"},{"title": find_m4_c6, "payload": "/find_m4_c6"}]

            utter_dl201_m4_cs_list = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_dl201_m4_cs_list'")
            cursor.execute(utter_dl201_m4_cs_list)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        elif intent=="find_dl201_m5_cs":

            find_m5_c1 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m5_c1'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m5_c1) 
            find_m5_c1 = cursor.fetchone()  

            find_m5_c2 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m5_c2'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m5_c2) 
            find_m5_c2 = cursor.fetchone()  

            find_m5_c3 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m5_c3'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m5_c3) 
            find_m5_c3 = cursor.fetchone()  

            find_m5_c4 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m5_c4'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m5_c4) 
            find_m5_c4 = cursor.fetchone()  
            
            find_m5_c5 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m5_c5'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m5_c5) 
            find_m5_c5 = cursor.fetchone()         

            buttons = []

            buttons = [{"title": find_m5_c1, "payload": "/find_m5_c1"},{"title": find_m5_c2, "payload": "/find_m5_c2"},
                        {"title": find_m5_c3, "payload": "/find_m5_c3"},{"title": find_m5_c4, "payload": "/find_m5_c4"},
                        {"title": find_m5_c5, "payload": "/find_m5_c5"}]

            utter_dl201_m5_cs_list = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_dl201_m5_cs_list'")
            cursor.execute(utter_dl201_m5_cs_list)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        elif intent=="find_dl201_m6_cs":

            find_m6_c1 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m6_c1'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m6_c1) 
            find_m6_c1 = cursor.fetchone()  

            find_m6_c2 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m6_c2'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m6_c2) 
            find_m6_c2 = cursor.fetchone()  

            find_m6_c3 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m6_c3'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m6_c3) 
            find_m6_c3 = cursor.fetchone()      

            buttons = []

            buttons = [{"title": find_m6_c1, "payload": "/find_m6_c1"},{"title": find_m6_c2, "payload": "/find_m6_c2"},
                        {"title": find_m6_c3, "payload": "/find_m6_c3"}]

            utter_dl201_m6_cs_list = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_dl201_m6_cs_list'")
            cursor.execute(utter_dl201_m6_cs_list)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        elif intent=="find_dl201_m7_cs":

            find_m7_c1 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m7_c1'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m7_c1) 
            find_m7_c1 = cursor.fetchone()  

            find_m7_c2 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m7_c2'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m7_c2) 
            find_m7_c2 = cursor.fetchone()  

            find_m7_c3 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m7_c3'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m7_c3) 
            find_m7_c3 = cursor.fetchone()      

            find_m7_c4 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m7_c4'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m7_c4) 
            find_m7_c4 = cursor.fetchone()    

            buttons = []

            buttons = [{"title": find_m7_c1, "payload": "/find_m7_c1"},{"title": find_m7_c2, "payload": "/find_m7_c2"},
                        {"title": find_m7_c3, "payload": "/find_m7_c3"},{"title": find_m7_c4, "payload": "/find_m7_c4"}]

            utter_dl201_m7_cs_list = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_dl201_m7_cs_list'")
            cursor.execute(utter_dl201_m7_cs_list)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        elif intent=="find_dl201_m8_cs":

            find_m8_c1 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m8_c1'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m8_c1) 
            find_m8_c1 = cursor.fetchone()  

            find_m8_c2 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m8_c2'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m8_c2) 
            find_m8_c2 = cursor.fetchone()  

            find_m8_c3 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m8_c3'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m8_c3) 
            find_m8_c3 = cursor.fetchone()      

            find_m8_c4 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m8_c4'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m8_c4) 
            find_m8_c4 = cursor.fetchone()    

            find_m8_c5 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m8_c5'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m8_c5) 
            find_m8_c5 = cursor.fetchone()    

            buttons = []

            buttons = [{"title": find_m8_c1, "payload": "/find_m8_c1"},{"title": find_m8_c2, "payload": "/find_m8_c2"},
                        {"title": find_m8_c3, "payload": "/find_m8_c3"},{"title": find_m8_c4, "payload": "/find_m8_c4"},
                        {"title": find_m8_c5, "payload": "/find_m8_c5"}]

            utter_dl201_m8_cs_list = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_dl201_m8_cs_list'")
            cursor.execute(utter_dl201_m8_cs_list)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        elif intent=="find_dl201_m9_cs":

            find_m9_c1 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m9_c1'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m9_c1) 
            find_m9_c1 = cursor.fetchone()  

            find_m9_c2 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m9_c2'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m9_c2) 
            find_m9_c2 = cursor.fetchone()  

            find_m9_c3 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m9_c3'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m9_c3) 
            find_m9_c3 = cursor.fetchone()      

            buttons = []

            buttons = [{"title": find_m9_c1, "payload": "/find_m9_c1"},{"title": find_m9_c2, "payload": "/find_m9_c2"},
                        {"title": find_m9_c3, "payload": "/find_m9_c3"}]

            utter_dl201_m9_cs_list = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_dl201_m9_cs_list'")
            cursor.execute(utter_dl201_m9_cs_list)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        elif intent=="find_dl201_m10_cs":

            find_m10_c1 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m10_c1'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m10_c1) 
            find_m10_c1 = cursor.fetchone()  

            find_m10_c2 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m10_c2'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m10_c2) 
            find_m10_c2 = cursor.fetchone()  

            find_m10_c3 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m10_c3'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m10_c3) 
            find_m10_c3 = cursor.fetchone()      

            find_m10_c4 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m10_c4'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m10_c4) 
            find_m10_c4 = cursor.fetchone()  

            find_m10_c5 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m10_c5'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m10_c5) 
            find_m10_c5 = cursor.fetchone()   

            find_m10_c6 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m10_c6'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m10_c6) 
            find_m10_c6 = cursor.fetchone()  

            find_m10_c7 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m10_c7'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m10_c7) 
            find_m10_c7 = cursor.fetchone()   

            buttons = []

            buttons = [{"title": find_m10_c1, "payload": "/find_m10_c1"},{"title": find_m10_c2, "payload": "/find_m10_c2"},
                        {"title": find_m10_c3, "payload": "/find_m10_c3"},{"title": find_m10_c4, "payload": "/find_m10_c4"},
                        {"title": find_m10_c5, "payload": "/find_m10_c5"},{"title": find_m10_c6, "payload": "/find_m10_c6"},
                        {"title": find_m10_c7, "payload": "/find_m10_c7"}]

            utter_dl201_m10_cs_list = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_dl201_m10_cs_list'")
            cursor.execute(utter_dl201_m10_cs_list)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        elif intent=="find_dl201_m11_cs":

            find_m11_c1 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m11_c1'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m11_c1) 
            find_m11_c1 = cursor.fetchone()  

            find_m11_c2 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m11_c2'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m11_c2) 
            find_m11_c2 = cursor.fetchone()   

            buttons = []

            buttons = [{"title": find_m11_c1, "payload": "/find_m11_c1"},{"title": find_m11_c2, "payload": "/find_m11_c2"}]

            utter_dl201_m11_cs_list = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_dl201_m11_cs_list'")
            cursor.execute(utter_dl201_m11_cs_list)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        elif intent=="find_dl201_m12_cs":

            find_m12_c1 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m12_c1'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m12_c1) 
            find_m12_c1 = cursor.fetchone()  

            buttons = []

            buttons = [{"title": find_m12_c1, "payload": "/find_m12_c1"}]

            utter_dl201_m12_cs_list = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_dl201_m12_cs_list'")
            cursor.execute(utter_dl201_m12_cs_list)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        elif intent=="find_dl201_m13_cs":

            find_m13_c1 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m13_c1'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m13_c1) 
            find_m13_c1 = cursor.fetchone()  

            find_m13_c2 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m13_c2'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m13_c2) 
            find_m13_c2 = cursor.fetchone()  

            find_m13_c3 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m13_c3'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m13_c3) 
            find_m13_c3 = cursor.fetchone()      

            find_m13_c4 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m13_c4'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m13_c4) 
            find_m13_c4 = cursor.fetchone()  

            find_m13_c5 = ("SELECT title_of_case FROM digital_tutor_case_summaries WHERE intent = 'find_m13_c5'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_m13_c5) 
            find_m13_c5 = cursor.fetchone()   

            buttons = []

            buttons = [{"title": find_m13_c1, "payload": "/find_m13_c1"},{"title": find_m13_c2, "payload": "/find_m13_c2"},
                        {"title": find_m13_c3, "payload": "/find_m13_c3"},{"title": find_m13_c4, "payload": "/find_m13_c4"},
                        {"title": find_m13_c5, "payload": "/find_m13_c5"}]

            utter_dl201_m13_cs_list = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_dl201_m13_cs_list'")
            cursor.execute(utter_dl201_m13_cs_list)       
            for response in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionUtterDL201m1csSampleQs(Action):

    def name(self) -> Text:
        return "action_utter_dl201_m1_cs_sampleqs"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        if intent=="find_m1_c1":

            find_dl201_m1_c1_q1 = ("SELECT question FROM digital_tutor_case_summaries_qas WHERE intent = 'find_dl201_m1_c1_q1'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_dl201_m1_c1_q1) 
            find_dl201_m1_c1_q1 = cursor.fetchone()

            find_dl201_m1_c1_q2 = ("SELECT question FROM digital_tutor_case_summaries_qas WHERE intent = 'find_dl201_m1_c1_q2'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_dl201_m1_c1_q2) 
            find_dl201_m1_c1_q2 = cursor.fetchone()

            find_dl201_m1_c1_q3 = ("SELECT question FROM digital_tutor_case_summaries_qas WHERE intent = 'find_dl201_m1_c1_q3'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_dl201_m1_c1_q3) 
            find_dl201_m1_c1_q3 = cursor.fetchone()

            buttons = []

            buttons = [{"title": find_dl201_m1_c1_q1, "payload": "/find_dl201_m1_c1_q1"},{"title": find_dl201_m1_c1_q2, "payload": "/find_dl201_m1_c1_q2"},
                        {"title": find_dl201_m1_c1_q3, "payload": "/find_dl201_m1_c1_q3"}]

            utter_dl201_cs_sampleqs = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_dl201_cs_sampleqs'")  
            cursor.execute(utter_dl201_cs_sampleqs)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionUtterDL201m1c1SampleQsAnswer(Action):

    def name(self) -> Text:
        return "action_utter_dl201_m1_c1_sampleqs_answer"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        if intent=="find_dl201_m1_c1_q1":

            find_dl201_m1_c1_q1 = ("SELECT answer FROM digital_tutor_case_summaries_qas WHERE intent = 'find_dl201_m1_c1_q1'")  
            cursor.execute(find_dl201_m1_c1_q1)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

            find_anotherquestion_cs = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_anotherquestion_cs'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_anotherquestion_cs) 
            find_anotherquestion_cs = cursor.fetchone()

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

            buttons = [{"title": find_anotherquestion_cs, "payload": "/find_m1_c1"},{"title": find_askquestion_cc, "payload": "/find_askquestion_cc"},
                        {"title": find_guidance_cc, "payload": "/find_guidance_cc"},{"title": find_askquestion_cs, "payload": "/find_askquestion_cs"}]

            find_proceed_button = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_proceed_button'")  
            cursor.execute(find_proceed_button)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        elif intent=="find_dl201_m1_c1_q2":

            find_dl201_m1_c1_q2 = ("SELECT answer FROM digital_tutor_case_summaries_qas WHERE intent = 'find_dl201_m1_c1_q2'")  
            cursor.execute(find_dl201_m1_c1_q2)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

            find_anotherquestion_cs = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_anotherquestion_cs'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_anotherquestion_cs) 
            find_anotherquestion_cs = cursor.fetchone()

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

            buttons = [{"title": find_anotherquestion_cs, "payload": "/find_m1_c1"},{"title": find_askquestion_cc, "payload": "/find_askquestion_cc"},
                        {"title": find_guidance_cc, "payload": "/find_guidance_cc"},{"title": find_askquestion_cs, "payload": "/find_askquestion_cs"}]

            find_proceed_button = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_proceed_button'")  
            cursor.execute(find_proceed_button)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        elif intent=="find_dl201_m1_c1_q3":

            find_dl201_m1_c1_q3 = ("SELECT answer FROM digital_tutor_case_summaries_qas WHERE intent = 'find_dl201_m1_c1_q3'")  
            cursor.execute(find_dl201_m1_c1_q3)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

            find_anotherquestion_cs = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_anotherquestion_cs'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_anotherquestion_cs) 
            find_anotherquestion_cs = cursor.fetchone()

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

            buttons = [{"title": find_anotherquestion_cs, "payload": "/find_m1_c1"},{"title": find_askquestion_cc, "payload": "/find_askquestion_cc"},
                        {"title": find_guidance_cc, "payload": "/find_guidance_cc"},{"title": find_askquestion_cs, "payload": "/find_askquestion_cs"}]

            find_proceed_button = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_proceed_button'")  
            cursor.execute(find_proceed_button)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        else:

            nlu_fallback_case = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'nlu_fallback_case'")  
            cursor.execute(nlu_fallback_case)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

            find_anotherquestion_cs = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_anotherquestion_cs'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_anotherquestion_cs) 
            find_anotherquestion_cs = cursor.fetchone()

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

            buttons = [{"title": find_anotherquestion_cs, "payload": "/find_m1_c1"},{"title": find_askquestion_cc, "payload": "/find_askquestion_cc"},
                        {"title": find_guidance_cc, "payload": "/find_guidance_cc"},{"title": find_askquestion_cs, "payload": "/find_askquestion_cs"}]

            find_proceed_button = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'find_proceed_button'")  
            cursor.execute(find_proceed_button)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []
