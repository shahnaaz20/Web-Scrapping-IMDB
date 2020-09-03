# import requests 
# import bs4
# from bs4 import BeautifulSoup
# url = "https://www.imdb.com/india/top-rated-indian-movies/"
# response = requests.get(url)
# print(response)
# bs = bs4.BeautifulSoup(response.text,"html.parser")
# formatted = bs.prettify()
# with open("imdb.html","w+") as my_file:
#     my_file.write(formatted)
# # list_img = bs.find_all("a")
# # print(len(list_img))
# def scarp_movies():
#     main_div = bs.find("div",class_="lister")
#     tbody = main_div.find("tbody",class_="lister-list")
#     trs = tbody.find_all("tr")
#     movie_rank=[]
#     movie_name = []
#     for tr in trs:
#         p = tr.find("td",class_="posterColumn").get_text().strip()
#         rank = ""
#         for i in p:
#             if "." not in i:
#                 rank = rank + i
#             else:
#                 break
#         movie_rank.append(rank)
#         title = tr.find("td",class_ ="titleColumn").a.get_text
#         return title
# print(scarp_movies())
