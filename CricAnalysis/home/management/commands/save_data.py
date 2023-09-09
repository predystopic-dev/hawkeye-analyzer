import json
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from django.db import transaction
from ...models import Team
from bs4 import BeautifulSoup as bs
import requests
import os

#match_id = '13326385178016'
#url = f'https://polls.iplt20.com/widget/welcome/get_data?path=https://post-feeds.s3.ap-south-1.amazonaws.com/Delivery_1_1_1_{match_id}.json'
url = 'https://www.iplt20.com/match/2023/865'
#url = 'https://www.bcci.tv/events/100/australia-tour-of-india-2023/match/741/2nd-test'
def load_data_from_json(json_file_path):
    with open(json_file_path, 'r') as f:
        data = json.load(f)


class Command(BaseCommand):
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    obj = soup.find('object')['data']
    match_id = obj.split('&')[1].split('=')[1]
    
    
    def handle(self, *args, **options):    
        inning = 1
        over = 1
        delivery = 1
        data = []

        while (delivery <= 6):
            url = f'https://polls.iplt20.com/widget/welcome/get_data?path=https://post-feeds.s3.ap-south-1.amazonaws.com/Delivery_{inning}_{over}_{delivery}_{Command.match_id}.json'
            response = requests.get(url)
            if response.text.strip().lower() != "null": 
                
                delivery += 1
                
            if (delivery == 7):
                delivery = 1
                over += 1
            if (response.text.strip().lower() == "null" and inning == 4):
                break
            if (response.text.strip().lower() == "null" and inning != 4):
                inning += 1
                over = 1
                delivery = 1
