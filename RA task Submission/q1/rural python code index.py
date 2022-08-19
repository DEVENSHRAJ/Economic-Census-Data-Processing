import pandas as pd
import datetime

RURALSchedule=["Schedule no. cum Record ID","Sector Code","STATE-UT code","DISTRICT code","TEHSIL etc. code","Village code","Enumeration Block No.","Page Number","Line No.","Enterprise Premises Status Code No.","Running Serial No of Enterprise within a page","Activity code (Major or Subsidiary)","Major activity NIC â€“ 2004 Code","Classification code (Agri or Non Agri)","Operation Code (Perennial or Not)","Ownership Code","Social Group of owner code","Power/Fuel used for Enterprise activity","Registration Code (1st code)","Registration Code (2nd code)","Total No. of Persons Usually working :- Adult Male","Total No. of Persons Usually working :- Adult Female","Total No. of Persons Usually working :- Children Male","Total No. of Persons Usually working :- Children Female","Total No. of Persons Usually working :- Total","Non Hired Persons Usually working :- Adult Male","Non Hired Persons Usually working :- Adult Female","Non Hired Persons Usually working :- Children Male","Non Hired Persons Usually working :- Children Female","Non Hired Persons Usually working :- Non-Hired Total (col 17 to 20)","Source of Finance","Address Slip attached (Y or N)","Image No.(Auto generated)","Record No.(Auto Generated)","Batch No."]

rural_df=pd.DataFrame(columns=RURALSchedule)
errorfile = open("rural file containing error.txt", "w")
rural_index=[2,1,2,2,4,8,4,2,3,1,2,1,4,1,1,1,1,1,1,1,5,3,2,2,5,2,2,2,2,3,1,1,4,4,13]
temp_rows_data_for_df=[]
fileName="ec05st02.txt"
num_lines = sum(1 for line in open(fileName))


#main part

now_initial = datetime.datetime.now()
print ("Initial Current date and time : ",now_initial)

linecount=-1
line_to_df_val= 1000   
progress=  100000        
non_numeric=73
last_reach=num_lines-(num_lines%line_to_df_val)
with open(fileName) as f_ec:
    for line in f_ec:
        linecount+=1
        line=line.strip()
        #progress meter
        if linecount%progress==0:
            print("progress :- ",linecount)
        if int(line[:2])==53:
            pass
        else:
            continue
        row_data=[]
        idx_reach=0
        for i in rural_index:
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
            temp_df=pd.DataFrame(temp_rows_data_for_df,columns=RURALSchedule)
            rural_df=pd.concat([rural_df,temp_df], ignore_index=True)
            temp_df = temp_df[0:0]
            temp_rows_data_for_df=[]
            
now_final = datetime.datetime.now()
print ("Final Current date and time : ",now_final)
print("Approx time of execution:- ", now_final-now_initial)

rural_df.to_csv('csv final rural extracted.csv', index=False)