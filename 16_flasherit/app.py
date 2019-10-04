# Jesse Chen & Pratham Rawat
# SoftDev1 pd1
# K16 -- Oh yes, perhaps I do...
# 2019-10-02

from flask import Flask, render_template, session, request, redirect, flash
import os

app = Flask(__name__);

@app.route("/")
def whyTho():
    try:
        username = session["username"]
        print("Username: " + username)
        userpswd = session["password"]
        print("Password: " + userpswd)
        return redirect("/welcome")
    except Exception as e:
        print(e)
        return redirect("/login")

@app.route("/login", methods=['POST', 'GET'])
def logIn():
    global ErrorStatus
    return render_template('start.html')

@app.route("/welcome")
def welcome():
    return render_template('welcome.html')

@app.route("/logout")
def logout():
    session.pop("username")
    session.pop("password")
    return redirect("/")

@app.route("/auth", methods=['POST'])
def authenticate():
    userData = request.form
    print("data: " + str(userData))
    username = userData["username"]
    userpswd = userData["password"]
    users = open("data/accounts.csv");
    accountsDict = {}
    for line in users:
        temp = line.strip().split(',')
        accountsDict[temp[0]] = temp[1]
    try:
        if(accountsDict[username] != userpswd):
#            print(accountsDict[username] + " = " + userpswd)
            print("Incorrect Password")
            flash("Incorrect Password!")
            return redirect("/login")
        else:
            session["username"] = accountsDict[username]
            session["password"] = userpswd
            print(request.cookies)
            return redirect("/welcome")
    except Exception as e: #Will run if the username does not exist in the Dictionary
        print(e)
        print("No username found!")
        flash("Incorrect Username!")
        return redirect("/login")

if __name__ == "__main__":
    app.secret_key = "yeet"
    app.config['SESSION_PERMANENT'] = True
#    app.config['SESSION_TYPE'] = 'memcached'
    app.debug = True
    app.run()
