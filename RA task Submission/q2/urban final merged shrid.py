import pandas as pd

#initialization
base_data="csv final urban extracted.csv"
merging_data="py csv shrug_ec05_urban.csv"
left=["STATE-UT code","DISTRICT code","Town code"]
right=["ec05_state_id","ec05_district_id","ec05_town_id"]

#dataframe creation
urban_base_data=urban_base_data=pd.read_csv(base_data, dtype={"Image No.(Auto generated)": "string","Record No.(Auto Generated)": "string","Batch No.":"string"})
urban_shrid_merge_basedata=pd.read_csv(merging_data)
urban_shrid_merge_basedata.drop(["Unnamed: 0"], inplace=True, axis=1)

#merging work left join

urban_final_df = pd.merge(urban_base_data, urban_shrid_merge_basedata,  how='left', left_on=left, right_on = right)
urban_final_df.drop(right, inplace=True, axis=1)
urban_final_df.to_csv('urban final merged shrid.csv', index=False)