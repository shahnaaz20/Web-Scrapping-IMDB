from bs4 import BeautifulSoup
import requests,pprint
from web_scrapping_tsak_4 import scrape_movie_details
from imdb_task_1 import scarp_movies
scarp_movies=scarp_movies()
url_list = []
for i in range(0,len(scarp_movies)):
    url_list.append(scarp_movies[i]["url"])
def scrape_10_movie_detail(movie):
    i = 0 
    movies_details=[]
    for i in movie:
        detail = scrape_movie_details(i)
        movies_details.append(detail)
    return(movies_details)
# pprint.pprint(scrape_10_movie_detail(url_list))

