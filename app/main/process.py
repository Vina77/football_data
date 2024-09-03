import pandas as pd

def process_data(data):
    matches = data['matches']
    df = pd.DataFrame([{
        'home_team': match['homeTeam']['name'],
        'away_team': match['awayTeam']['name'],
        'home_score': match['score']['fullTime']['home'],
        'away_score': match['score']['fullTime']['away'],
    } for match in matches])
    return df