import pprint
from web_scrapping_tsak_4 import scrape_movie_details
from web_scrapping_task_13 import scrap_movie_cast
from imdb_task_1 import scarp_movies
scarp_movies=scarp_movies()
def actor_with_movie():
    url_list = []
    for i in range(0,5):
        url_list.append(scarp_movies[i]["url"])
    movie_cast_list = []
    for i in url_list:
        url_id = i[27:36]
        scrap_movie_casts = scrap_movie_cast("https://www.imdb.com/title/"+str(url_id)+"/fullcredits?ref_=tt_cl_sm#cast")
        movie_cast_list.append(scrap_movie_casts)
    main_dic={}
    for all_movie_cast in movie_cast_list:
        my_list=[]
        for actors in all_movie_cast:
            dic={}
            name = actors["Name"]
            imdb_id = actors["imdb_id"]
            if name not in my_list:
                dic["Name"]=name
                dic["num_movies"]=1
            else:
                dic["num_movies"]+=1
            main_dic[imdb_id]=dic
    pprint.pprint(main_dic)
actor_with_movie()