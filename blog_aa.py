#Trabalho de progamação aplicada 2 
##################################
#Professor: Jefferson Santos
# Dupla: Alberto Pinheiro Filho; Ana Carolina Do Valle
#1.Importando as bibliotecas necessárias para executar o programa
from flask import Flask, render_template, request, session
from flask_session import Session

blog_aa = Flask(__name__)

blog_aa.config["SESSION_PERMANENT"] = False
blog_aa.config["SESSION_TYPE"] = "filesystem"

Session(blog_aa)

@blog_aa.route("/", methods=["GET", "POST"])
def index():
    if  session.get("notes") is None:
        session["notes"] = []

    if request.method == "POST":
        title = request.form.get("title")
        session["notes"].append(title)
        note = request.form.get("note")
        session["notes"].append(note)


    return render_template("index.html", notes=session["notes"])

@blog_aa.route("/new_post", methods=["GET", "POST","DEL"])
def new_post():
    if  session.get("notes") is None:
            session["notes"] = []

    if request.method == "POST":
            title = request.form.get("title")
            session["notes"].append(title)
            note = request.form.get("note")
            session["notes"].append(note)
            

    return render_template("new_post.html", notes=session["notes"])
#@blog_aa.route(f"/{note}", methods=["POST","GET"])
#def edit(note):


