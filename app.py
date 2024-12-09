#api cannot appear in cloud
from flask import Flask
from flask import render_template,request
import textblob
import google.generativeai as genai

app = Flask("__name__")
@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    name = request.form.get("q")
    return(render_template("main.html"))

@app.route("/GenAI",methods=["GET","POST"])
def GenAI():
    return(render_template("GenAI.html"))

@app.route("/GenAI_result",methods=["GET","POST"])
def GenAI_result():
    api1='AIzaSyAMy8gbF-lF5OZqcfVhxJPGhBKQvQEE3dU'
    genai.configure(api_key=api1)
    model=genai.GenerativeModel("gemini-1.5-flash")
    q = request.form.get("q")
    r=model.generate_content(q)
    r=r.candidates[0].content.parts[0].text
    return(render_template("GenAI_result.html",r=r))#第一个r是从html读取的，第二个r是python的

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

