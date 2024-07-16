import streamlit as st
from news import get_top_articles
#from bd_connection import get_newest_top_news
from inserting_news import get_newest_pharmaceutical_news
def pharmaceutical_news():
    st.title('PHARMACEUTICAL NEWS!')
    
    articles = get_newest_pharmaceutical_news()
    for article in articles:
        st.markdown(f"### [{article['title']}]({article['url']})")
        st.write(f"**Publisher:** {article['publisher']}")
        st.write(f"**Summary:** {article['summarized_article']}")
        st.write("---")
