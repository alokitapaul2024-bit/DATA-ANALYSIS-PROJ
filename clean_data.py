import pandas as pd
df=pd.read_csv("GoogleAds_DataAnalytics_Sales_Uncleaned.csv")
print(df.head())
#Rename column headers to be clean and uniform
df.columns =df.columns.str.strip() #removing extra spaces
df.columns = df.columns.str.lower() #making the word to lowercase
df.columns = df.columns.str.replace(' ', '_') #replacing the spaces with underscores
#Identifying all the null values
print("\n BEFORE (empty values):")
print(df.isnull().sum()) #when a coloumn is null it is denoted as True i.e 1(binary 1 & 0) and the amount of times T appears it gets added and hence giving us the number of missing values
#filling all the null space  with the most common value found in the coloumn(mode)-for the numeric items and filling the rest strings with 'Unknown'
df.clicks=df.clicks.fillna(df.clicks.mode())
df.impressions=df.impressions.fillna(df.impressions.mode())
df.cost=df.cost.fillna('Unknown')
df.leads=df.leads.fillna(df.leads.mode())
df.conversions=df.conversions.fillna(df.conversions.mode())
df.conversion_rate=df.conversion_rate.fillna(df.conversion_rate.mode())
df.sale_amount=df.sale_amount.fillna('Unknown')
print("\n")
print("AFTER:")
print(df.isnull().sum()) #checking for nulls after doing the above operation
#Checking for duplicates
print("Duplicates found: ",df.duplicated().sum()) 
#Standardize text values e.g 'MOBILE,mobile,Mobile' as Mobile
df.device= df.device.str.strip().str.lower().str.capitalize() #making the word to lowercase and then just capitalizing the first letter
df.location= "Hyderabad"#as there can be multiple mistake withe spelling and spaces, manually detecting and fixing is not efficient, so standardizing by putting the same value for all(as everyone went for Hyderabad only)
df.campaign_name= "Data Analytics Course" #as there can be multiple mistake withe spelling and spaces, manually detecting and fixing is not efficient, so standardizing by putting the same value for all(as everyone went for data analytics course only)
#Converting date formats to a consistent type
df.ad_date=pd.to_datetime(df.ad_date,format='mixed',dayfirst=True,errors='coerce')#as the date formats can be of diff types so letting python know if there are multiple formats of date and stting as the the element of the date to be the day number of the month, errors='coerce': Replaces anything not matching the provided formats with NaN
df.ad_date=df.ad_date.dt.strftime('%d-%m-%Y') #setting the format
print("\n BEFORE(datatype):")
print(df.dtypes) #checking how the datatypes are set initially
#Fixing data types of specific coloumns
df.clicks=pd.to_numeric(df.clicks,errors='coerce')  #errors='coerce': Replaces anything not matching the provided formats with NaN to keep the data safe from being inconsistent
df.clicks = df.clicks.round(0).astype('Int64') #rounding off and then converting to integer datatype
df.impressions=pd.to_numeric(df.impressions,errors='coerce')
df.impressions = df.impressions.round(0).astype('Int64') 
df.leads=pd.to_numeric(df.leads,errors='coerce')
df.leads = df.leads.round(0).astype('Int64') 
df.conversions=pd.to_numeric(df.conversions,errors='coerce')
df.conversions = df.conversions.round(0).astype('Int64')
df.conversion_rate=pd.to_numeric(df.conversion_rate,errors='coerce')
df.conversion_rate = df.conversion_rate.round(3) #rounding off to next 3 decimal places(as mostly observed data in the dataset is in this format)
print("\n AFTER:")
print(df.dtypes)
print("\n")
print(df.head()) #checking the data after cleaning
df.to_csv("cleaned_data.csv",index=False) #saving to csv file and making the index as false as there is no index
print("Saved successfully")