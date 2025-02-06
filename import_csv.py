import numpy as np
import pandas as pd

# Load the CSV file using the Windows file path (using raw string notation):
file_path = r"C:\Users\sethw\New folder\players_stats_by_season_full_details.csv"
df = pd.read_csv(file_path)

# Selecting relevant columns for calculations
df_selected = df[['Season', 'Player', 'GP', 'MIN', 'FGM', 'FGA', '3PM', '3PA', 'FTM', 'FTA', 'PTS', 'BLK', 'STL']]

# Convert only the numeric columns to numbers, coercing errors to NaN for safety
numeric_cols = ['GP', 'MIN', 'FGM', 'FGA', '3PM', '3PA', 'FTM', 'FTA', 'PTS', 'BLK', 'STL']
df_selected[numeric_cols] = df_selected[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Remove rows with missing essential numeric data
df_selected = df_selected.dropna(subset=numeric_cols)

# Field Goal Accuracy (FG%)
df_selected['FG%'] = np.where(df_selected['FGA'] > 0, df_selected['FGM'] / df_selected['FGA'], 0)

# Three-Point Accuracy (3P%)
df_selected['3P%'] = np.where(df_selected['3PA'] > 0, df_selected['3PM'] / df_selected['3PA'], 0)

# Free Throw Accuracy (FT%)
df_selected['FT%'] = np.where(df_selected['FTA'] > 0, df_selected['FTM'] / df_selected['FTA'], 0)

# Average Points Per Minute
df_selected['PTS/Min'] = np.where(df_selected['MIN'] > 0, df_selected['PTS'] / df_selected['MIN'], 0)

# Overall Shooting Accuracy (average of FG%, 3P%, and FT%)
df_selected['Overall Shooting Accuracy'] = (df_selected['FG%'] + df_selected['3P%'] + df_selected['FT%']) / 3

# Average Blocks Per Game
df_selected['BLK/G'] = df_selected['BLK'] / df_selected['GP']

# Average Steals Per Game
df_selected['STL/G'] = df_selected['STL'] / df_selected['GP']

# Save the processed data to a new CSV file (using a raw string for the file path)
output_file_path = r"C:\Users\sethw\Documents\output.csv"
df_selected.to_csv(output_file_path, index=False)

print(f"Processed data saved to: {output_file_path}")
