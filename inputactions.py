import pandas as pd
import config
# Read the xls file
data = pd.read_excel(config.Input_file)

# Access data
for index, row in data.iterrows():
    print(row['TestCase'], "",row['OrgId'])

    # Use username and password for your tests