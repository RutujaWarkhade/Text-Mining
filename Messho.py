# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 04:14:04 2024

@author: om
"""
#3
"""
we extract the text from meesho website
"""

from bs4 import BeautifulSoup as bs
import requests
link="https://www.meesho.com/happy-customer-review/p/26opw"
page=requests.get(link)
page
page.content
watch = bs(page.content, 'html.parser')
print(watch.prettify())
#we extract the review title
title = watch.find_all('span', class_="sc-eDvSVe gUjMRV Comment__CommentText-sc-1ju5q0e-3 cfdxfJ Comment__CommentText-sc-1ju5q0e-3 cfdxfJ")
title
review_title=[]
for i in range(0,len(title)):
    review_title.append(title[i].get_text())
review_title
review_title[:]=[title.strip('\n') for title in review_title]
review_title
"""
["It's really awesome 👍🏼", 
 'Fabric is good customer happy']
"""
len(review_title)
#total 2 reviews 
rating = watch.find_all('span',class_="sc-eDvSVe laVOtN")
rating
rate=[]
for i in range(0,len(rating)):
    rate.append(rating[i].get_text())
rate
rate[:]=[r.strip('/') for r in rate]
rate
"""
['4.1', '5.0', '5.0']
"""
len(rate)
#3
#we gate 3 rate hence we ave to pop 1
rate.pop(-1)
len(rate)
#now we have to save the data in .csv file
import pandas as pd
df=pd.DataFrame()
df['Review_Title']=review_title
df['Rate']=rate
df
#to create .csv file
df.to_csv("C:/8-text minning/text_mining/Saree(meesho)_reviews.csv")
#############################################
#sentiment analysis
import pandas as pd
from textblob import TextBlob
sent = "It's really awesome 👍🏼"
pol = TextBlob(sent).sentiment.polarity
pol
#1.0
df = pd.read_csv("C:/8-text minning/text_mining/Saree(meesho)_reviews.csv")
df.head()
"""
   Review_Title                  Rate
0  It's really awesome 👍🏼        4.1
1  Fabric is good customer happy  5.0

"""
df['polarity']=df['Review_Title'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['polarity']
"""
0    1.00
1    0.75
Name: polarity, dtype: float64

"""
