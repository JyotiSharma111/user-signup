from flask import Flask,request

app = Flask(__name__)

form = """
    <!doctype html>
    <head>
    <style>
        .error{{color:red;}}
        </style>
       
        </head>
        <body>
        <h1>Sign up</h1>
            <form action="/signup" method="post">
            <table>
            <tr><td>
            <label for="username">Username
                <input type="text" name="username"></label>
                <span class="error">{usererror}</span>
            <tr><td>
                <label for="password">Password</label>
                <input type="password" name="password">
                <span class="error">{pswderror}</span>
            <tr><td>
                <label for="verify_pswd">Verify password</label>
                <input type="password" name="verify_pswd">
                <span class="error">{verifypswderror}</span>
            <tr><td>
                <label for="email">Email optional</label>
                <input type="text" name="email"><br>
            <tr><td>
                <input type="submit">
            </form>
        </body>
    </head> 
"""

@app.route("/")
def index():
    return form

def check_Space(t):
    for i in t:
        if i==" ":
            return False
            

@app.route("/signup", methods=["POST"])
def signup():
    username=request.form["username"]
    password=request.form["password"]
    verify_pswd=request.form["verify_pswd"]
    usererror=" "
    pswderror=" "
    verifypswderror=" "
    if username=="" or password=="" or verify_pswd=="":
        return form.format(usererror="this is not valid username",pswderror="this is not valid password",
        verifypswderror="passwords dont match")
    
    if not password==verify_pswd:
            return form.format(usererror="",pswderror="",verifypswderror="passwords dont match")
    if  check_Space(username) or  check_Space(password):
                 return form.format(usererror="contains a space",pswderror="contains a space",verifypswderror="" )
  
    


if __name__=="__main__":
    app.run(debug=True)



























