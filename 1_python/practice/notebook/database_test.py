import mysql.connector as connection
import pandas as pd
from tqdm import tqdm

df = pd.read_excel('./data/Data Challenge-Generic ED 2009.xlsx', engine='openpyxl')
df.dropna(inplace=True)
print(len(df))
length = len(df)
try:
    mydb = connection.connect(host='localhost',
                              user='root',
                              passwd='root',
                              database='sarvesh')
    cursor = mydb.cursor()
    # df['Arrival Date'] = [str(i).split('T')[0] for i in df['Arrival Date'].values][0]
    # df['Dr Seen Date'] = [str(i).split('T')[0] for i in df['Dr Seen Date'].values][0]
    # df['Depart Actual Date'] = [str(i).split('T')[0] for i in df['Dr Seen Date'].values][0]
    for index, row in tqdm(df.iterrows()):
        query = "insert into EDdata(MRN ,presentation_visit_no ,Triage_priority ,Age ,Arrival_date ,dr_seen_date ," \
                "Depart_actual_date ,depart_status_code ,departure_statue_desc ,depart_dest_code ,depart_dest_desc ," \
                "TimeDiff_Arrival_Actual_Depart ,TimeDiff_treatDrNr_Act_Depart ,presenting_complaint_code ," \
                "Presenting_complaint_desc ,diag_code ,diagnosis_desc) values('{}','{}','{}','{}','{}','{}','{}'," \
                "'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(
            *[row[i] for i in ['MRN', 'Presentation Visit Number', 'Triage Priority', ' Age  (yrs)',
                               'Arrival Date', 'Dr Seen Date', 'Depart Actual Date',
                               'Depart Status Code', 'Departure Status Desc.', 'Depart. Dest. Code',
                               'Depart. Dest. Desc.', 'TimeDiff Arrival-Actual Depart (mins)',
                               'TimeDiff TreatDrNr-Act. Depart (mins)', 'Presenting Complaint Code',
                               'Presenting Complaint Desc.', 'Diag Code', 'Diagnosis Desc.']])
        try:
            cursor.execute(query)
        except Exception as e:
            print(query + '\n')
            print(e)
            continue
        length -= 1
        if length == 0 or length <= 1:
            print('done')
        mydb.commit()



except Exception as e:
    print('something went wrong')
    print(query)
    print(e)
else:

    #     cursor.execute(query)
    mydb.commit()
    print('all good')
