from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 
import os

app=Flask(__name__)
path= os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///"+os.path.join(path,"db.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")