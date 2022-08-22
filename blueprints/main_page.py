from flask import Blueprint, render_template
import operations as op


task_list = Blueprint('task_list', __name__)


@task_list.route('/', methods=('GET', 'POST'))
def show_all_tasks():
    tasks = op.show()
    list_of_tasks = list(tasks)
    for dictionary in list_of_tasks:
        dictionary['id'] = dictionary['_id']
        del dictionary['_id']
    return render_template("main_page.html", tasks=list_of_tasks)
