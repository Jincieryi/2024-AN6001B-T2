from flask import Flask
from flask import render_template,request
import textblob

app = Flask("__name__")
@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    name = request.form.get("q")
    return(render_template("main.html"))

@app.route("/SA",methods=["GET","POST"])
def SA():
    return(render_template("SA.html"))

@app.route("/SA_result",methods=["GET","POST"])
def SA_result():
    q = request.form.get("q")#第一个q是python的，第二个q是从html读取的
    r = textblob.TextBlob(q).sentiment
    return(render_template("SA_result.html",r=r))#第一个r是从html读取的，第二个r是python的

if __name__ == "__main__":
    app.run()

