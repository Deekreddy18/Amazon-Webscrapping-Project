#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Amazon webscrapping Project using Python
#Importing Libraries

from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib


# In[17]:


# Connect to Website and pull in data

URL = 'https://www.amazon.com/SS-Kashmir-Leather-Exclusive-Protection/dp/B071787MKT/ref=sr_1_3?crid=2BG7MSI1ZMF7B&keywords=cricket+bats&qid=1688677133&sprefix=cricket+bats%2Caps%2C103&sr=8-3'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-64a72932-74ff2e5d0628e89b0e77c594"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

print(soup1)


# In[24]:


title = soup2.find(id='ProductTitle')

price = soup2.find(id='price')


# In[25]:


import datetime

today = datetime.date.today()

print(today)


# In[26]:



import csv 

header = ['Title', 'Price', 'Date']
data = [title, price, today]

#Creating and appending data into csv file
with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[29]:




with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[30]:


#ceating a function for price check
def check_price():
    URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()

    price = soup2.find(id='priceblock_ourprice').get_text()

    price = price.strip()[1:]
    title = title.strip()

    import datetime

    today = datetime.date.today()
    
    import csv 

    header = ['Title', 'Price', 'Date']
    data = [title, price, today]

    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
 


# In[ ]:


while(True):
    check_price()
    time.sleep(86400)


# In[32]:


#Creatin a mail function to generate mail regardin product prices
def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('AlexTheAnalyst95@gmail.com','xxxxxxxxxxxxxx')
    
    subject = "The Shirt you want is below $15! Now is your chance to buy!"
    body = "Alex, This is the moment we have been waiting for. Now is your chance to pick up the shirt of your dreams. Don't mess it up! Link here: https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data+analyst+tshirt&qid=1626655184&sr=8-3"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'AlexTheAnalyst95@gmail.com',
        msg
     
    )

