# Define the text you want to search through.
# PASTE YOUR FULL HTML CONTENT BETWEEN THE TRIPLE QUOTES BELOW.
import re
from scipy.stats import norm
import pandas as pd
def get_fair_prob(over_odds, under_odds):
    # Convert American odds to implied probability
    def american_to_prob(odds):
        if odds < 0:
            return (-odds) / (-odds + 100)
        else:
            return 100 / (odds + 100)

    prob_over = american_to_prob(over_odds)
    prob_under = american_to_prob(under_odds)
    
    # Remove vig
    total_prob = prob_over + prob_under
    fair_prob_over = prob_over / total_prob
    return fair_prob_over

# This is the key assumption
STD_DEV = 35
mean_df = pd.read_csv(r"wr_data\mean_lines.csv")

# Calculate fair probability for the over
mean_df['p_fair_over'] = mean_df.apply(lambda row: get_fair_prob(row['mean_over_odds'], row['mean_under_odds']), axis=1)

# Calculate the z-score from the fair probability
# norm.ppf is the inverse of the cumulative distribution function (probit function)
mean_df['z_score'] = norm.ppf(mean_df['p_fair_over'])

# Calculate the normalized line (the mean of the assumed distribution)
# formula: mean = current_x - (z_score * std_dev)
# However, ppf(p) gives the z-score for P(X < x) = p. We have P(X > x) = p_fair_over,
# so we need to use P(X < x) = 1 - p_fair_over.
mean_df['z_score_correct'] = norm.ppf(1 - mean_df['p_fair_over'])
mean_df['normalized_line'] = mean_df['mean_line'] - (mean_df['z_score_correct'] * STD_DEV)

# Create final dataframe and sort it
result_df = mean_df[['Player', 'normalized_line']].sort_values(by='normalized_line', ascending=False)
result_df.to_csv(r'wr_data\normalized_lines.csv', index=False)

print(result_df)














