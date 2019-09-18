# Jesse Chen
# SoftDev1 pd1
# K8 -- Lemme Flask You Sump'n
# 2019-09-18



from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when root route requested
def hello_world():
    print(__name__) #where will this go?
    return "No hablo queso!"

@app.route("/a") #assign following fxn to run when root route requested
def hello_worldA():
    print(__name__) #where will this go?
    return "Route A"

@app.route("/b") #assign following fxn to run when root route requested
def hello_worldB():
    print(__name__) #where will this go?
    return "Route B"

@app.route("/c") #assign following fxn to run when root route requested
def hello_worldC():
    print(__name__) #where will this go?
    return "Route C"

if __name__ == "__main__":
    app.debug = True
    app.run()
