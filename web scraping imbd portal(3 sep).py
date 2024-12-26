# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 08:49:43 2024

@author: om
"""

from bs4 import BeautifulSoup as bs
import requests
link='https://m.imdb.com/title/tt0068646/reviews?ref_=tt_urv'
page=requests.get(link)
page
page.content
soup=bs(page.content,'html.parser')
print(soup.prettify())
#prettify() function which removes all unnecessary data ,header-footer


title = soup.find_all('a',class_="title")
title
review_title=[]
for i in range(0,len(title)):
    review_title.append(title[i].get_text())
review_title
review_title[:]=[title.strip('\n') for title in review_title]
review_title
len(review_title)
################################################
###we got 25 review titles
###now let us scrab rating
#rating = soup.find_all('svg',class_='ipl-icon ipl-star-icon')
rating = soup.find_all('span',class_='point-scale')
rating
rate=[]
for i in range(0,len(rating)):
    rate.append(rating[i].get_text())
rate
rate[:]=[r.strip('/') for r in rate]
rate
len(rate)
rate.append('')
rate.append('')
len(rate)
for i in range(0,10):
    rate.pop(-1)
len(rate)
################################
#Now let us scrab the review body
review=soup.find_all('div',class_='text')
review
review_body=[]
for i in range(0,len(review)):
    review_body.append(review[i].get_text())
review_body
len(review_body)
###we got 25 review
#now we have to save the data in .csv file
import pandas as pd
df=pd.DataFrame()
df['Review_Title']=review_title
df['Rate']=rate
df['Review']=review_body
df
#to create .csv file
df.to_csv("C:/8-text minning/text_mining/GodFather_reviews.csv")
#############################################
#sentiment analysis
import pandas as pd
from textblob import TextBlob
sent = "This is very excellent garden"
pol = TextBlob(sent).sentiment.polarity
pol
df = pd.read_csv("C:/8-text minning/text_mining/GodFather_reviews.csv")
df.head()
df['polarity']=df['Review'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['polarity']

