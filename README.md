# AGMARKNET_Commodity_price_ETL_POSTGRES
This projects aims to collect and analyse the AGMARKNET Data, AGMARKNET is one Gov API that publish commoditiy price various mandi in INDIA. There is History data stored Manully htting the API on postman. Aim of the project is to store all the history data into postgres database and update this data base on daly basis using scheduled AWS lambda on daly basis. Nad connct the database to AWS quick sight and anlyse the data basis on daily basis

## Data sources (Open Sources)

Data come from hiiting the GOVT API :¶
API URL:https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070?api-key=579b464db66ec23bdd000001d9143fc81ac74bce7ad727abc2705a8a&format=csv&limit=10000

##sample DATA
![image](https://user-images.githubusercontent.com/56694165/147430522-7899e0e6-f224-4ee5-af65-e14a80898474.png)


## Project Summary

The project follows the follow steps:

Step 1: Scope the Project and Gather Data
Step 2: Explore and Assess the Data
Step 3: Define the Data Model
Step 4: Run ETL to Model the Data
Step 5: Complete Project Write Up

##Tables Details
![image](https://user-images.githubusercontent.com/56694165/147430579-e5f25ac2-1d71-4991-99f5-89861762d42b.png)

##Scheduling the the function to run daily Basis
Agmarknet_lambda.py is function which fetchs the data every day at 11:30 pm and pushes the data into redshift table

## Setting Alerts of On Microsoft teams
![image](https://user-images.githubusercontent.com/56694165/147430902-6aa9a2f3-c337-40b0-9d91-48cb36a1d763.png)


# Analysing on AWS Quicksight 
attaching the sample images on aws quicksight.

![image](https://user-images.githubusercontent.com/56694165/147431091-b4afdef3-f5a8-4a0d-bad6-3e70ecd129cb.png)
![image](https://user-images.githubusercontent.com/56694165/147431118-36e58611-991e-4e81-954b-5b23adc21389.png)
![image](https://user-images.githubusercontent.com/56694165/147431142-b157cb82-955d-41cb-a641-1c985d122cc2.png)
![image](https://user-images.githubusercontent.com/56694165/147431163-dc59a7a3-5779-45d8-9b22-b07873ec8ff2.png)





