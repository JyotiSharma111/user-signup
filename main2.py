from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('form.html')
    return template.render()

def user_validate(username):
    if len(username)>3 and len(username) < 20 and username!=username.isspace():
        return True
    else:
        return False

def pwd_validate(password):
    if len(password)>3 and len(password) < 20 and password!=password.isspace():
        return True
    else:
        return False
    
def verifypswd_validate(verify_pswd,password):
    if verify_pswd==password:
        return True
    else:
        return False

def email_validate(email):
    if len(email)>3 and len(email) < 20 and email!=email.isspace():
        if email.count('@')==1 and email.count(".")==1:
            return True
        else:
            return False
        
@app.route("/", methods=["POST"])
def validate_form():
    username=request.form["username"]
    password=request.form["password"]
    verify_pswd=request.form["verify_pswd"]
    email=request.form["email"]
    
    usererror=""
    pswderror=""
    verifypswderror=""
    email_error=""
    if  not user_validate(username):
        usererror="Not a valid username"
    if not pwd_validate(password):
        pswderror="Not a valid password"
        password=""
        verify_pswd=""
    if not verifypswd_validate(verify_pswd,password):
        verifypswderror="Passwords doesnt match"
        verify_pswd=""
    if  not email_validate(email):
        email_error="Invalid email address"
        

    if not usererror and not pswderror and not email_error and not verifypswderror:
        return "WELCOME  " + username
    else:
        template = jinja_env.get_template('form.html')
        return template.render(username=username,usererror=usererror,pswderror=pswderror,verifypswderror=verifypswderror,
        email_error=email_error)
if __name__=="__main__":
    app.run(debug=True)



























