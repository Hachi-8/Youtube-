#pip install google-api-python-client

from apiclient.discovery import build
import pandas as pd

YOUTUBE_API_KEY = 'AIzaSyBPme7scNi_jfFz5cK9rPoSrX68H5-2G5c'

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

search_response = youtube.search().list(
part='snippet',
#検索したい文字列を指定
q='ボードゲーム',
#視聴回数が多い順に取得
order='viewCount',
type='video',
).execute()


