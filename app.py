from flask import Flask,request,redirect,render_template
from werkzeug.utils import html
from datetime import datetime
from youtube_scraping import youtube_search,picking_title,picking_ids,video_info
#from thread import Article,Thread
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

db_uri = "sqlite:///test.db"
#or os.environ.get('DATABASE_URL') #or "postgresql://localhost/flasknote"
app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
db = SQLAlchemy(app)   

class Article(db.Model):
    #__tablename__ = "articles"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pub_date = db.Column(db.DateTime, nullable=False,
                                default=datetime.utcnow)
    name = db.Column(db.String(80))
    #name = db.Column(db.Text(80))
    article = db.Column(db.Text())
    thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'), nullable=False)

    def __init__(self, pub_date, name, article, thread_id):
        self.pub_date = pub_date
        self.name = name
        self.article = article
        self.thread_id = thread_id


class Thread(db.Model):
    #__tablename__ = "threads"
    id = db.Column(db.Integer, primary_key=True)
    threadname = db.Column(db.String(80), unique=True)
    #threadname = db.Column(db.Text(80), unique=True)
    articles = db.relationship('Article', backref='thread', lazy=True)

    def __init__(self, threadname, articles=[]):
        self.threadname = threadname
        self.articles = articles


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

@app.route("/thread")
def thread():
    title=request.form['value']
    thread_get = request.form["thread"]
    threads = Thread.query.all()
    #articles = Article.query.all()
    thread_list = []
    threads = Thread.query.all()
    for th in threads:
        thread_list.append(th.threadname)
        #print("----" + th.threadname + "----")
    if thread_get in thread_list:
        thread = Thread.query.filter_by(threadname=thread_get).first()
        articles = Article.query.filter_by(thread_id=thread.id).all()
    return render_template(
        "thread.html",
        articles=articles,
        thread=thread_get,
        title=title
    )
#<button type="submit" value="{{video['id']}}">評判・コメント</button>
#<input class="detailbtn" id="{{video[id]}}" type ="submit" value="評判・コメント">
#実行
if __name__=="__main__":
    app.run(host="127.0.0.1",debug=True)