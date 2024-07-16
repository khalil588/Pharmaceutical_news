from scr_bot import Scrapper


with Scrapper(teardown= False) as bot:
    bot.land_first_page()
    data_cl = bot.extracting_data()
    data_cl['search_news'] = 0
    data_cl.to_csv('data_collected.csv',index=False)