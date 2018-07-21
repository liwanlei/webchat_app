""" 
@author: lileilei
@file: __init__.py.py 
@time: 2018/5/26 20:35 
"""
from flask import  Flask
import  os
from flask_sqlalchemy import  SQLAlchemy
from config import  mysql
app=Flask(__name__)
SECRET_KEY = 'BaSeQuie'
app.config.from_object(mysql())
db=SQLAlchemy(app)
from  app import views,model,url
