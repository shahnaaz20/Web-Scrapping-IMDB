import requests,json,pprint,os
from bs4 import BeautifulSoup
from web_scrapping_tsak_4 import scrape_movie_details
url =  "https://www.imdb.com/title/tt0079221/fullcredits?ref_=tt_cl_sm#cast"
movie_id = url[27:36]
def scrap_movie_cast():
        if os.path.isfile(str(movie_id)+"1.json")==True:
                    with open(str(movie_id)+"1.json","r") as read_file:
                            cast_list = json.load(read_file)
                            return cast_list
        else:
            page = requests.get(url)
            soup = BeautifulSoup(page.text,"html.parser")
            table = soup.find("table",class_="cast_list")
            trs = table.find_all("td",class_="")
            cast_list=[]
            for tr in trs:
                actors_dic={}
                actor = tr.find("a").get_text().strip()
                imdb_id = tr.find("a")["href"][-10:-1]
                actors_dic["imdb_id"]=str(imdb_id)
                actors_dic["Name"]=str(actor)
                cast_list.append(actors_dic)
            json_file = open(str(movie_id)+"1.json","w")
            json.dump(cast_list,json_file,indent=2)
            return cast_list
pprint.pprint(scrap_movie_cast())
