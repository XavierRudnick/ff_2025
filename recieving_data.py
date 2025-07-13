import pandas as pd
import io
import re

def calculate_target_share(df: pd.DataFrame) -> pd.DataFrame:

    if not all(col in df.columns for col in ['Player', 'Team', 'Tgt']):
        raise ValueError("DataFrame must contain 'Player', 'Team', and 'Tgt' columns.")

    # Calculate total targets for each team and map it back to each player's row
    # .transform('sum') ensures the sum is aligned back to the original DataFrame's shape
    df['Team_Total_Targets'] = df.groupby('Team')['Tgt'].transform('sum')

    # Calculate individual player's target share
    # Handle cases where Team_Total_Targets might be zero to avoid division by zero
    df['Target_Share'] = df.apply(
        lambda row: (row['Tgt'] / row['Team_Total_Targets']) * 100
        if row['Team_Total_Targets'] > 0 else 0,
        axis=1
    )
    df['Target_Share'] = df['Target_Share'].round(2)
    # Clean up the temporary column if desired, or keep it for debugging/insight
   
    #df = df.drop(columns=['Team_Total_Targets'])

    return df

def standardize_player_name(name):
    name = str(name).replace(' Jr.', '').replace(' Sr.', '').replace(' III', '').replace(' II', '').replace("'", "").replace(".", "").replace("Joshua","Josh").replace("Gabe","gabriel").strip().lower()
    # You might also want to remove punctuation or convert to lowercase
    # name = ''.join(char for char in name if char.isalnum() or char.isspace()).lower()
    return name

def routes_run():
    # Regex pattern:
    # (.+?) : Capturing Group 1: Player Name (non-greedy match for any characters)
    # :\\s* : Literal colon, followed by optional whitespace
    # (\\d+) : Capturing Group 2: Routes Run (one or more digits)
    # $ : End of the line

    routes_run_regex = re.compile(r'(.+?):\s*(\d+)$')

    for line in routes_run_txt.splitlines():
        line = line.strip()
        if not line: # Skip empty lines
            continue

        match = routes_run_regex.match(line)

        if match:
            player_name = match.group(1).strip()
            routes_run_str = match.group(2)

            try:
                routes_run = int(routes_run_str)
                data_for_df.append([player_name, routes_run])
            except ValueError as e:
                print(f"Error converting data for line: '{line}' - {e}")
        else:
            # This will now catch any lines that don't conform to "Player Name: Routes Run"
            print(f"Skipping line (does not match 'Player Name: Routes Run' pattern): '{line}'")

    df_routes_run_new = pd.DataFrame(data_for_df, columns=['Player', 'Routes Run'])


# Read the data into a pandas DataFrame, inferring the header from the first row
df = pd.read_csv(r"data\merged_wr.csv")

routes_run_txt = r"data\routes_run_wr.txt"
data_for_df = []

"""
## Wrapping Header Names
# Get the current column names
original_headers = df.columns.tolist()
# Wrap each header name in double quotes
quoted_headers = ['"' + str(col) + '"' for col in original_headers]
# Join them into a single string
header_string = ','.join(quoted_headers)

## Wrapping Second Column Values (Player Names)
# Get the 'Player' column (which is the second column)
player_names = df['Player']
# Wrap each player name in double quotes. Note: Some names already have quotes (like "JaMarr Chase").
# We will remove existing quotes first to avoid double quoting, then add new quotes.
cleaned_and_quoted_names = ['"' + str(name).strip('"') + '"' for name in player_names]
# Join them into a single string
player_names_string = ', '.join(cleaned_and_quoted_names)

columns_to_drop = ['Int', 'Awards',"-9999"]
df = df.drop(columns=columns_to_drop)

df = calculate_target_share(df)

"""

merged_df_final.to_csv(r"data\FantasyPros_ProFootball_WR.csv",index=False)
