from bson.objectid import ObjectId
from flask import request, g


def create():
    content = request.form['Content']
    deadline = request.form['Deadline']
    return g.mongo_client.tasks.insert_one({'Content': content, 'Deadline': deadline})


def delete(id):
    return g.mongo_client.tasks.delete_one({"_id": ObjectId(id)})


def show():
    return g.mongo_client.tasks.find()


def update(id):
    new_content = request.form['New_Content']
    new_deadline = request.form['New_Deadline']
    return g.mongo_client.tasks.update_one({'_id': ObjectId(id)},
                                           {'$set': {'Content': new_content,
                                                     'Deadline': new_deadline}})
