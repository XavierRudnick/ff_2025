import pandas as pd
import io

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


# Read the data into a pandas DataFrame, inferring the header from the first row
df = pd.read_csv(r"data\clean_wr_data.csv")

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

df.to_csv(r"data\clean_wr_data.csv",index=False)
