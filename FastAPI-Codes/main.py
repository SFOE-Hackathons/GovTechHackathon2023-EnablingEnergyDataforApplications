# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 15:31:56 2023

@author: U80827488
"""

from fastapi import FastAPI
import pandas as pd
import requests, urllib3
import io

 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
app = FastAPI()

def load_csv(url):
    proxies = {
          "http":'http://proxy-bvcol.admin.ch:8080',
          "https":'http://proxy-bvcol.admin.ch:8080'
        }
    s = requests.get(url, proxies = proxies, verify = False).text
    df = pd.read_csv(io.StringIO(s))
    df2=df.head(5)
    df1=df2.T
    return df1



@app.get("/fuellstandGasspeicher")
# async def index():
#     return {"message": "Hallo Welt!"}
def get_ogd102():   
    url = 'https://bfe-energy-dashboard-ogd.s3.amazonaws.com/ogd102_fuellstand_gasspeicher.csv'
    df = load_csv(url)
    return {'datasource': url}, {'data': df}, 200  # return data and 200 OK code



@app.get("/stromverbrauch")
# async def index():
#     return {"message": "Hallo Welt!"}
def get_ogd103():   
    url = 'https://bfe-energy-dashboard-ogd.s3.amazonaws.com/ogd103_stromverbrauch_geschaetzt_swissgrid.csv'
    df = load_csv(url)
    return {'datasource': url}, {'data': df}, 200  # return data and 200 OK code