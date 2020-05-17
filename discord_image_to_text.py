from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from bs4 import BeautifulSoup
import json
from requests import get
import time
import os
import sys
import random
import re
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from imagetotext import *
from env import *

def getVariables(channel_name):
 
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    #
    # use headless browser.
    #

    driver = webdriver.Firefox(firefox_options=options)

    #
    # use firefox browser.
    #

    # driver = webdriver.Firefox()

    #
    # Grab configuration settings
    #
    email = Connection['EMAIL']
    password = Connection['PASSWORD']
    print(CHA)
    try:
        ptr = CHA[channel_name]
    except:
        return None
    channel = ptr['CHANNEL']
    guild = ptr['GUILD']
    query = ptr['variable_list']
    print(query)
    url = "https://discord.com/login"
    driver.get(url) 

    #
    #Login into the account
    #
    while True:
        try:
            email_el = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/input')
            pass_el = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input')
            login_butt = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]')

            email_el.send_keys(email)
            pass_el.send_keys(password)

            login_butt.click()
            break
        except:
            time.sleep(1)

    #
    # Wait until finish rendering page.
    #
    try:
        myElem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
        print ("Page is ready!")
    except TimeoutException:
        pass

    #
    # Go to given channel and guild, get images' urls.
    #
    channel_url = 'https://discord.com/channels/' + channel + '/' + guild
    driver.get(channel_url)
    while True:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        items = soup.find_all('a',{'class':'anchor-3Z-8Bb anchorUnderlineOnHover-2ESHQB imageWrapper-2p5ogY imageZoom-1n-ADA clickable-3Ya1ho embedWrapper-lXpS3L'})
        if (len(items)>0):
            break
        else:
            time.sleep(1)

    image_urls = []

    #
    # Get latest image and convert into text.
    #
    for it in items:
        url = it['href']
        ptrarr = url.split('/')
        daytimestr = ptrarr[len(ptrarr)-1].split('.')[0]
        image_urls.append([daytimestr, it['href']])
    latestimgurl = image_urls[len(image_urls)-1][1]
    latestimg_data = get(latestimgurl).content
    with open('data/ptr.png', 'wb') as handler:
        handler.write(latestimg_data)
    latesttext = get_string('data/ptr.png')

    #
    # a function to get string according to setting request
    #
    def get_cleanstring(string):
        resl = None
        try:
            resl = string.decode('utf-8')
        except:
            try:
                resl = string.decode('ascii')
            except:
                resl = string
        return resl
    def find_str(strl, substr):
        if(len(substr.strip())==0):
            return get_cleanstring(strl)
        sea = re.search(substr, strl)
        if (sea):
            loc = sea.span()
            i = loc[1]
            sub = ''
            while(i<len(strl) and strl[i]!=' ' and strl[i]!='\n'):
                sub += strl[i]
                i += 1
            return get_cleanstring(sub)
        return None

    #
    # Get a dictionary from the lates text according the setting.
    #
    result = {}
    for it in query:
        key = it['variable']
        querystr = it['texttosearch']
        val = find_str(latesttext,querystr)
        result[key] =val

    print(result)
    driver.close()
    return result

