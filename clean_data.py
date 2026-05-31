import pandas as pd
df=pd.read_csv("GoogleAds_DataAnalytics_Sales_Uncleaned.csv")
#print(df.info())
print(df.head())
#5. Rename column headers to be clean and uniform
df.columns =df.columns.str.strip()
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')
#1. Identifying all the null values
print("\n BEFORE (empty values):")
print(df.isnull().sum()) #when a coloumn is null it is denoted as T=1 and the amount of times T appears it gets added and hence giving us the number of missing values
df.clicks=df.clicks.fillna(df.clicks.mean())
df.impressions=df.impressions.fillna(df.impressions.mean())
df.cost=df.cost.fillna('Unknown')
df.leads=df.leads.fillna(df.leads.mean())
df.conversions=df.conversions.fillna(df.conversions.mean())
df.conversion_rate=df.conversion_rate.fillna(df.conversion_rate.mean())
df.sale_amount=df.sale_amount.fillna('Unknown')
print("\n")
print("AFTER:")
print(df.isnull().sum())
#2. Checking for duplicates
print("Duplicates found: ",df.duplicated().sum()) #no duplicates as per data
#3. Standardize text values MOBILE,mobile,Mobile as Mobile
df.device= df.device.str.strip().str.lower().str.capitalize()
df.location= df.location.str.strip().str.lower().str.capitalize()
df.campaign_name= "Data Analytics Course" #as there can be multiple mistake withe spelling adn spaces, manually detecting and fixing will take much longer time so standardizing by putting the same value for all
#4. Converting date formats to a consistent type
df.ad_date=pd.to_datetime(df.ad_date,format='mixed',dayfirst=True,errors='coerce')
df.ad_date=df.ad_date.dt.strftime('%d-%m-%Y')
print("\n BEFORE(datatype):")
print(df.dtypes)
#6. Fix data types
df.clicks=pd.to_numeric(df.clicks,errors='coerce')
df.clicks = df.clicks.round(0).astype('Int64') 
df.impressions=pd.to_numeric(df.impressions,errors='coerce')
df.impressions = df.impressions.round(0).astype('Int64') 
df.leads=pd.to_numeric(df.leads,errors='coerce')
df.leads = df.leads.round(0).astype('Int64') 
df.conversions=pd.to_numeric(df.conversions,errors='coerce')
df.conversions = df.conversions.round(0).astype('Int64')
df.conversion_rate=pd.to_numeric(df.conversion_rate,errors='coerce')
df.conversion_rate = df.conversion_rate.round(3)
print("\n AFTER:")
print(df.dtypes)
print("\n")
print(df.head())
df.to_csv("cleaned_data.csv",index=False) #saving to csv file and making the index as false as there is no index
print("Saved successfully")