from bs4 import BeautifulSoup
import requests
import pprint

url = "https://www.imdb.com/india/top-rated-indian-movies/"
page = requests.get(url)
soup = BeautifulSoup(page.text,"html.parser")

def scarp_movies():
        main_div = soup.find("div",class_="lister")
        tbody = main_div.find("tbody",class_="lister-list")
        trs = tbody.find_all("tr")
        movies_ranking=[]
        movies_name = []
        movies_year =[]
        movies_rating=[]
        movies_link = []
        # return trs
        for tr in trs:
                p = tr.find("td",class_ = "titleColumn").get_text().strip()
                rank = ""
                for i in p:
                        if "." not in i:
                                rank = rank + i
                        else:
                                break
                movies_ranking.append(rank)
                # return(movies_ranking)
                titles = tr.find("td",class_ = "titleColumn").a.get_text()
                movies_name.append(titles)
                # return(movies_name)
                ratings = tr.find("td",class_ = "ratingColumn imdbRating").strong.get_text()
                movies_rating.append(ratings)
                # return(movies_rating)
                years = tr.find("td",class_ = "titleColumn").span.get_text()
                movies_year.append(years[1:5])

                link = tr.find("td",class_ ="posterColumn").a['href']
                movie_link = "https://www.imdb.com"+link
                movies_link.append(movie_link)
        # return(movies_link)
        top_rated_movies = []
        i = 0
        while i < len(movies_ranking):
                
                details ={"position":""}
                details["position"]=movies_ranking[i]
                details["name"]=str(movies_name[i])
                details["year"]=int(movies_year[i])
                details["rating"]=float(movies_rating[i])
                details["url"]=movies_link[i]
                top_rated_movies.append(details)  
                i = i + 1     
        return(top_rated_movies)
# pprint.pprint(scarp_movies())
# # print(scarp_movies())

