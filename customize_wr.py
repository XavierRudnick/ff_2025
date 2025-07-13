import pandas as pd
import io
import re

def standardize_player_name(name):
    name = str(name).replace(' Jr.', '').replace(' Sr.', '').replace(' III', '').replace(' II', '').replace("'", "").replace(".", "").replace("Joshua","Josh").replace("Gabe","gabriel").strip().lower()
    return name

df = pd.read_csv(r"rush_data\pf_rush_rb.csv")

df.to_csv(r"rush_data\pf_rush_rb.csv",index=False)