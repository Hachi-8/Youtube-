from flask import Flask,request

def create_app():
    app = Flask(__name__)
    return app

#ルーティングの指定　---
@app.route("/")
def index():
    return """
        <html><body>
        <form action = "/hello" method ="GET">
          名前:<input type ="text" name="name">
          <input type ="submit" value="送信">
        </form>
        </body></html>
    """

@app.route("/hello")
def hello():
    name=request.args.get("name")
    if name is None:
        name="名無し"
    return """
    <h1>{0}さん、こんにちは！</h1>
    """.format(name)


#実行
if __name__=="__main__":
    app.run(host="127.0.0.1")