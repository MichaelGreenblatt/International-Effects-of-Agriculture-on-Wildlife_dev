import pandas as pd

#
country_info = pd.read_csv("SYB64_145_202110_Land.csv")
country = country_info["Land"]
#Drop country names in country that aren't really countries
#Fix column headings in file - move row 2 to row 1
land_area = country_info["Series" == "Land area (thousand hectares)"]
#Isolate each occurance by year from land area row

#Some units are in thousand hectares - either indicate that or *1000
print("\nTotal Land Area Worldwide:\n",*1000)

print("\nArable Land Area Worldwide, 2005:\n",)
print("\nArable Land Area Worldwide, 2018:\n",)
print("\nPercent Change in Arable Land Area Worldwide, 2005 to 2018:\n",variable1/variable2)

print("\nLand Area Covered by crops, 2005:\n",)
#Add more print statements for each measure

#%%
