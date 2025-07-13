import pandas as pd
import io
import re

df = pd.read_csv(r"wr_data\merged_wr.csv")

#columns_for_new_df = ['Player', 'Age', 'Team', 'G','Tgt','Rec','Yds','Target_Share','AIR','CATCHABLE','RZ TGT','RZ_REC','RZ_REC_PCT','RZ_P_TD','RZ_TGT_PCT','Routes Run','FPTS','FPTS/G','RTD','XFP','TD/G','XTD','fpts_diff','td_diff','team_air','air_pct','WOPR','VOR']
#new_df = df[columns_for_new_df]

df_example = pd.DataFrame(df)
print(df_example)