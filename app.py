from flask import Flask,request,redirect,render_template
from youtube_scraping import youtube_search,picking_title,picking_ids,video_info

app = Flask(__name__)
    

#ルーティングの指定　---
@app.route("/")
def index(): 
    return """
        <html>
        <style>
           form{
                text-align: center;
           } 
           input.searchword{
               width:24%;
               height:30px;
           }
           input.searchbtn{
               height:30px;
           }
        </style>
        <body>
        <form action = "/search" method ="GET">
          <h1>Youtube Search</h1>
          <input class="searchword" type ="text" name="name">
          <input class="searchbtn" type ="submit" value="検索">
        </form>
        </body></html>
    """

@app.route("/search")
def search():
    name=request.args.get("name")
    search_result=youtube_search(name)
    search_result_titles=picking_title(search_result)
    search_result_ids=picking_ids(search_result)
    len_titles=len(search_result_titles)

    videos=video_info(search_result_ids)
    if name==None:
        return redirect("/")
    else:
        #titles=[]
        #for item in search_result["items"]:
        #    titles.append(item["snippet"]["title"])
        return render_template(
            "search_result.html",
            titles=search_result_titles,
            name=name,
            ids=search_result_ids,
            range_len_titles=range(len_titles),
            videos=videos
        )
        #return """
        #<h1>{0}の検索結果</h1>
        #    <p>{1}</p>
        #    <p>{2}</p>
        #    <p>{3}</p>
        #""".format(name,search_result,titles,search_result_titles)


#実行
if __name__=="__main__":
    app.run(host="127.0.0.1",debug=True)