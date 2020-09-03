from web_scrapping_task_5 import scrape_10_movie_detail
from web_scrapping_tsak_4 import scrape_movie_details
from imdb_task_1 import scarp_movies
scarp_movies=scarp_movies()
url_list = []
for i in range(0,10):
    url_list.append(scarp_movies[i]["url"])
movies_detail_list = scrape_10_movie_detail(url_list)
def directors():
    director_dic={}
    count=1
    for i in movies_detail_list:
        for j in i["Director"]:
            if j not in director_dic:
                director_dic[j]=1
            else:
                director_dic[j]+=1
    return(director_dic)
# print(directors())
        