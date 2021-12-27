import requests
import json
import pandas as pd
import urllib3
from sqlalchemy import create_engine
http=urllib3.PoolManager()
import psycopg2



agmarknet_insert = """
INSERT INTO agmarknet (state,district ,market , commodity ,variety, arrival_date  ,min_price    ,max_price  ,modal_price ) VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s) """

web_hk_url='https://bigdata348.webhook.office.com/webhookb2/67ed8852-6de4-4fa0-ac89-4c9c0bb3a4ce@3e8db0ca-95a6-4914-bac6-6cab03d9aa54/IncomingWebhook/fa2ad6575650437ba8929b982fde8eca/2c052b0c-c6da-4874-90a0-43ed59bdb83f'
def smsg(nor,db,table,movement_type):
    msg = {
        "@context": "https://schema.org/extensions",
        "@type": "MessageCard",
        "themeColor": "64a837",
        "title": "Agmarknet Data Append",
        "text":f"Data scuccesfully updated ",
        "sections":[
            {
                "facts": [
                    {
                        "name": "No of Records ",
                        "value": nor
                    },
                    {
                        "name": "Upload database",
                        "value": db
                    },
                    {
                        "name": "Upload table",
                        "value": table
                    },
                    {
                        "name":"Movement Type",
                        "value":movement_type
                    }
                   

                    
                ]
            }
        ]
    }
    encoded_msg = json.dumps(msg).encode('utf-8')
    resp = http.request('POST',web_hk_url, body=encoded_msg)


def lambda_handler(event,context):
    url = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070?api-key=579b464db66ec23bdd000001d9143fc81ac74bce7ad727abc2705a8a&format=csv&limit=10000"

    payload={}
    headers = {
      'accept': 'application/xml',
      'Cookie': 'BIGipServerapi.data.gov.in=!3+MbghwZgEPYHt6CbbshOuMRiHS6yPaTO/SoI8x2yuzWQTb260vG8vD/gim86FybvljnTZREBSVVyQ==; TS01a12685=0161d6dfc399201b55df766bb2117226b37bf28203848e59b7a982f2aaaf1352b4e590defb37aa8dd56601356220b9bc91328274e7; TS01a12685028=01e4def216eb6f369607dd6aaa5eca2f193f115ae365c13592f7be6de97164e5ec81a274c42a7ed178cfaad301add56178616e7022'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    x=response.text
    listt=x.split("\n")

    columns=listt[0].split(",")

    State=[]
    District=[]
    Market=[]
    Commodity=[]
    Variety=[]
    Arrival_Date=[]
    Min_x0020_Price=[]
    Max_x0020_Price=[]
    Modal_x0020_Price=[]

    for i in listt[1:-1]:
        State.append(i.split(',')[0])
        District.append(i.split(',')[1])
        Market.append(i.split(',')[2])
        Commodity.append(i.split(',')[3])
        Variety.append(i.split(',')[-5])
        Arrival_Date.append(i.split(',')[-4])
        Min_x0020_Price.append(i.split(',')[-3])
        Max_x0020_Price.append(i.split(',')[-2])
        Modal_x0020_Price.append(i.split(',')[-1])

    df=pd.DataFrame({'State':State,'District':District,'Market':Market,"Commodity":Commodity,"Variety":Variety,"Arrival_Date":Arrival_Date,"Min_Price":Min_x0020_Price,"Max_Price":Max_x0020_Price,"Modal_Price":Modal_x0020_Price})
    
    conn = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=postgres")
    cur = conn.cursor()
    for index, row in df.iterrows():
        cur.execute(agmarknet_insert, list(row.values))
        conn.commit()
        
    nor=len(df)
    db='postgres'
    table='agmarknet'
    movement_type='append'
    smsg(nor,db,table,movement_type)