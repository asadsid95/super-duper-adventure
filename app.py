# import requests
# from bs4 import BeautifulSoup

# # Define the URL of the webpage to scrape
# url = 'https://example-news-website.com'

# # Send a GET request to the webpage
# response = requests.get(url)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Parse the webpage content
#     soup = BeautifulSoup(response.content, 'html.parser')
    
#     # Find all article titles and links (adjust the tags and classes based on the webpage structure)
#     articles = soup.find_all('h2', class_='article-title')
    
#     # Loop through the articles and extract the title and link
#     for article in articles:
#         title = article.get_text()
#         link = article.find('a')['href']
        
#         # Print the title and link
#         print(f'Title: {title}')
#         print(f'Link: {link}')
#         print('-' * 80)
# else:
#     print(f'Failed to retrieve the webpage. Status code: {response.status_code}')

from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='8ea028de9aa54353ab079410273c0128')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='Apple',
                                          category='business',
                                          language='en',
                                          country='us')

# /v2/everything
# all_articles = newsapi.get_everything(q='bitcoin',
#                                       sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,techcrunch.com',
#                                       from_param='2017-12-01',
#                                       to='2017-12-12',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=2)

# /v2/top-headlines/sources
sources = newsapi.get_sources()

print(top_headlines)