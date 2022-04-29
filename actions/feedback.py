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
###################                    FEEDBACK                      ################### 
########################################################################################

class ActionShareFeedbackRating(Action):

    def name(self) -> Text:
        return "action_share_feedback_rating"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the text
        if intent=="Feedback":

            share_rating_feedback = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'share_rating_feedback'")  
            cursor = connection.cursor(buffered=True)
            cursor.execute(share_rating_feedback) 
            share_rating_feedback = cursor.fetchone()      

            one_star_feedback = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'one_star_feedback'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(one_star_feedback) 
            one_star_feedback = cursor.fetchone()      

            two_star_feedback = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'two_star_feedback'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(two_star_feedback) 
            two_star_feedback = cursor.fetchone()      

            three_star_feedback = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'three_star_feedback'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(three_star_feedback) 
            three_star_feedback = cursor.fetchone()      

            four_star_feedback = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'four_star_feedback'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(four_star_feedback) 
            four_star_feedback = cursor.fetchone()      

            five_star_feedback = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'five_star_feedback'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(five_star_feedback) 
            five_star_feedback = cursor.fetchone()      

            buttons = []

            buttons = [{"title": five_star_feedback, "payload": "/five_star_feedback"},{"title": four_star_feedback, "payload": "/four_star_feedback"},
                    {"title": three_star_feedback, "payload": "/three_star_feedback"},{"title": two_star_feedback, "payload": "/two_star_feedback"},
                    {"title": one_star_feedback, "payload": "/one_star_feedback"}]
                    
            dispatcher.utter_message(str(share_rating_feedback).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)


        return []

class ActionShareFeedbackComment(Action):

    def name(self) -> Text:
        return "action_share_feedback_comment"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the text

        share_comment_feedback = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'share_comment_feedback'")  
        cursor = connection.cursor(buffered=True)
        cursor.execute(share_comment_feedback) 
        share_comment_feedback = cursor.fetchone()      

        share_comment_feedback_yes = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'share_comment_feedback_yes'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(share_comment_feedback_yes) 
        share_comment_feedback_yes = cursor.fetchone()           

        exit_feedback = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'exit_feedback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(exit_feedback) 
        exit_feedback = cursor.fetchone()  

        buttons = []

        buttons = [{"title": share_comment_feedback_yes, "payload": "/share_comment_feedback_yes"},{"title": exit_feedback, "payload": "/exit_feedback_with_rating"},]
                    
        dispatcher.utter_message(str(share_comment_feedback).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionShareFeedbackCommentResult(Action):

    def name(self) -> Text:
        return "action_share_feedback_comment_result"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the text
        if intent=="share_comment_feedback_yes":

            give_comment_feedback = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'give_comment_feedback'")  
            cursor = connection.cursor(buffered=True)
            cursor.execute(give_comment_feedback) 
            give_comment_feedback = cursor.fetchone()      
            dispatcher.utter_message(str(give_comment_feedback).strip('("",)').strip("'").replace('\',', ''))

        elif intent=="exit_feedback_with_rating":

            exit_feedback_with_rating = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'exit_feedback_with_rating'")  
            cursor = connection.cursor(buffered=True)
            cursor.execute(exit_feedback_with_rating) 
            exit_feedback_with_rating = cursor.fetchone()      
            dispatcher.utter_message(str(exit_feedback_with_rating).strip('("",)').strip("'").replace('\',', ''))        

            utter_greet_3 = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_greet_3'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(utter_greet_3) 
            utter_greet_3 = cursor.fetchone()        
            
            dispatcher.utter_message(str(utter_greet_3).strip('("",)').strip("'").replace('\',', ''))

        return []

class ValidateSurveyForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_survey_form"

    def validate_open_feedback(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:
        """Validate `open_feedback` value."""

        # If the name is super short, it might be wrong.
        print(f"Open Feedback given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 3:
            dispatcher.utter_message(text=f"That's a very short feedback. I'm assuming you mis-spelled. Please try again by leaving your feedback comment below.")
            return {"open_feedback": None}
        else:
            return {"open_feedback": slot_value}

class ActionSubmitFeedback(Action): 

    def name(self) -> Text: 
        return "action_submit_feedback"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:                                 
            
        FeedbackUpdate(tracker.get_slot("open_rating"),tracker.get_slot("open_feedback")) 
                                           
        return []

class ActionShareFeedbackFinal(Action):

    def name(self) -> Text:
        return "action_share_feedback_final"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        cursor = connection.cursor(buffered=True)

        exit_feedback_with_rating_comment = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'exit_feedback_with_rating_comment'")  
        cursor = connection.cursor(buffered=True)
        cursor.execute(exit_feedback_with_rating_comment) 
        exit_feedback_with_rating_comment = cursor.fetchone()      
        dispatcher.utter_message(str(exit_feedback_with_rating_comment).strip('("",)').strip("'").replace('\',', ''))      

        utter_greet_2 = ("SELECT utterance FROM digital_tutor_buttons WHERE intent = 'utter_greet_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_greet_2) 
        utter_greet_2 = cursor.fetchone()        
            
        dispatcher.utter_message(str(utter_greet_2).strip('("",)').strip("'").replace('\',', ''))

        return []