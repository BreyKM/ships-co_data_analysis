from dotenv import load_dotenv
load_dotenv()

import os
import pandas as pd

from supabase import create_client, Client

#supabase database connection
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

#query to get the data from multiple tables in the database
responseTable = supabase.table('usa_county_list') \
    .select('county, state, state_tax_rate(state_tax_rate), county_tax_rate(local_tax_rate), workforce_wages(annual_average_pay), median_county_income(median_income), unemployment_by_county(unemployment_rate)') \
    .filter('workforce_wages.industry', 'eq', '102 Service-providing') \
    .execute()


df = pd.DataFrame(responseTable.data)


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.options.display.width = 0


max_points_per_category = .25

#combine the state and county tax rates to create tax-rate column
for i in range(len(df)):
    if len(df['county_tax_rate'][i]) > 0:
        df.loc[i, 'tax-rate'] = df['state_tax_rate'][i]['state_tax_rate'] + \
            df['county_tax_rate'][i][0]['local_tax_rate']
        # print(df['tax-rate'][i])
    else:
        df.loc[i, 'tax-rate'] = df['state_tax_rate'][i]['state_tax_rate']
        # print(df['tax-rate'][i])

min_tax_rate = df['tax-rate'].min()
max_tax_rate = df['tax-rate'].max()

#create a tax-points column to rank counties based on tax-rate
for i in range(len(df)):
    number = df['tax-rate'][i]
    if number < min_tax_rate:
        normalize = 1
    elif number > max_tax_rate:
        normalize = 0
    else:
        normalize = 1 - ((number - min_tax_rate) /
                         (max_tax_rate - min_tax_rate))
    points = (max_points_per_category * normalize)
    df.loc[i, 'tax-points'] = points

# Average pay points
low_average_pay = 0
max_average_pay = 128547


