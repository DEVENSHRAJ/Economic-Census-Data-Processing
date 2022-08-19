import pandas as pd

#initialization
base_data="csv final rural extracted.csv"
merging_data="py  csv shrug_ec05_rural.csv"
left=["STATE-UT code","Village code"]
right=["ec05_state_id","ec05_village_id"]


#dataframe creation
rural_base_data=pd.read_csv(base_data,low_memory=False, dtype={"Image No.(Auto generated)": "string","Record No.(Auto Generated)": "string","Batch No.":"string"})
rural_shrid_merge_basedata=pd.read_csv(merging_data)
rural_shrid_merge_basedata.drop(["Unnamed: 0"], inplace=True, axis=1)


#merging work left join
rural_final_df = pd.merge(rural_base_data, rural_shrid_merge_basedata,  how='left', left_on=left, right_on = right)
rural_final_df.drop(right, inplace=True, axis=1)
rural_final_df.to_csv('rural final merged shrid.csv', index=False)