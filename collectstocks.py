from constant import *
from  alpaca_trade_api import REST, Stream
import pandas as pd

def remove_after_special(text):
    for char in '!$^/,()':  # Loop through potential special characters
        index = text.find(char)
        if index != -1:
            return text[:index]  # Return everything before the special character
    return text

def collect_data_alpaca(): 
    rest_client = REST(base_url=BASE_URL, key_id=API_KEY, secret_key=API_SECRET)
    news = rest_client.list_assets()
    #print(news)
    #df = pd.DataFrame(new._raw for new in news)
    df = pd.DataFrame(new._raw for new in news)
    print("Nombre d'action dans la bourse :")
    print(len(news))
    df['name'] = df['name'].apply(remove_after_special)
    df.to_csv('data.csv',index=False)
    """df_tradable = df.loc[df['tradable']==True]
    df_tradable=df_tradable.loc[df_tradable['status']=='active']
    df_tradable['symbol_rect'] = df_tradable['symbol'].apply(remove_after_special)
    #df_tradable.to_excel('what.xlsx',index=False)
    return df_tradable['symbol_rect'].values"""
collect_data_alpaca()