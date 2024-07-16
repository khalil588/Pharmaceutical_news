from gnews import GNews
from transformers import T5Tokenizer, T5ForConditionalGeneration
from bd_connection import  get_companies_to_get_news_from
# Load the tokenizer and model
tokenizer = T5Tokenizer.from_pretrained("Falconsai/text_summarization")
model = T5ForConditionalGeneration.from_pretrained("Falconsai/text_summarization")
google_news = GNews(period='1h',exclude_websites=['www.thepharmaletter.com','dailyjournal.net','www.politico.com','www.marketwatch.com','https://thehill.com/','www.newsobserver.com','www.portsmouth-dailytimes.com','www.reuters.com','www.timesofisrael.com','www.forbes.com','www.axios.com'])  # Set timeframe during initialization
import datetime

# Summarizing the article part 
def get_article(company=""):
    
    json_resp = google_news.get_news(company)
    news = []
    print(len(json_resp))
    if len(json_resp) > 0 :
        for i in json_resp :
            print(i) 
            article = google_news.get_full_article(
            i['url'])
            i['full_article'] = article.text 
            i['summarized_article'] = to_summarize(article.text)
            news.append(i)
    else : 
        return 0 

    return news


def to_summarize(ARTICLE=""): 
    # Preprocess the input text
    input_ids = tokenizer.encode("summarize: " + ARTICLE, return_tensors="pt", max_length=512, truncation=True)

    # Generate the summary
    summary_ids = model.generate(input_ids, max_length=1000, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)

    # Decode the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary


def get_total_news(): 
    companies_list = get_companies_to_get_news_from()
    all_news = []
    for company in companies_list : 
        new = get_article(company)
        if isinstance(new, list) : 
            all_news.extend(new)
    return all_news


def get_top_articles():
    
    json_resp = google_news.get_top_news()
    news = []
    print("###############################################")
    if len(json_resp) > 0 :
        print(len(json_resp))
        for i in json_resp :

            article = google_news.get_full_article(
            i['url'])
            #print(i)
            i['full_article'] = article.text 
            i['summarized_article'] = to_summarize(article.text)
            news.append(i)
    else : 
        return 0 

    return news





#print(get_top_articles())