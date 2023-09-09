import json
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from django.db import transaction
from ...models import Team

#def load_data_from_json(json_file_path):
    #with open(json_file_path, 'r') as f:
    #    data = json.load(f)
    

class Command(BaseCommand):
    team_data = [
            {'team_id' : 40, 'team_name' : 'Afghanistan', 'team_flag' : 'team_flags/afghanistan.png'},
            {'team_id' : 2, 'team_name' : 'Australia', 'team_flag' : 'team_flags/australia.png'},
            {'team_id' : 25, 'team_name' : 'Bangladesh', 'team_flag' : 'team_flags/bangladesh.png'},
            {'team_id' : 12, 'team_name' : 'Bermuda', 'team_flag' : 'team_flags/bermuda.png'},
            {'team_id' : 17, 'team_name' : 'Canada', 'team_flag' : 'team_flags/canada.png'},
            {'team_id' : 14, 'team_name' : 'East Africa', 'team_flag' : 'team_flags/east_africa.png'},
            {'team_id' : 1, 'team_name' : 'England', 'team_flag' : 'team_flags/england.png'},
            {'team_id' : 19, 'team_name' : 'Hong Kong', 'team_flag' : 'team_flags/hong_kong.png'},
            {'team_id' : 140, 'team_name' : 'ICC World XI', 'team_flag' : 'team_flags/icc_world_xi.png'},
            {'team_id' : 6, 'team_name' : 'India', 'team_flag' : 'team_flags/india.png'},
            {'team_id' : 29, 'team_name' : 'Ireland', 'team_flag' : 'team_flags/ireland.png'},
            {'team_id' : 4083, 'team_name' : 'Jersey', 'team_flag' : 'team_flags/jersey.png'},
            {'team_id' : 26, 'team_name' : 'Kenya', 'team_flag' : 'team_flags/kenya.png'},
            {'team_id' : 28, 'team_name' : 'Namibia', 'team_flag' : 'team_flags/namibia.png'},
            {'team_id' : 32, 'team_name' : 'Nepal', 'team_flag' : 'team_flags/nepal.png'},
            {'team_id' : 15, 'team_name' : 'Netherlands', 'team_flag' : 'team_flags/netherlands.png'},
            {'team_id' : 5, 'team_name' : 'New Zealand', 'team_flag' : 'team_flags/new_zealand.png'},
            {'team_id' : 37, 'team_name' : 'Oman', 'team_flag' : 'team_flags/oman.png'},
            {'team_id' : 7, 'team_name' : 'Pakistan', 'team_flag' : 'team_flags/pakistan.png'},
            {'team_id' : 20, 'team_name' : 'Papua New Guinea', 'team_flag' : 'team_flags/papua_new_guinea.png'},
            {'team_id' : 30, 'team_name' : 'Scotland', 'team_flag' : 'team_flags/scotland.png'},
            {'team_id' : 3, 'team_name' : 'South Africa', 'team_flag' : 'team_flags/south_africa.png'},
            {'team_id' : 8, 'team_name' : 'Sri Lanka', 'team_flag' : 'team_flags/sri_lanka.png'},
            {'team_id' : 27, 'team_name' : 'United Arab Emirates', 'team_flag' : 'team_flags/united_arab_emirates.png'},
            {'team_id' : 11, 'team_name' : 'United States of America', 'team_flag' : 'team_flags/united_states_of_america.png'},
            {'team_id' : 4, 'team_name' : 'West Indies', 'team_flag' : 'team_flags/west_indies.png'},
            {'team_id' : 9, 'team_name' : 'Zimbabwe', 'team_flag' : 'team_flags/zimbabwe.png'},
            {'team_id' : 20201, 'team_name' : 'Chennai Super Kings', 'team_flag' : 'team_flags/chennai_super_kings.png'},
            {'team_id' : 20202, 'team_name' : 'Delhi Capitals', 'team_flag' : 'team_flags/delhi_capitals.png'},
            {'team_id' : 20203, 'team_name' : 'Gujarat Titans', 'team_flag' : 'team_flags/gujarat_titans.png'},
            {'team_id' : 20204, 'team_name' : 'Kolkata Knight Riders', 'team_flag' : 'team_flags/kolkata_knight_riders.png'},
            {'team_id' : 20206, 'team_name' : 'Lucknow Super Giants', 'team_flag' : 'team_flags/lucknow_super_giants.png'},
            {'team_id' : 20207, 'team_name' : 'Mumbai Indians', 'team_flag' : 'team_flags/mumbai_indians.png'},
            {'team_id' : 20209, 'team_name' : 'Punjab Kings', 'team_flag' : 'team_flags/punjab_kings.png'},
            {'team_id' : 20210, 'team_name' : 'Rajasthan Royals', 'team_flag' : 'team_flags/rajasthan_royals.png'},
            {'team_id' : 20211, 'team_name' : 'Royal Challengers Bangalore', 'team_flag' : 'team_flags/royal_challengers_bangalore.png'},
            {'team_id' : 20212, 'team_name' : 'Sunrisers Hyderabad', 'team_flag' : 'team_flags/sunrisers_hyderabad.png'},
    ]

    def handle(self, *args, **options):
        for team_info in Command.team_data:
            team_id = team_info['team_id']
            team_name = team_info['team_name']
            team_flag = team_info['team_flag']
            team = Team(team_id, team_name, team_flag)
            team.save()
