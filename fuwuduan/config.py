""" 
@author: lileilei
@file: config.py 
@time: 2018/5/26 20:36 
"""
import  os
selseid='979e06170cfea866e7227cf39efcf246'
appid='wx585cd68238de42a5'
class mysql():
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "shop.db")
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False