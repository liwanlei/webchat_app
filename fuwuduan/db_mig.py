""" 
@author: lileilei
@file: db_mig.py 
@time: 2018/5/27 13:58 
"""
from flask_migrate import Migrate,MigrateCommand
from flask_script import  Manager
from app import db,app
manage=Manager(app)
migrate=Migrate(app,db)
manage.add_command('db',MigrateCommand)
if __name__=='__main__':
    manage.run()