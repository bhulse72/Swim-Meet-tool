#!/usr/bin/env python3

import sys

# this is the basic dictionary structure for storing times 
class team_times(dict):
    def __init__(self):
        # Initialize a fixed list of events with default times
        self.events = {
            "200 Medley Relay": [0,0,0],
            "200 Freestyle": [0,0,0],
            "200 IM": [0,0,0],
            "50 Freestyle": [0,0,0],
            "100 Butterfly": [0,0,0],
            "100 Freestyle": [0,0,0],
            "500 Freestyle": [0,0,0],
            "200 Free Relay": [0,0,0],
            "100 Backstroke": [0,0,0],
            "100 Breaststroke": [0,0,0],
            "400 Free Relay": [0,0,0]
        }


# this function takes the home scores dictionary and the away scores dictionary and returns the total scores for each team
# for individual events: 1st = 6o, 2nd = 4p, 3rd = 3p, 4th = 2p, 5th = 1p, 6th = 0p
# for relays: 1st = 8p, 2nd = 4p, 3rd = 2p, 4th = 0p
def calculate_score(home_times: team_times, away_times: team_times) -> tuple[int, int]:
    pass

# this function takes user input to populate the home and away scores dictionaries
def get_input(home_times: team_times, away_times: team_times): 
    print("")
    pass

def main():
    # Your main code here
    print("Hello, World!")

if __name__ == "__main__":
    main()