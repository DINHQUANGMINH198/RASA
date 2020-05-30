from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.events import UserUtteranceReverted
from rasa_core_sdk.events import AllSlotsReset
from rasa_core_sdk.events import Restarted

import requests
import json
import feedparser


# Ham lay ket qua so xo va tra ve. Ten ham la action_get_lottery
class action_get_lottery(Action):
    def name(self):
        # Doan nay khai bao giong het ten ham ben tren la okie
        return 'action_get_lottery'

    def run(self, dispatcher, tracker, domain):
        # Khai bao dia chi luu tru ket qua so xo. O day lam vi du nen minh lay ket qua SX Mien Bac
        url = 'https://xskt.com.vn/rss-feed/mien-bac-xsmb.rss'
        # Tien hanh lay thong tin tu URL
        feed_cnt = feedparser.parse(url)
        # Lay ket qua so xo moi nhat
        first_node = feed_cnt['entries']
        # Lay thong tin ve ngay va chi tiet cac giai
        return_msg = first_node[0]['title'] + "\n" + first_node[0]['description']
        # Tra ve cho nguoi dung
        dispatcher.utter_message(return_msg)
        return []


class api_give_name(Action):
    def name(self):
        return 'api_give_name'

    def run(self, dispatcher, tracker, domain):
        customer_name = str(tracker.get_slot("cust_name"))
        customer_sex = str(tracker.get_slot("cust_sex"))
        # in ra thông tin các entities cust_sex và cust_sex mới nhất ra màn hình
        print("last cust_name:", customer_name, ", last cust_sex:", customer_sex)

        hovaten = customer_sex + " " + customer_name
        last_message = "- from api: Kính chào "  + hovaten + ". ABC Shop có thể giúp gì được " + hovaten + " ạ?"
        dispatcher.utter_message(last_message)
        return []
