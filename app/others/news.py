print("Hello News")

from newsapi import NewsApiClient
#import newsapi

# Init
newsapi = NewsApiClient(api_key='371f269807584ff8bce67cb14efe32c6')

# /v2/everything

all_articles = newsapi.get_everything(q='cartagena',
                                      #sources='bbc-news,the-verge',
                                      #domains='bbc.co.uk,techcrunch.com',
                                      from_param='2025-05-19',
                                      to='2025-06-18',
                                      language='en',
                                      sort_by='relevancy',
                                      page=1)


#print(all_articles)
#print(all_articles["articles"])

# "For loop"
for article in all_articles["articles"]:
    print("--- Article ---")
    #print(article)
    print(f"TITLE: {article['title']}")
    print(f"PUBLISHED DATE: {article["publishedAt"]}")
    print(f"URL: {article["url"]}")
    #print(article["title"])


