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

@blog_aa.route('/', methods=['POST', 'GET'])
def index():
    if session.get('notes') is None:
        session['notes']=[]
    
    if request.method=='POST':
        title=request.form.get('title')
        message=request.form.get('message')
        if session['notes']==[]:
            id=1
        else:
            id= (session['notes'][-1]).get('id')+1
        post = {'title':title,'message':message,'id':id}
        session['notes'].append(post)
    return render_template('index.html', notes=session['notes'])


    

@blog_aa.route('/new-post', methods=['GET', 'POST'])
def new_post():
    return render_template('new_post.html')

@blog_aa.route('/edit-<int:id>', methods=['GET','POST'])
def edit_post(id):
    input_note={}
    notes=session['notes']
    for note in notes:
        if note.get('id')==id:
            title=note.get('title')
            message=note.get('message')
            input_note={'title':title,'message':message,'id':id}
    return render_template('new_post.html', input_note=input_note, notes=session['notes'])
