from flask import Flask, render_template,  request, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from datetime import datetime
from werkzeug.utils import secure_filename
import json
import os
import math

local_server = True
with open('config.json', 'r') as c:
    params = json.loads(c.read())["params"]

app = Flask(__name__)
app.secret_key = 'secret-key'
app.config['UPLOAD_FOLDER'] = params['upload_location']
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD=  params['gmail-password']
)
mail = Mail(app)
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
db = SQLAlchemy(app)


class Contacts(db.Model):
    '''
    sno, name phone_num, msg, date, email
    '''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)


class Projects(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(21), nullable=False)
    code = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    language = db.Column(db.String(120), nullable=True)


@app.route("/")
def home():
    flash("hello i am jasgun singh")
    projects = Projects.query.filter_by().all()
    # [0:params['no_of_posts']]
    last = math.ceil(len(projects)/int(params['no_of_posts']))
    page = request.args.get('page')
    if(not str(page).isnumeric()):
        page = 1
    page = int(page)
    projects = projects[(page-1)*int(params['no_of_posts']):(page-1)*int(params['no_of_posts'])+int(params['no_of_posts'])]

    if(page==1):
        prev = "#"
        next = "/?page="+ str(page+1)

    elif(page==last):
        prev = "/?page="+ str(page-1)
        next = "#"
    else:
        prev = "/?page="+ str(page-1)
        next = "/?page="+ str(page+1)
        


    
    return render_template('index.html', params=params, projects=projects, prev=prev, next=next)

@app.route("/about")
def about():
    return render_template('about.html', params=params)



@app.route("/uploader", methods=['GET', 'POST'])
def uploader():
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            f = request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            return "Uploaded successfully"






@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    projects = Projects.query.all()
    if ('user' in session and session['user'] == params['admin_user']):
        return render_template('dashboard.html', params=params, projects=projects)

    if request.method=='POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        if (username == params['admin_user'] and userpass == params['admin_password']):
            session['user'] = username
            
            return render_template('dashboard.html', params=params, projects= projects)
    return render_template('login.html', params=params)
    

@app.route("/edit/<string:sno>", methods=['GET', 'POST'])
def edit(sno):
    projects = Projects.query.all()
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            box_title = request.form.get('title')
            language = request.form.get('language')
            slug = request.form.get('slug')
            code = request.form.get('code')
            date = datetime.now()

            if sno=='0':
                post = Projects(title=box_title,slug=slug,code=code,language=language, date=date)
                db.session.add(post)
                db.session.commit()
            else:
                project = Projects.query.filter_by(sno=sno).first()
                project.title=box_title
                project.slug=slug
                project.code=code
                project.language=language
                project.date=date
                db.session.commit()
                # return redirect('/edit/' + sno)
                return redirect('/dashboard')
        project = Projects.query.filter_by(sno=sno).first()
        return render_template('edit.html', params=params, projects= project, sno=sno)




@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/dashboard')

@app.route("/projects/")
def projects():
    projects = Projects.query.filter_by().all()
    # [0:params['no_of_posts']]
    
    last = math.ceil(len(projects)/int(params['no_of_posts']))
    page = request.args.get('page')
    if(not str(page).isnumeric()):
        page = 1
    page = int(page)
    projects = projects[(page-1)*int(params['no_of_posts']):(page-1)*int(params['no_of_posts'])+int(params['no_of_posts'])]

    if(page==1):
        prev = "#"
        next = "/projects/?page="+ str(page+1)

    elif(page==last):
        prev = "/projects/?page="+ str(page-1)
        next = "#"
    else:
        prev = "/projects/?page="+ str(page-1)
        next = "/projects/?page="+ str(page+1)

    return render_template('all_projects.html', params=params, projects=projects, prev=prev, next=next)
    # return render_template('all_projects.html', params=params, projects=projects)

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        entry = Contacts(name=name, phone_num = phone, msg = message, date= datetime.now(),email = email )
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message from ' + name,
                          sender=email,
                          recipients = [params['gmail-user']],
                          body = message + "\n" + phone
                          )

    return render_template('contact.html', params=params)
@app.route("/projects/<string:projects_slug>", methods=['GET'])
def projects_route(projects_slug):
    projects = Projects.query.filter_by(slug=projects_slug).first()
    return render_template('project.html', params=params, projects=projects)

@app.route("/delete/<string:sno>", methods=['GET', 'POST'])
def delete(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        project = Projects.query.filter_by(sno=sno).first()
        db.session.delete(project)
        db.session.commit()
    return redirect('/dashboard')


app.run(debug=True)
