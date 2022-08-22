from flask import Flask, g
import pymongo
from blueprints.main_page import task_list
from blueprints.crud import crud


app = Flask(__name__)
app.register_blueprint(task_list)
app.register_blueprint(crud)


app.config['PYMONGO_SETTINGS'] = {'db': 'task_manager',
                                  'host': 'localhost',
                                  'port': 27017,
                                  'connect': False,
                                  }


@app.before_request
def init_globals():
    settings = app.config['PYMONGO_SETTINGS']
    pyconn = pymongo.MongoClient(host=settings['host'], port=settings['port'], connect=False)
    g.mongo_client = pyconn[settings['db']]


if __name__ == '__main__':
    app.run()
