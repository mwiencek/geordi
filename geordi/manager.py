from flask.ext.script import Manager
from geordi import create_app
from geordi.data import model
from geordi.data.manage import data_manager

manager = Manager(create_app)
manager.add_option('-l', '--log-debug', dest='log_debug', required=False, action='store_true')
manager.add_option('-s', '--log-sql', dest='log_sql', required=False, action='store_true')

manager.add_command('data', data_manager)

@manager.command
def create_tables():
    model.create_tables(manager.app)

if __name__ == "__main__":
    manager.run()
