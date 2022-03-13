import re

from bs4 import BeautifulSoup

with open("blank/index.html", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
# name = soup.find_all("div", class_="user__name")
# for item in name:
#     print(item.text.strip())

# print(name)
#
# find_all_user_info = soup.find(class_="user__info").find_all("span")
#
# for item in find_all_user_info:
#     print(item.text)


# social = soup.find(class_="social__networks").find("ul").find_all("a")
# all_a = soup.find_all("a")
# for item in all_a:
#     item_text = item.text
#     item_url = item.get("href")
#     print(f'{item_text}:{item_url}')
# post_div = soup.find(class_="post__text").find_parent()
# print(post_div)

# post_div = soup.find(class_="post__text").find_parent("div", 'user__post')
# print(post_div)

links = soup.find(class_="ewe__links").find_all("a")
for link in links:
    link_href = link.get("href")
    link_href1 = link["href"]
    link_data_attr = link.get("data-attr")
    link_data_attr1 = link["data-attr"]
    print(link_href+"/"+link_data_attr)
    print(link_href1 + "/" + link_data_attr1)


find_odejda = soup.find_all(text=re.compile("[Mm]agazine"))
for find_item in find_odejda:
    print(find_item.text)
print(find_odejda)


