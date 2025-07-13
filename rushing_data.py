import pandas as pd
import io
import re

def standardize_player_name(name):
    name = str(name).replace(' Jr.', '').replace(' Sr.', '').replace(' III', '').replace(' II', '').replace("'", "").replace(".", "").replace("Joshua","Josh").replace("Gabe","gabriel").strip().lower()
    return name

df = pd.read_csv(r"rush_data\pf_rush_rb.csv")
#df1 = pd.read_csv(r"rush_data\FantasyPros_Fantasy_Football_Advanced_Stats_Report_RB.csv")
#df2 =  pd.read_csv(r"rush_data\FantasyPros_Fantasy_Football_Statistics_RB.csv")
#df3 =  pd.read_csv(r"rush_data\FantasyPros_Fantasy_Football_Red_Zone_Report_RB.csv")
df4 = pd.read_csv(r"rush_data\rb_fantasy_points_xtd.csv")

#columns_to_drop = [
#    "TK LOSS_x","TK LOSS YDS_x","REC_x","TGT_x","RZ TGT_x","TK LOSS_y","TK LOSS YDS_y","REC_y","TGT_y","RZ TGT_y"
#]

#df = df.drop(columns=columns_to_drop)
#df.to_csv(r"rush_data\pf_rush_rb.csv",index=False)

#filtered_df = df[df['Pos'] == 'RB']
#filtered_df.to_csv(r"rush_data\pf_rush_rb.csv",index=False)

#df1["Player"] = df1["Player"].str.replace(r'\s+\(.*\)', '', regex=True)

#df1['Player'] = df1['Player'].apply(standardize_player_name)
#df['Player'] = df['Player'].apply(standardize_player_name)

#columns_to_merge_from_df1 = [
#    "Player","TK LOSS","TK LOSS YDS","REC","TGT","RZ TGT"
#]

#df2["Player"] = df2["Player"].str.replace(r'\s+\(.*\)', '', regex=True)

#df2['Player'] = df2['Player'].apply(standardize_player_name)
#df['Player'] = df['Player'].apply(standardize_player_name)

#columns_to_merge_from_df1 = [
#    "Player","Rush TD","Rec TD","Rec YDS","FPTS","FPTS/G"
#]

#merged_df = pd.merge(df, df2[columns_to_merge_from_df1], on="Player", how="left")

#df3["Player"] = df3["Player"].str.replace(r'\s+\(.*\)', '', regex=True)

#df3['Player'] = df3['Player'].apply(standardize_player_name)
#df['Player'] = df['Player'].apply(standardize_player_name)

#columns_to_merge_from_df1 = [
   # "Player","RZ YDS","RZ TD","RZ PCT","RZ REC","RZ TGT","RZ REC TD","RZ REC TGT PCT","RZ FPTS","RZ FPTS/G"
#]


#df4["Player"] = df4["NAME"].str.replace(r'\s+\(.*\)', '', regex=True)

#df4['Player'] = df4['Player'].apply(standardize_player_name)
#df['Player'] = df['Player'].apply(standardize_player_name)

#columns_to_merge_from_df2 = [
#    "Player","XFP","TD/G","XTD"
#]

#merged_df = pd.merge(df, df4[columns_to_merge_from_df2], on="Player", how="left")

df['fpts_diff'] =df['FPTS/G'] - df['XFP']
df['fpts_diff'] = df['fpts_diff'].round(2)

df['tds_diff'] =df['TD/G'] - df['XTD']
df['tds_diff'] = df['tds_diff'].round(2)

df.to_csv(r"rush_data\pf_rush_rb.csv",index=False)

