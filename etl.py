import pandas as pd
import psycopg2
from sql_queries import agmarknet_insert, markets_insert, state_insert, district_insert
import os

data_path='data.csv'
dbname="postgres" 
user="postgres" 
password="postgres"


erors=[]
sucess=[]
# reading the data
def read_data(data_path):
    df=pd.read_csv(data_path)
    #creating the district data
    x=df.groupby(['district','state'])[['state']].count()
    x.columns=['count']
    dis=x.reset_index().drop('count',axis=1)
    return df,dis

        
#creating the connection 

def creat_conn(dbname,user,password):
    conn = psycopg2.connect(f"host=127.0.0.1 dbname={dbname} user={user} password={password}")
    cur = conn.cursor()
    return cur

#inserting data into  the tables

def insert_data():
    for index, row in df.iterrows():
        cur.execute(agmarknet_insert, list(row.values))
        conn.commit()

    for i in df['market'].unique():
        cur.execute(markets_insert, [i])
        conn.commit()

    for i in df['state'].unique():
        cur.execute(state_insert, [i])
        conn.commit()

    for index, row in dis.iterrows():
        cur.execute(district_insert, list(row.values))
        conn.commit()
        
try:
    df,dis=read_data(data_path)
    print('Data read successfull')
except:
    print('Data Read Failed')
    
try:
    cur=creat_conn(dbname,user,password)
    print('connection successfull')
except:
    print('connection Failed')
    
try:
    insert_data()
    print("data insert successfull")
except:
    print('data insert failed')
    
    

     
    
        


