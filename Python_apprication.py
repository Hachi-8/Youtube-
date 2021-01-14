from flask import Flask,request,redirect
from youtube_scraping import youtube_search,picking_title

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
    search_result_title=picking_title(search_result)
    if name==None:
        return redirect("/")
    else:
        return """
        <h1>{0}の検索結果</h1>
            <p>{1}</p>
        """.format(name,search_result_title)


#実行
if __name__=="__main__":
    app.run(host="127.0.0.1")