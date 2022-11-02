# -*- coding: utf-8 -*-
"""
@author: koenk
"""

#%% imports
import soccerdata as sd
import pandas as pd
import numpy as np
import json
import os

import matplotlib.pyplot as plt

import socceraction
import socceraction.spadl as spadl

from mplsoccer import Pitch, VerticalPitch
#%% 
if __name__ == '__main__':
    ws = sd.WhoScored(leagues="FRA-Ligue 1", seasons="2021-2022", proxy='tor')
    
    


#%%   

while True:
    try:
        df_events = ws.read_events(match_id=range(1558308, 1558574))
        break
    except ConnectionError:
        pass


#%%

df_events.to_csv(r'C:\Users\koenk\Google Drive\Projects\data\whoscoredpremierleague2122.csv')