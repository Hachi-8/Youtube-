from flask import Flask,request
from youtube_scraping import youtube_search

app = Flask(__name__)
    

#ルーティングの指定　---
@app.route("/")
def index():
    return """
        <html><body>
        <form action = "/search" method ="GET">
          検索:<input type ="text" name="name">
          <input type ="submit" value="検索">
        </form>
        </body></html>
    """

@app.route("/search")
def search():
    name=request.args.get("name")
    search_result=youtube_search(name)
    #if name is None:
    #    name="名無し"
    return """
    <h1>{0}の検索結果</h1>
        <p>
        for sr in search_result.get("items", []):
            print(sr['snippet']['title'])
            print(sr['snippet']['publishedAt'])
        </p>
    """.format(name)


#実行
if __name__=="__main__":
    app.run(host="127.0.0.1")