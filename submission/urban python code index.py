import pandas as pd


URBANSchedule=["Schedule no. cum Record ID","Sector Code","STATE-UT code","DISTRICT code","Town code","Frame code","Ward No.","Investigator Unit No.","UFS Block No.","Page Number","Line No.","Enterprise Premises Status Code No.","Running Serial No of Enterprise within a page","Activity code (Major or Subsidiary)","Major activity NIC â€“ 2004 Code","Classification code (Agri or Non Agri)","Operation Code (Perennial or Not)","Ownership Code","Social Group of owner code","Power/Fuel used for Enterprise activity","Registration Code (1st code)","Registration Code (2nd code)","Total No. of Persons Usually working :- Adult Male","Total No. of Persons Usually working :- Adult Female","Total No. of Persons Usually working :- Children Male","Total No. of Persons Usually working :- Children Female","Total No. of Persons Usually working :- Total","Non Hired Persons Usually working :- Adult Male","Non Hired Persons Usually working :- Adult Female","Non Hired Persons Usually working :- Children Male","Non Hired Persons Usually working :- Children Female","Non Hired Persons Usually working :- Non-Hired Total (col 17 to 20)","Source of Finance","Address Slip attached (Y or N)","Image No.(Auto generated)","Record No.(Auto Generated)","Batch No."]
urban_df=pd.DataFrame(columns=URBANSchedule)
errorfile = open("urban file containing error.txt", "w")
urban_index=[2,1,2,2,2,2,5,5,2,2,3,1,2,1,4,1,1,1,1,1,1,1,5,3,2,2,5,2,2,2,2,3,1,1,4,4,13]
temp_rows_data_for_df=[]
fileName="ec05st02s.txt"
num_lines = sum(1 for line in open(fileName))

#main part
linecount=-1
line_to_df_val=1000
progress=10000
non_numeric=73
last_reach=num_lines-(num_lines%line_to_df_val)
with open(fileName) as f_ec:
    for line in f_ec:
        linecount+=1
        line=line.strip()
        #progress meter
        if linecount%progress==0:
            print("progress :- ",linecount)
        if int(line[:2])==54:
            pass
        else:
            continue
        row_data=[]
        idx_reach=0
        for i in urban_index:
            val=line[idx_reach:idx_reach+i]
            try:
                if idx_reach>=non_numeric:
                    row_data.append(val)
                else:
                    row_data.append(int(val))
            except:
                errorfile.write("error occured at location: (line,column) as :- ("+str(linecount+1)+","+str(idx_reach+1)+")\n")
                row_data.append(val)
            idx_reach+=i
        temp_rows_data_for_df.append(row_data)
        if len(temp_rows_data_for_df)>=line_to_df_val or (linecount)>=last_reach:
            temp_df=pd.DataFrame(temp_rows_data_for_df,columns=URBANSchedule)
            urban_df=pd.concat([urban_df,temp_df], ignore_index=True)
            temp_df = temp_df[0:0]
            temp_rows_data_for_df=[]
            
errorfile.close()
urban_df.to_csv('csv final urban extracted.csv', index=False)
