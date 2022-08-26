# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from rasa_sdk.types import DomainDict
from rasa_sdk import Tracker, FormValidationAction, Action

# class ValidateSimplePizzaForm(FormValidationAction):
#     def name(self) -> Text:
#         return "validate_location_form"

#     def validate_location(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:


#         dispatcher.utter_message(text=f"OK! You want to have a {slot_value} pizza.")
#         return []




class ActionWeather(Action):

    def name(self) -> Text:
        return "action_weather_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = tracker.get_slot("city")
        api_adress = 'http://api.openweathermap.org/data/2.5/weather?appid=d855415b94911ab4e59fea60d05db7b1&q='
        url = api_adress + city
        json_data = requests.get(url).json()

        format_weather = json_data['main']
        temp = int(format_weather['temp'] - 273)
        print(city, temp)
        dispatcher.utter_message(response="utter_weather", temp=temp)
        return []

class GetWeather(Action):

    def name(self) -> Text:
        return "weather_action"