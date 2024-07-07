import random
from faker import Faker
import plotly.graph_objects as go
import streamlit as st

# Initialize Faker for generating random names
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
        "Name": fake.name(),  # Random player name
        "Position": random.choice(positions),
        "Nationality": fake.country(),  # Random nationality
        "Age": random.randint(18, 40),
        "Goals": random.randint(0, 10),
        "Assists": random.randint(0, 10),
        "Passing Accuracy (%)": round(random.uniform(50, 95), 2),
        "Tackles Won": random.randint(0, 10),
        "Expected Goals": round(random.uniform(0, 1), 2),
        "Expected Assists": round(random.uniform(0, 1), 2),
        "Key Passes": random.randint(0, 10),
        "Key Tackles": random.randint(0, 10),
        "Shots": random.randint(0, 10),
        "Successful Dribbles": random.randint(0, 10),
        "Clean Sheets": random.randint(0, 10),  # New attribute: Clean Sheets
        "Goals Conceded": random.randint(0, 10),  # New attribute: Goals Conceded
        "Possession": round(random.uniform(40, 70), 2),  # New attribute: Possession
        "Chances Conceded": random.randint(10, 30),  # New attribute: Chances Conceded
        "Chances Created": random.randint(20, 60),  # New attribute: Chances Created
    }
    return player

# Function to generate a random manager
def generate_random_manager():
    manager = {
        "Name": fake.name(),  # Random manager name
        "Nationality": fake.country(),  # Random nationality
        "Age": random.randint(30, 60),
    }
    return manager

# Function to generate a random football team
def generate_random_team():
    team = {
        "Team Name": fake.company(),  # Random team name
        "Players": [generate_random_player() for _ in range(11)],
        "Manager": generate_random_manager(),
    }
    return team

# Generate 10 random football teams
random_teams = [generate_random_team() for _ in range(10)]

# Streamlit app with custom styling
st.set_page_config(
    page_title="Scout One ZM by UC.Labs",
    page_icon="⚽️",
    layout="wide",
)

