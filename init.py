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

print(df)