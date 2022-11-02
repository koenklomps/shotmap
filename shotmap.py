# -*- coding: utf-8 -*-
"""
@author: koenk
"""
#%% imports

import pandas as pd
import numpy as np
import os

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.patheffects as path_effects
from matplotlib.font_manager import FontProperties

from mplsoccer import VerticalPitch

import socceraction
import socceraction.spadl as spadl

#%% import event data

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df_events = pd.read_csv('../data/whoscorederedivisie2122v2.csv')

#%% create shots df

df_shots = df_events[df_events['is_shot'] == True].copy()


#%% dessers shot map

df_missedshots = df_shots[(df_shots['player_id'] == 244805) & (df_shots['type'] != 'Goal')].copy()
df_goals = df_shots[(df_shots['player_id'] == 244805) & (df_shots['type'] == 'Goal')].copy()


pitch = VerticalPitch(
    pitch_type = "opta",
    half=True,
    line_color='#BD97A7',
    pitch_color='#765d6a',
    goal_type='box',
    goal_alpha=0.7
)

fig, ax = pitch.draw(figsize=(12, 10))
sc1 = pitch.scatter(df_missedshots['x'], df_missedshots['y'],
                   s=300,
                   c='None', 
                   edgecolors='#BD97A7', 
                   marker='o',
                   hatch=3*'x',
                   ax=ax
)

sc2 = pitch.scatter(df_goals['x'], df_goals['y'],
                   s=300,
                   c='#eeba0c',  
                   edgecolors='#383838', 
                   marker='o',
                   ax=ax
)

font = FontProperties()
font.set_family('Poppins')
font.set_name('Poppins')

txt1 = ax.text(x=98, y=55, s='Cyriel',
              size=50, color=pitch.line_color,
              fontproperties=font, weight='ultralight',
              va='bottom', ha='left')

txt2 = ax.text(x=98, y=51, s='Dessers',
              size=50, color=pitch.line_color,
              fontproperties=font, weight='bold',
              va='bottom', ha='left')

#plt.savefig("./dessers.png",bbox_inches='tight', pad_inches=0.0, dpi=300)

#%% haller shot map

df_missedshots = df_shots[(df_shots['player_id'] == 236544) & (df_shots['type'] != 'Goal')].copy()
df_goals = df_shots[(df_shots['player_id'] == 236544) & (df_shots['type'] == 'Goal')].copy()

pitch = VerticalPitch(
    pitch_type = "opta",
    half=True,
    line_color='#1e5c42',
    pitch_color='#548872',
    goal_type='box',
    goal_alpha=0.7
)

fig, ax = pitch.draw(figsize=(12, 10))
sc1 = pitch.scatter(df_missedshots['x'], df_missedshots['y'],
                   s=300,
                   c='None', 
                   edgecolors='#1e5c42',
                   marker='o',
                   hatch=3*'x',
                   ax=ax
)

sc2 = pitch.scatter(df_goals['x'], df_goals['y'],
                   s=300,
                   c='#725488',  
                   edgecolors='#383838',  
                   marker='o',
                   ax=ax
)

font = FontProperties()
font.set_family('Poppins')
font.set_name('Poppins')

txt1 = ax.text(x=98, y=55, s='Sébastien',
              size=50, color=pitch.line_color,
              fontproperties=font, weight='ultralight',
              va='bottom', ha='left')

txt2 = ax.text(x=98, y=51, s='Haller',
              size=50, color=pitch.line_color,
              fontproperties=font, weight='bold',
              va='bottom', ha='left')

#plt.savefig("./haller.png",bbox_inches='tight', pad_inches=0.0, dpi=300)

#%% zahavi shot map

df_missedshots = df_shots[(df_shots['player_id'] == 44096) & (df_shots['type'] != 'Goal')].copy()
df_goals = df_shots[(df_shots['player_id'] == 44096) & (df_shots['type'] == 'Goal')].copy()

pitch = VerticalPitch(
    pitch_type = "opta",
    half=True,
    line_color='#489FB5',
    pitch_color='#16697A',
    goal_type='box',
    goal_alpha=0.7
)

fig, ax = pitch.draw(figsize=(12, 10))
sc1 = pitch.scatter(df_missedshots['x'], df_missedshots['y'],
                   s=300,
                   c='None', 
                   edgecolors='#489FB5',
                   marker='o',
                   hatch=3*'x',
                   ax=ax
)

sc2 = pitch.scatter(df_goals['x'], df_goals['y'],
                   s=300,
                   c='#DADABE',  
                   edgecolors='#383838',  
                   marker='o',
                   ax=ax
)

font = FontProperties()
font.set_family('Poppins')
font.set_name('Poppins')

txt1 = ax.text(x=98, y=55, s='Eran',
              size=50, color=pitch.line_color,
              fontproperties=font, weight='ultralight',
              va='bottom', ha='left')

txt2 = ax.text(x=98, y=51, s='Zahavi',
              size=50, color=pitch.line_color,
              fontproperties=font, weight='bold',
              va='bottom', ha='left')

#plt.savefig("./zahavi.png",bbox_inches='tight', pad_inches=0.0, dpi=300)



