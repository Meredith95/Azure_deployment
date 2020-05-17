from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "This is a Flask Web App on Linux and deployed to Azure with Github"
    
