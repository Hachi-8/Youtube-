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
    maxResults=1,
    ).execute()

    return json.dumps(search_response["items"],indent=2,ensure_ascii=False)

def picking_title(arg):
    title=[]
    for item in arg.get("items",[]):
        title.append(item["spippet"]["title"])
    return title
