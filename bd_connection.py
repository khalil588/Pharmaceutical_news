import pymongo
import pandas as pd 
import datetime
#from news import get_top_articles

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Hikma_news"]
Competition_name = db["Competition_name"]
all_stocks = db['all_stocks']
Top_news = db['Top_news']
Users = db['Team']

def get_all_comopanies(): 
    df = all_stocks.find()
    return(pd.DataFrame(list(df)))

def get_pharmaceutical_companies():
    df = Competition_name.find()
    return pd.DataFrame(list(df))

def update_pharmaceutical_companies(symbol,value):
    filter_criteria = {'Symbol': symbol}
    update_operation = {'$set': {'search_news': value}}
    result = Competition_name.update_one(filter_criteria, update_operation)

def get_users(): 
    df = Users.find()
    return pd.DataFrame(list(df))

def add_user(full_name,email,age,position,phone_number ): 
    document = {"Full_name":full_name,"Email":email,"Age":age,"Position":position,"Phone_Number":phone_number}
    result = Users.insert_one(document)
    print(f"Inserted document ID: {result.inserted_id}")

def delete_user(email): 
    query = {"Email":email}
    result = Users.delete_one(query)
    print(f"Deleted {result.deleted_count} document")


def get_companies_to_get_news_from(): 
    df = Competition_name.find({'search_news':1})
    data = pd.DataFrame(list(df))
    companies_list = data['Company Name'].to_list()
    return companies_list



