#pip install google-api-python-client

from apiclient.discovery import build
import pandas as pd
import json

def youtube_search(word):
    YOUTUBE_API_KEY = 'AIzaSyBPme7scNi_jfFz5cK9rPoSrX68H5-2G5c'
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'
    
    youtube = build(
        YOUTUBE_API_SERVICE_NAME, 
        YOUTUBE_API_VERSION, 
        developerKey=YOUTUBE_API_KEY
        )

    search_response = youtube.search().list(
    part='snippet',
    #検索したいワードの指定
    q=word,
    #視聴回数が多い順に取得
    order='viewCount',
    type='video',
    maxResults=20,
    ).execute()

    return search_response

def picking_title(arg):
    titles=[]
    for item in arg["items"]:
        titles.append(item["snippet"]["title"])
    return titles

def picking_viewcount(arg):
    viewcounts=[]
    for item in arg["statistics"]:
        viewcounts.append(item["viewcount"])
    return viewcounts

def picking_ids(arg):
    ids=[]
    for item in arg["items"]:
        ids.append("https://www.youtube.com/watch?v="+item["id"]["videoId"])
    return ids