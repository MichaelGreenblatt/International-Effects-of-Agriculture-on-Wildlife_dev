import pandas as pd
import geopandas as gpd

geo_data = pd.read_csv("Countries & Territories Taxonomy MVP - C&T Taxonomy with HXL Tags.csv")
geo_data = geo_data.drop(columns=["ID","HRinfo ID","RW ID","m49 numerical code","FTS API ID",
                                  "Appears in UNTERM list","Appears in DGACM list",
                                  "ISO 3166-1 Alpha 2-Codes","ISO 3166-1 Alpha 3-Codes",
                                  "x Alpha2 codes","x Alpha3 codes","m49 Alt Term",
                                  "ISO Alt Term","UNTERM Alt Term","FTS Alt Term",
                                  "HRinfo Alt Term","RW Short Name","RW API Alt Term",
                                  "English Short","French Short","Spanish Short","Russian Short",
                                  "Chinese Short","Arabic Short","Admin Level","Region Code",
                                  "Region Name","Sub-region Code","Sub-region Name",
                                  "Intermediate Region Code","Intermediate Region Name","Regex",
                                  "Currency","Concatenation"])

#%% Match countries with UN file in countries.py
countries_geo_data = un_countries.merge(geo_data,on="Preferred Term",how="inner",validate="1:1",indicator=True)
print("Number of Countries Worldwide After the Merge:\n",countries_geo_data.value_counts())
countries_geo_data = countries_geo_data.drop(columns="_merge")

# Delete excess countries


#%% Match countries in UN file to their coordinates
lat = countries_geo_data["Latitude"]
long = countries_geo_data["Longitude"]
coords = [lat,long]

country_coords = countries_geo_data.join(coords,)