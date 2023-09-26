# Import Streamlit library
import streamlit as st
import random
import pandas as pd
import numpy as np
from matplotlib import use  # Use the "Agg" backend (Agg is a non-interactive backend)
use.("Agg")
from matplotlib import pyplot as plt

# Enable Matplotlib support in Streamlit
st.set_option('deprecation.showPyplotGlobalUse', False)

# Define the possible player positions
positions = [
    "Goalkeeper",
    "Fullback",
    "Centreback",
    "Defensive Midfielder",
    "Attacking Midfielder",
    "Winger",
    "Striker",
]

# Function to generate random player data
def generate_random_player():
    player = {
        "Name": "Player " + str(random.randint(1, 100)),
        "Position": random.choice(positions),
        "Nationality": "Country " + str(random.randint(1, 50)),
        "Age": random.randint(18, 40),
        "Goals Scored": random.randint(0, 10),
        "Assists": random.randint(0, 10),
        "Passing Accuracy (%)": round(random.uniform(50, 95), 2),
        "Tackles Won": random.randint(0, 10),
        "Saves": random.randint(0, 10),
    }
    return player

# Streamlit app
st.set_page_config(
    page_title="Scout One ZM by UC.Labs",
    page_icon="⚽️",
    layout="wide",
)

# Custom CSS for background color
st.markdown(
    """
    <style>
    body {
        background-color: #7f6d5e;  /* Brown */
        color: #4caf50;  /* Green */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add Streamlit title with custom CSS
st.markdown(
    """
    <style>
    .css-15vbvxv {
        background-color: #4caf50 !important;  /* Green */
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Generate teams
if st.button("Generate Teams"):
    team_a = [generate_random_player() for _ in range(5)]
    team_b = [generate_random_player() for _ in range(5)]
    st.write(f"Team A")
    st.write(f"Team B")

# Generate and display scout report
if st.button("Generate Scout Report"):
    team_to_scout = st.selectbox("Select a team to scout", ["Team A", "Team B"])
    
    if team_to_scout == "Team A":
        selected_team = team_a
    else:
        selected_team = team_b
    
    st.markdown(f"## Scout Report for {team_to_scout}", unsafe_allow_html=True)
    
    for player in selected_team:
        st.header(f"Player: {player['Name']} ({player['Position']})")
        st.write(f"Nationality: {player['Nationality']}")
        st.write(f"Age: {player['Age']} years")
        st.write(f"Goals Scored: {player['Goals Scored']}")
        st.write(f"Assists: {player['Assists']}")
        st.write(f"Passing Accuracy: {player['Passing Accuracy (%)']}%")
        st.write(f"Tackles Won: {player['Tackles Won']}")
        st.write(f"Saves (for Goalkeepers): {player['Saves']}")
