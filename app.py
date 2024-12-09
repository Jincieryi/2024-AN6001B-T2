#api cannot appear in cloud
from flask import Flask
from flask import render_template,request
import textblob
import google.generativeai as genai
import os

app = Flask("__name__")
#api = "AIzaSyAERZuHDhsmFlFNxeFEq99YCvdBePIQ4d8"
api = os.getenv("makersuite")
genai.configure(api_key=api)
model = genai.GenerativeModel("gemini-1.5-flash")

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
    q = request.form.get("q")
    r = model.generate_content(q)
    return(render_template("genAI_result.html",r=r.candidates[0].content.parts[0].text))

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

