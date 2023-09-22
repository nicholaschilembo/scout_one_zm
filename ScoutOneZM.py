# Import Streamlit library
import streamlit as st

# Import other necessary libraries
import random
from faker import Faker
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Enable Matplotlib support in Streamlit
st.set_option('deprecation.showPyplotGlobalUse', False)

# Create a Faker instance for generating random data
fake = Faker()

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
        "Name": fake.name(),
        "Position": random.choice(positions),
        "Nationality": fake.country(),
        "Age": random.randint(18, 40),
        "Goals Scored": random.randint(0, 10),
        "Assists": random.randint(0, 10),
        "Passing Accuracy (%)": round(random.uniform(50, 95), 2),
        "Tackles Won": random.randint(0, 10),
        "Saves": random.randint(0, 10),
    }
    return player

# Function to generate random team data
def generate_random_team():
    team = {
        "Team Name": fake.unique.first_name(),
        "Manager": fake.name(),
    }
    return team

# Function to generate teams
def generate_teams():
    team_a = [generate_random_player() for _ in range(5)]
    team_b = [generate_random_player() for _ in range(5)]
    return team_a, team_b

# Function to create a radar pie chart for player stats
def create_player_radar_chart(player_stats):
    stats = list(player_stats.keys())
    values = list(player_stats.values())
    
    # Normalize values to be in the range [0, 1]
    values = [(value - min(values)) / (max(values) - min(values)) for value in values]
    
    angles = np.linspace(0, 2 * np.pi, len(stats), endpoint=False).tolist()
    angles += angles[:1]
    
    fig, ax = plt.subplots(subplot_kw={'polar': True}, figsize=(6, 6))
    ax.fill(angles, values, 'b', alpha=0.1)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(stats)
    
    return fig

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
    team_a, team_b = generate_teams()
    team_a_data = generate_random_team()
    team_b_data = generate_random_team()
    st.write(f"Team A: {team_a_data['Team Name']} (Manager: {team_a_data['Manager']})")
    st.write(f"Team B: {team_b_data['Team Name']} (Manager: {team_b_data['Manager']})")

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

        # Create radar pie chart for player stats
        radar_chart = create_player_radar_chart(player)
        st.pyplot(radar_chart)