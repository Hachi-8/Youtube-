#pip install google-api-python-client

from apiclient.discovery import build
from flask import current_app
import requests
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

def video_info(video_ids):
    video_url = "https://www.googleapis.com/youtube/v3/videos"


    YOUTUBE_API_KEY = 'AIzaSyBPme7scNi_jfFz5cK9rPoSrX68H5-2G5c'
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'
    
    youtube = build(
        YOUTUBE_API_SERVICE_NAME, 
        YOUTUBE_API_VERSION, 
        developerKey=YOUTUBE_API_KEY
        )

    r = youtube.videos().list(
    key = " YOUTUBE_API_KEY ",
    id = ",".join(video_ids),
    part = "snippet,contentDetails",
    maxResult = 20    
    )

    video_params = {
        "key" : " YOUTUBE_API_KEY ",
        "id" : ",".join(video_ids),
        "part" : "snippet,contentDetails",
        "maxResult" : 20
    }
    
    #r = requests.get(video_url, params=video_params)
    results = r.json()["items"]
    videos=[]
    for result in results:
        video_data = {
            "id" : results["id"],
            "url" : f'https://www.youtube.com/watch?v={ result["id"] }',
            "thumnail" : result["thumnails"]["high"]["url"],
            "duration" : result["contentDetails"]["duration"],
            "title" : result["snippet"]["title"]
        } 
        videos.append(video_data)
    return videos

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
        ids.append(item["id"]["videoId"])
    return ids