## Script to clean Excel travel data.
import pandas as pd

# Read xls file.
uk = pd.read_excel("series-010820_uk-visits-abroad.xls")

# Update terminal display options to show all rows.
# We need to see which rows to keep.
pd.set_option("display.max_rows", None)

# View all rows.
uk

# Only keep the monthly data. Tableau can do the aggregations.
uk = uk.iloc[178: , ]

# Reset display options to the default.
pd.reset_option("display.max_rows")

# Simplify the column names.
uk = uk.rename(columns = {"Title":"Date", "UK visits abroad: All visits Thousands - SA":"UK_Visits_Abroad"})

# Convert date strings to datetime. I'm impressed this worked so simply!
uk["Date"] = pd.to_datetime(uk["Date"])

# Values are in thousands, convert back to that.
uk["UK_Visits_Abroad"] = uk["UK_Visits_Abroad"] * 1000

# View results.
uk

# Read in population data
pop = pd.read_csv("series-050820_uk-population.csv")
pop

# Remove title information above.
pop = pop.iloc[7:, ]

# Rename columns.
pop = pop.rename(columns = {"Title":"Year", "United Kingdom population mid-year estimate":"Population"})
pop

# Create year column from date column.
uk["Year"] = pd.DatetimeIndex(uk["Date"]).year

# Look at uk dataset.
uk

# Group by Year and sum visits.
# We could have also just pulled the annual data from the original data file.
uk_year = uk.groupby(by='Year').sum()
uk_year

# Need to convert population year to integer.
pop.dtypes
pop["Year"] = pop["Year"].astype('int')

# Join visit and population data by year.
uk_year = pd.merge(uk_year, pop, how="inner", on="Year")

# Look at data types of each field.
uk_year.dtypes

# Convert population to an integer.
uk_year['Population'] = uk_year['Population'].astype('int')

# Create visits per capita calculated field.
uk_year["Visits_per_Capita"] = uk_year['UK_Visits_Abroad'] / uk_year['Population']

# Drop Year column, no longer needed.
uk = uk.drop(columns = 'Year')

# Review datasets.
uk
uk_year

# Save cleaned data to csv.
uk.to_csv("uk-visits-abroad.csv", index=False)
uk_year.to_csv("uk-visits-abroad-pc.csv", index=False)

