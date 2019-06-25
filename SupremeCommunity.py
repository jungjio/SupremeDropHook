import lxml.etree as ET
import datetime
import discord
import time
import os
import requests
from discord.ext import commands
from datetime import date
from bs4 import BeautifulSoup
import sys
import time
import json





BASELINK = "https://www.supremecommunity.com"
SUPREMELINK = "https://www.supremecommunity.com/season/spring-summer2019/droplist/"
date = "2019-06-27"
WEBHOOK = "INSERT YOUR WEBHOOK"
SUPREMELINK = SUPREMELINK + date
CATEGORY = ["accessories",
"jackets",
"tops-sweaters",
"sweatshirts",
"t-shirts",
"t-shirt",
"shorts",
"bags",
"pants",
"skate",
"shoes",
"accessories",
"shirts",
"hats"]








source = requests.get(SUPREMELINK)
soup = BeautifulSoup(source.content, "html.parser")

# print(soup.encode("utf-8"))
count = 0
nameArray = []
keywordArray = []
priceArray = []
categoryArray = []
links = []
for text in soup.find_all('h2'):
    nameArray.append(text.get_text())
    x = text.get_text()
    x = "+" + x
    x = (x.replace(" ",",+"))
    keywordArray.append(x.lower())

for category in soup.find_all('p',{"class": "category hidden"}):
    print(category.get_text())
    if category.get_text() in CATEGORY:
        categoryArray.append(category.get_text())
        #print(category.get_text())
    elif category.get_text() == "":
        categoryArray.append(category.get_text())
        #print(category.get_text())
    elif category.get_text() == "z":
        continue

print(len(categoryArray))
print(categoryArray)

for link in soup.find_all('img',{"class": "prefill-img"}):
    links.append(BASELINK + str(link['src']))
    print(BASELINK + str(link['src']))

print(len(links))

for priceusd in soup.find_all('p',{"class": "priceusd hidden"}):
    if int(priceusd.get_text()) < 9000 :
        priceArray.append(priceusd.get_text())
        print((priceusd.get_text()))

print(len(priceArray))



for x in range(len(nameArray)):

    # if "Raiders" in nameArray[x]:
        # webhook = DiscordWebhook(url=WEBHOOK2)
        # # create embed object for webhook
        # embed = DiscordEmbed(title=nameArray[x], description=keywordArray[x], color=242424)
        #
        #
        # # add embed object to webhook
        # webhook.add_embed(embed)
        #
        # # # add fields to embed
        # embed.add_embed_field(name='Price', value="$" + priceArray[x])
        # embed.add_embed_field(name='Category', value=categoryArray[x])
        #
        # # # set image
        # embed.set_image(url=links[x])
        #
        # # # set footer
        # embed.set_footer(text='Created by J.io')
        # webhook.execute()
        # time.sleep(5)




    # nameArray[x] = nameArray[x].replace("®", "")
    # keywordArray[x] = keywordArray[x].replace("®", "")
    if categoryArray[x] == "":
        categoryArray[x] = "N/A"
        # print(nameArray[x])
        if "Tee" in nameArray[x] or "tee" in nameArray[x]:
            categoryArray[x] = "t-shirts"
    if priceArray[x] == "0":
        priceArray[x] = "N/A"
    sendMe = {
      "username": "Supreme",
      "embeds": [
        {
          "title": nameArray[x],
          "description": keywordArray[x],
          "color": 242424,
          "fields": [
            {
              "name": "Price",
              "value": priceArray[x],
              "inline": True
            },
            {
              "name": "Category",
              "value": categoryArray[x],
              "inline": True
            }
          ],
          "image": {
            "url": links[x]
          },
          "footer": {
            "text": "Made by J.io",
          }
        }
      ]
    }

    response = requests.post(WEBHOOK, data=json.dumps(sendMe), headers={'Content-Type': 'application/json'})
    print(response.status_code, response.text)
    time.sleep(3)
    print(sendMe)
    print("Name: " +  nameArray[x] + "\nKeywords: " + keywordArray[x] + "\nPrice: " +  priceArray[x] +  "\nCategory: " + categoryArray[x]+ "\nIMGLINK : " + links[x])


    # else:
    #     webhook = DiscordWebhook(url=WEBHOOK2)
    #     # create embed object for webhook
    #     embed = DiscordEmbed(title=nameArray[x], description=keywordArray[x], color=242424)
    #
    #
    #     # add embed object to webhook
    #     webhook.add_embed(embed)
    #
    #     # # add fields to embed
    #     embed.add_embed_field(name='Price', value="$" + priceArray[x])
    #     embed.add_embed_field(name='Category', value=categoryArray[x])
    #
    #     # # set image
    #     embed.set_image(url=links[x])
    #
    #     # # set footer
    #     embed.set_footer(text='Created by J.io')
    #     webhook.execute()
    #     time.sleep(5)
