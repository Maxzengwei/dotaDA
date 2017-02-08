from django.shortcuts import render
from django.http import HttpResponse
from .models import Match, Player
import json
import dota2api


if __name__ == "__main__":
    print("Start Dota Api")
    api = dota2api.Initialise("B279ECFCF25AF5B787A87DB0CCEB5BA5")
    hist = api.get_match_history(account_id=84331215)
#  match = api.get_match_details(match_id=2820318558)
    
    for x in (0,hist["num_results"]):
        match = hist["matches"][x]
        r = Match( match_id=match(match_id),match_seq_num=match(match_seq_num),start_time=match(start_time),lobby_type=match(lobby_type))
        r.save()
        print(match(match_id))