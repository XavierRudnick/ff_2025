import pandas as pd
import io

#df1 = pd.read_csv(r"wr_data\fantasy_points_xtd.csv")
df = pd.read_csv(r"wr_data\merged_wr.csv")
#df3 = pd.read_csv(r"data\FantasyPros_ProFootball_WR.csv")

#df1["Player"] = df1["NAME"].str.replace(r'\s+\(.*\)', '', regex=True)

#print(df2.head())
#print(df1.head())
columns_to_merge_from_df2 = [
    "Player","Y/R" ,"AIR","AIR/R", "CATCHABLE","YACON","YACON/R","RZ TGT"
]

columns_to_merge_from_df2 = [
    "Player","RZ_REC","RZ_TGT","RZ_REC_PCT","RZ_YDS","RZ_P_TD","RZ_TGT_PCT"
]

columns_to_merge_from_df2 = [
    "Player","REC_I10","TGT_I10","REC_PCT_I10","YDS_I10","TD_I10","TGT_PCT_I10"
]

columns_to_merge_from_df2 = [
    "Player","FPTS","FPTS/G","RTD"
]

columns_to_drop = [
    "Player","FPTS","FPTS/G","RTD"
]

columns_to_merge_from_df2 = [
    "Player","XFP","TD/G","XTD"
]

def standardize_player_name(name):
    name = str(name).replace(' Jr.', '').replace(' Sr.', '').replace(' III', '').replace(' II', '').replace("'", "").replace(".", "").replace("Joshua","Josh").replace("Gabe","gabriel").strip().lower()
    # You might also want to remove punctuation or convert to lowercase
    # name = ''.join(char for char in name if char.isalnum() or char.isspace()).lower()
    return name

#df1['Player'] = df1['Player'].apply(standardize_player_name)
#df2['Player'] = df2['Player'].apply(standardize_player_name)

#print(df1[df1['Rank'] == 65])
#df2 = df2.drop(columns=columns_to_drop)
 

#merged_df = pd.merge(df2, df1[columns_to_merge_from_df2], on="Player", how="left")

#df2['fpts_diff'] =df2['FPTS/G'] - df2['XFP']
#df2['fpts_diff'] = df2['fpts_diff'].round(2)
#df['air_pct'] = df['air_pct'].round(2)
#df['WOPR'] = 1.5 * .01 * df["Target_Share"] + .7 * .01 * df['air_pct']
#df['AIR'] = df['AIR'].astype(str).str.replace(',', '', regex=False)
#df['AIR'] = pd.to_numeric(df['AIR'], errors='coerce')
#df['AIR'] = df['AIR'].astype('Int64')
#df['team_air'] = df.groupby('Team')['AIR'].transform('sum')
#df['air_pct'] = (df['AIR'] / df['team_air']) * 100
#df['WOPR'] = df['WOPR'].round(2)
sorted_players = df.sort_values(by='FPTS/G', ascending=False)
top_50_players = sorted_players.head(35)
print(top_50_players[['Player', 'FPTS/G']])

df['VOR'] = df["FPTS/G"] - 13
df['VOR'] = df["VOR"].round(2)

df.to_csv(r"wr_data\merged_wr.csv",index=False)