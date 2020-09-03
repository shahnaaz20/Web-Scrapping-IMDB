from web_scrapping_task_2 import movies_by_year
import pprint
movies_year = movies_by_year()
def group_by_decade():
    movies_dec = {}
    list_of_dec = []
    for year in movies_year:
        mod = year%10
        dec = year-mod
        if dec not in list_of_dec:
            list_of_dec.append(dec)
    list_of_dec.sort()
    for i in list_of_dec:
        movies_dec[i]=[]
    print(movies_dec)
    for dec_10 in movies_dec:
        print(dec_10)
        decade = dec_10+9
        print(decade)
        for k in movies_year:
            print(k)
            if k <= decade and k>=dec_10:
                for v in movies_year[k]:
                    movies_dec[dec_10].append(v)
    return(movies_dec)
# pprint.pprint(group_by_decade())


        
    