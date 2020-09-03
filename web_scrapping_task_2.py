from imdb_task_1 import scarp_movies
import pprint
def movies_by_year():
        s_m = scarp_movies()
        movies_year_list = []
        for i in s_m:
                year=i["year"]
                if year not in movies_year_list:
                        movies_year_list.append(year)
        movies_year_dic={}
        for i in movies_year_list:
                movies_year_dic.update({i:[]})
        # print(movies_year_dic)
        c = 1
        for j in s_m:
                year = j["year"]
                # print(c,year)
                c+=1
                for k in movies_year_dic:
                        if k == year:
                                movies_year_dic[k].append(j)
        return(movies_year_dic)
# pprint.pprint(movies_by_year())
