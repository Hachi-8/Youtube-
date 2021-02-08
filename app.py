from flask import Flask,request,redirect,render_template
from werkzeug.utils import html
from youtube_scraping import youtube_search,picking_title,picking_ids,video_info
from flask_sqlalchemy import SQLAlchemy
from Youtube_portal import app
from thread import Article,Thread



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
               height:25px;
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
        return render_template(
            "search_result.html",
            titles=search_result_titles,
            name=name,
            ids=search_result_ids,
            range_len_titles=range(len_titles),
            videos=videos
        )

@app.route("/thread", methods=["GET"])
def thread():
    title=request.args.get('value')
    thread_get = request.args.get('value') #request.form["value"]
    threads = Thread.query.all()
    #articles = Article.query.all()
    thread_list = []

    for th in threads:
        thread_list.append(th.threadname)

    if thread_get in thread_list:
        thread = Thread.query.filter_by(threadname=thread_get).first()
        articles = Article.query.filter_by(thread_id=thread.id).all()
        return render_template(
            "thread.html",
            articles=articles,
            thread=thread_get,
            title=title
        )

    else:
        thread_new = Thread(thread_get)
        db.session.add(thread_new)
        db.session.commit()
        articles = Article.query.filter_by(thread_id=thread_new.id).all()
        return render_template(
            "thread.html",
            articles=articles,
            thread=thread_get,
            title=title
        )

@app.route("/result", methods=["POST"])
def result():
    date = datetime.now()
    article = request.form["article"]
    name = request.form["name"]
    thread = request.form["thread"]
    #print(article)
    #print(name)
    #print("------------------------------------------------------------")
    #print(thread)
    #print("------------------------------------------------------------")
    thread = Thread.query.filter_by(threadname=thread).first()
    #print(thread)
    #print("------------------------------------------------------------")
    admin = Article(pub_date=date, name=name, article=article, thread_id=thread.id)
    db.session.add(admin)
    db.session.commit()
    return render_template("result.html", article=article, name=name, now=date)

#<button type="submit" value="{{video['id']}}">評判・コメント</button>
#<input class="detailbtn" id="{{video[id]}}" type ="submit" value="評判・コメント">
#実行
if __name__=="__main__":
    app.run()