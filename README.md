# Assignment-2
 Player stats Anaylyzer 
 Chat Logs @ https://chatgpt.com/share/67a415f9-f0a0-8000-baf3-c61cf38985b5

Player Stats Processor
This script reads a CSV file containing player statistics, calculates various shooting and defensive metrics, and saves the processed data to a new CSV file.

What the Script Does
Reads the CSV File:
It loads the CSV from a specified file path using Pandas.

Selects Relevant Columns:
The script extracts columns that are needed for the calculations:
Season
 Player
 GP (Games Played)
 MIN (Minutes Played)
 FGM (Field Goals Made)
 FGA (Field Goals Attempted)
 3PM (Three-Pointers Made)
 3PA (Three-Pointers Attempted)
 FTM (Free Throws Made)
 FTA (Free Throws Attempted)
 PTS (Points Scored)
 BLK (Blocks)
 STL (Steals)
 Converts Data to Numeric:
 Numeric columns are converted to appropriate types, with errors coerced to NaN.

Cleans the Data:
Rows with missing essential numeric data are removed.

Calculates Metrics:
The following metrics are computed:

Field Goal Accuracy (FG%): FGM divided by FGA.
Three-Point Accuracy (3P%): 3PM divided by 3PA.
Free Throw Accuracy (FT%): FTM divided by FTA.
Points Per Minute (PTS/Min): PTS divided by MIN.
Overall Shooting Accuracy: The average of FG%, 3P%, and FT%.
Blocks Per Game (BLK/G): BLK divided by GP.
Steals Per Game (STL/G): STL divided by GP.
Saves the Processed Data:
The script writes the resulting DataFrame with the added metrics to a new CSV file.

How to Run
Dependencies:
Make sure you have Python installed along with the numpy and pandas librarie


After running the script, you should see a message indicating that the processed data has been saved.
