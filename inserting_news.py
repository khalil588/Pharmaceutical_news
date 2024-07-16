
import pymongo
import pandas as pd 
import datetime
from news import get_top_articles,get_total_news

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Hikma_news"]
Competition_name = db["Competition_name"]
all_stocks = db['all_stocks']
Top_news = db['Top_news']
Users = db['Team']
news = db['News']


def add_top_news_to_db(): 
    

    # Current date and time
    now = datetime.datetime.now()

    # Print the current timestamp
    #print("Current Timestamp:", now)
    formatted_timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    #print("Formatted Timestamp:", formatted_timestamp)
    articles = get_top_articles()
    lst_doc = []
    for article in articles :
        document =  {"title":article['title'],"url":article['url'],'publisher':article['publisher']['title'],'summarized_article':article['summarized_article'],'timestamp':formatted_timestamp}
        lst_doc.append(document)
    result = Top_news.insert_many(lst_doc)
    print('Done!')
    #print(f"Inserted document ID: {result.inserted_id}")



def get_newest_top_news(): 
    # Step 1: Find the maximum timestamp
    max_timestamp_doc = Top_news.find_one(sort=[('timestamp', -1)])
    max_timestamp = max_timestamp_doc['timestamp']

    # Step 2: Retrieve all documents with the maximum timestamp
    documents_with_max_timestamp = Top_news.find({'timestamp': max_timestamp})
    documents_list = list(documents_with_max_timestamp)
    return documents_list

#add_top_news_to_db()



def add_pharmacutical_news_to_db(): 
    

    # Current date and time
    now = datetime.datetime.now()

    # Print the current timestamp
    #print("Current Timestamp:", now)
    formatted_timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    #print("Formatted Timestamp:", formatted_timestamp)
    articles = get_total_news()
    lst_doc = []
    print(len(articles))
    for article in articles :
        document =  {"title":article['title'],"url":article['url'],'publisher':article['publisher']['title'],'summarized_article':article['summarized_article'],'timestamp':formatted_timestamp}
        lst_doc.append(document)
    result = news.insert_many(lst_doc)
    print('Done!')
    #print(f"Inserted document ID: {result.inserted_id}")



def get_newest_pharmaceutical_news(): 
    # Step 1: Find the maximum timestamp
    max_timestamp_doc = news.find_one(sort=[('timestamp', -1)])
    max_timestamp = max_timestamp_doc['timestamp']

    # Step 2: Retrieve all documents with the maximum timestamp
    documents_with_max_timestamp = news.find({'timestamp': max_timestamp})
    documents_list = list(documents_with_max_timestamp)
    return documents_list

#add_pharmacutical_news_to_db()