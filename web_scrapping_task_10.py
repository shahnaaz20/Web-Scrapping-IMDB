from web_scrapping_task_5 import scrape_10_movie_detail
from web_scrapping_tsak_4 import scrape_movie_details
from imdb_task_1 import scarp_movies
import pprint
scarp_movies=scarp_movies()
url_list = []
for i in range(0,10):
    url_list.append(scarp_movies[i]["url"])
movies_detail_list= scrape_10_movie_detail(url_list)
main_dic={}
for i in movies_detail_list:
    for director in i["Director"]:
        if director in i["Director"]:
            main_dic[director]={}
    for index in range(len(movies_detail_list)):
        for director in main_dic:
            if director in movies_detail_list[index]["Director"]:
                for language in movies_detail_list[index]["Language"]:
                    main_dic[director][language]=0

    for  counter in range(len(movies_detail_list)):
        for director in main_dic:
            if director in movies_detail_list[counter]["Director"]:
                for language in movies_detail_list[counter]["Language"]:
                    main_dic[director][language]+=1

pprint.pprint(main_dic)

                    
