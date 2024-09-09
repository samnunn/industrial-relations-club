import pandas as pd
import numpy as np

df_payrates = pd.read_csv('dit-salaries.csv', parse_dates=['date_start', 'date_end'], dtype={'year': str})

json = df_payrates.to_json(orient="records", date_format="iso")
with open('_site/dit-salaries.json', 'w') as f:
    f.write(json)