# Custom CSS for background color, fonts, and interactive elements
st.markdown(
    """
    <style>
    body {
        background-color: #ffffff; /* White background */
        color: #4caf50; /* Green text */
    }
    .stApp {
        background-color: #7f6d5e; /* Brown container background */
        padding: 2rem;
        border-radius: 10px;
    }
    .stButton, .stSelectbox {
        background-color: #4caf50; /* Green buttons */
        color: white;
        border-radius: 5px;
    }
    .stButton:hover, .stSelectbox:hover {
        background-color: #45a049; /* Darker green on hover */
    }
    .stSelectbox:focus {
        background-color: #4caf50; /* Green on focus */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and sidebar
st.title("Scout One ZM by UC.Labs")

# Sidebar menu to choose reports
report_choice = st.sidebar.radio("Choose Report:", ("TEAM PROFILES", "PLAYER REPORTS", "PLAYER COMPARISON", "PERFORMANCE PREDICTION"))

# Function to generate and display a radar chart
def generate_radar_chart(player):
    attributes = list(player.keys())[3:13]  # Extract performance attributes
    values = [player[attr] for attr in attributes]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=attributes,
        fill='toself',
        name=player['Name']
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]  # Set the range of the radar chart (adjust as needed)
            ),
        ),
        showlegend=True,
        title=f"Performance Radar Chart for {player['Name']}",
    )

    st.plotly_chart(fig)

# Function to generate and display a mini player text report
def generate_mini_report(player1, player2):
    position1 = player1["Position"]
    position2 = player2["Position"]
    
    if position1 == "Goalkeeper":
        strengths1 = ["Excellent reflexes", "Good shot-stopper"]
        weaknesses1 = ["Limited outfield skills"]
    elif position1 == "Defensive Midfielder":
        strengths1 = ["Strong defensive abilities", "Good passing"]
        weaknesses1 = ["Limited goal-scoring"]
    elif position1 == "Attacking Midfielder":
        strengths1 = ["Creative playmaking", "Good vision"]
        weaknesses1 = ["Limited defensive skills"]
    elif position1 == "Winger":
        strengths1 = ["Pace and dribbling", "Crossing ability"]
        weaknesses1 = ["Limited defensive skills"]
    elif position1 == "Striker":
        strengths1 = ["Excellent goal-scoring abilities"]
        weaknesses1 = ["Limited defensive skills"]
    else:
        strengths1 = []
        weaknesses1 = []
    
    if position2 == "Goalkeeper":
        strengths2 = ["Excellent reflexes", "Good shot-stopper"]
        weaknesses2 = ["Limited outfield skills"]
    elif position2 == "Defensive Midfielder":
        strengths2 = ["Strong defensive abilities", "Good passing"]
        weaknesses2 = ["Limited goal-scoring"]
    elif position2 == "Attacking Midfielder":
        strengths2 = ["Creative playmaking", "Good vision"]
        weaknesses2 = ["Limited defensive skills"]
    elif position2 == "Winger":
        strengths2 = ["Pace and dribbling", "Crossing ability"]
        weaknesses2 = ["Limited defensive skills"]
    elif position2 == "Striker":
        strengths2 = ["Excellent goal-scoring abilities"]
        weaknesses2 = ["Limited defensive skills"]
    else:
        strengths2 = []
        weaknesses2 = []
    
    st.subheader(f"Player Comparison: {player1['Name']} ({player1['Position']}) vs {player2['Name']} ({player2['Position']})")
    st.write("**STRENGTHS - PLAYER 1:**")
    for strength in strengths1:
        st.write(f"- {strength}")
    st.write("**WEAKNESSES - PLAYER 1:**")
    for weakness in weaknesses1:
        st.write(f"- {weakness}")
    
    st.write("**STRENGTHS - PLAYER 2:**")
    for strength in strengths2:
        st.write(f"- {strength}")
    st.write("**WEAKNESSES - PLAYER 2:**")
    for weakness in weaknesses2:
        st.write(f"- {weakness}")

# Function to generate and display a text team report
def generate_team_report(team):
    st.subheader(f"Here is the Team Report for {team['Team Name']}")
    st.write(f"**HEAD COACH:** {team['Manager']['Name']}")
    st.write("**STARTING XI:**")
    for i, player in enumerate(team["Players"], start=1):
        st.write(f"{i}. {player['Name']} ({player['Position']})")

# Function to generate and display the player performance prediction graph
def generate_player_performance_prediction(selected_team_pp, selected_player_pp):
    # Placeholder prediction logic (random data)
    predicted_ratings = [random.uniform(1, 9) for _ in selected_team_pp["Players"]]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=[player["Age"] for player in selected_team_pp["Players"]],
        y=predicted_ratings,
        mode='lines+markers',
        name="Predicted Performance"
    ))

    fig.update_layout(
        xaxis_title="Player Age",
        yaxis_title="Performance Rating (1-9)",
        title=f"Performance Prediction for {selected_player_pp['Name']}",
    )

    st.plotly_chart(fig)

if report_choice == "TEAM PROFILES":
    # Create a dropdown menu to select teams and managers
    selected_team_index = st.selectbox("Select a Team:", range(len(random_teams)))

    # Display selected team and manager details
    selected_team = random_teams[selected_team_index]
    st.write(f"**TEAM:** {selected_team['Team Name']}")
    st.write(f"**HEAD COACH:** {selected_team['Manager']['Name']}")

    # Display player list and abbreviated positions
    st.subheader("STARTING XI:")
    for i, player in enumerate(selected_team["Players"], start=1):
        st.write(f"{i}. {player['Name']} ({player['Position']})")

    # Generate and display mini team report
    generate_team_report(selected_team)

elif report_choice == "PLAYER REPORTS":
    # Create a dropdown menu to select teams and players
    selected_team_index = st.selectbox("Select a Team:", range(len(random_teams)))
    selected_team = random_teams[selected_team_index]

    selected_player_index = st.selectbox("Select a Player:", range(11))
    selected_player = selected_team["Players"][selected_player_index]

    # Generate and display radar chart for the selected player
    generate_radar_chart(selected_player)

    # Generate and display mini player text report
    generate_mini_report(selected_player, selected_player)

elif report_choice == "PLAYER COMPARISON":
    # Create a dropdown menu to select teams and players
    selected_team_index_1 = st.selectbox("Select Team 1:", range(len(random_teams)))
    selected_team_index_2 = st.selectbox("Select Team 2:", range(len(random_teams)))

    # Ensure that teams have players in the same position
    team1_positions = [player['Position'] for player in random_teams[selected_team_index_1]["Players"]]
    team2_positions = [player['Position'] for player in random_teams[selected_team_index_2]["Players"]]
    common_positions = list(set(team1_positions) & set(team2_positions))

    if not common_positions:
        st.warning("Selected teams do not have players in the same position for comparison.")
    else:
        selected_position = st.selectbox("Select Position:", common_positions)

        # Filter players from both teams based on the selected position
        team1_players = [player for player in random_teams[selected_team_index_1]["Players"] if player['Position'] == selected_position]
        team2_players = [player for player in random_teams[selected_team_index_2]["Players"] if player['Position'] == selected_position]

        # Generate and display radar chart for player 1
        st.subheader(f"Performance Radar Chart for {team1_players[0]['Name']} (Team 1)")
        generate_radar_chart(team1_players[0])

        # Generate and display radar chart for player 2
        st.subheader(f"Performance Radar Chart for {team2_players[0]['Name']} (Team 2)")
        generate_radar_chart(team2_players[0])

        # Generate and display mini player comparison report
        generate_mini_report(team1_players[0], team2_players[0])

elif report_choice == "PERFORMANCE PREDICTION":
    st.subheader("PLAYER PERFORMANCE PREDICTION")

    # Create a dropdown menu to select teams and players
    selected_team_index_pp = st.selectbox("Select a Team:", range(len(random_teams)))
    selected_team_pp = random_teams[selected_team_index_pp]

    selected_player_index_pp = st.selectbox("Select a Player:", range(11))
    selected_player_pp = selected_team_pp["Players"][selected_player_index_pp]

    # Generate and display the player performance prediction graph
    generate_player_performance_prediction(selected_team_pp, selected_player_pp)
