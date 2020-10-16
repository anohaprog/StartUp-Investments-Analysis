import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

data = pd.read_csv("investments_VC.csv", encoding='unicode_escape')
data = data.rename(columns={' market ': 'market', ' funding_total_usd ': 'funding_total_usd'})
data = data.dropna()

on_cols = {
    'market', 'funding_total_usd', 'status', 'country_code', 'city',
    'founded_at', 'seed', 'venture', 'equity_crowdfunding', 'undisclosed',
    'convertible_note', 'debt_financing', 'angel', 'grant', 'private_equity',
    'post_ipo_equity', 'post_ipo_debt', 'secondary_market', 'product_crowdfunding'
}

off_cols = list(filter(lambda x: x not in on_cols, data))
analysis_data = data.drop(off_cols, axis=1)

analysis_data['funding_total_usd'] = analysis_data['funding_total_usd'].str.replace(',','')
analysis_data['funding_total_usd'] = pd.to_numeric(analysis_data['funding_total_usd'], errors='coerce')

mappings = {}
for col in analysis_data.select_dtypes(['object']):
    values = analysis_data[col].unique()
    mappings[col] = dict(zip(values, range(len(values))))

analysis_data = analysis_data.replace(mappings)

corr = analysis_data.corr()
plt.figure(figsize=(20, 10))
sn.heatmap(corr, annot=True)
plt.show()