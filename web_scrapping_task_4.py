from imdb_task_1 import scarp_movies
from bs4 import BeautifulSoup
import requests
import pprint
movies=scarp_movies()
def scrape_movie_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")

    movie_div = soup.find("div",class_="title_wrapper").h1.get_text()
    movie_name =""
    for i in movie_div:
        if i == "(":
            break
        else:
            movie_name=movie_name+i.strip()
    main_class = soup.find("div",class_="plot_summary")
    directer = main_class.find("div",class_="credit_summary_item")
    tag = directer.find_all("a")
    directer_list = []
    for i in tag:
        directer_list.append(i.get_text())
    # return directer_list
    
    movie_bio = soup.find("div",class_="summary_text").get_text().strip()

    main_div = soup.find("div",class_="subtext")
    run_time = main_div.find("time").get_text().strip()
    hour = int(run_time[0])*60
    if "min" in main_div:
        minutes = int(runtime[3:].strip("min"))
        runtime=hour+minutes
    else:
        runtime=hour

    genres=main_div.find_all("a")
    genres.pop()
    movie_genres=[i.get_text() for i in genres]

    url = soup.find("div",class_="poster").a["href"]
    pic_url = "https://www.imdb.com"+url

    details = soup.find("div",attrs={"class":"article","id":"titleDetails"})
    div_list = details.find_all("div")
    for div in div_list:
        h4_tag = div.find_all("h4")
        for text in h4_tag:
            if "Language:" in text:
                languages = div.find_all("a")
                movie_languages = []
                for language in languages:
                    movie_languages.append(language.get_text())
                # return movie_languages
            if "Country:" in text:
                Country_tag = div.find_all("a")
                Countries = []
                for Country in Country_tag:
                    Countries.append(Country.get_text())
                # return Countries   

    movie_details={}
    movie_details["Name"]=movie_name
    movie_details["Director"]=directer_list
    movie_details["Country"]=Countries
    movie_details["Language"]=movie_languages
    movie_details["Poster_img_url"]=pic_url
    movie_details["Bio"]=movie_bio
    movie_details["Runtime"]=int(runtime)
    movie_details["Gener"]=movie_genres
    return movie_details

# pprint.pprint(scrape_movie_details( "https://www.imdb.com/title/tt0079221/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=690bec67-3bd7-45a1-9ab4-4f274a72e602&pf_rd_r=WB97423KXBAS2Q6SYWGX&pf_rd_s=center-4&pf_rd_t=60601&pf_rd_i=india.top-rated-indian-movies&ref_=fea_india_ss_toprated_tt_2"))
# pprint.pprint(scrape_movie_details("https://www.imdb.com/title/tt0112870/"))

        

        
