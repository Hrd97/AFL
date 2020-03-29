import os 
from app import create_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.model import *

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    #交互环境用
    manager.run()
    #app.run()

#运行程序用
