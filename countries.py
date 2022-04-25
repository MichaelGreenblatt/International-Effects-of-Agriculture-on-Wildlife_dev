import pandas as pd

#check variable types

#What is the file name? Revert to original name?
countries_data = pd.read_csv("un_country_statistics.csv")

continents = countries_data["Region Name"]
print("Number of Countries in the World:\n",continents.value_counts())

#%% Make each continent a list of countries?
#Are column names from file correct?
# Use cross-section or boolean selection (March 9 notes)
africa = continents.query("Region Name" == "Africa")
n_america = continents.query("Region Name" == "Northern America" & "Central America" & "Caribbean")
s_america = continents.query("Intermediate Region Name" == "South America")
asia = continents.query("Region Name" == "Asia")
europe = continents.query("Region Name" == "Europe")
oceania = continents.query("Region Name" == "Oceania")

#%% Use for loop instead of rows 7-12?
#for continent in continents:
#    continents.query("Region Name" == continent["Region Name"])

#%% Describe continents and countries
print("\nNumber of Countries in Africa:\n",africa.value_counts())
print("\nCountries in Africa:\n",africa)

print("\nNumber of Countries in North America:\n",n_america.value_counts())
print("\nCountries in North America:\n",n_america)

print("\nNumber of Countries in South America:\n",s_america.value_counts())
print("\nCountries in South America:\n",s_america)

print("\nNumber of Countries in Asia:\n",asia.value_counts())
print("\nCountries in Asia:\n",asia)

print("\nNumber of Countries in Europe:\n",europe.value_counts())
print("\nCountries in Europe:\n",europe)

print("\nNumber of Countries in Oceania:\n",oceania.value_counts())
print("\nCountries in Oceania:\n",oceania)

#%% Match countries from UN threatened species file to continents
#Does UN have endangered/extinct species file?
un_countries = pd.read_csv("SYB64_313_202110_Threatened Species.csv")
un_countries["continent"] = 
#How do I connect continent info between both files? For loop? M:1 merge?
#Do I need to do that or has it already been done from other file?

#%% Classify countries by income/development level
#Which API file should I use here? Do all have same numbers and column names?
income_data = pd.read_csv("Metadata_Country_API_EN.FSH.THRD.NO_DS2_en_csv_v2_3931066.csv")
country_income = income_data["IncomeGroup"]

# Compare countries from API file to countries in countries_data and drop non-countries
# Use join/append (March 7,9 notes)
# Do I need to make/reset index?
countries_merge = un_countries.merge(income_data,on="TableName",how="inner",validate="1:1",indicator=True)
print("\nNumber of Countries Worldwide After Merge:\n",countries_merge.value_counts())

# Calculate total number of countries in each income group
for income_group in country_income:
    #Use True statements?
    print(f"\nNumber of Countries Classified as {country_income}:\n",)

# Calculate countries in each income group by continent
for income_group in continents:
    


#%%



# When should I export data?