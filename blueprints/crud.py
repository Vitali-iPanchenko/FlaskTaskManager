from flask import Blueprint, render_template, request, redirect, url_for
import operations as op


crud = Blueprint('crud', __name__)


@crud.route('/create', methods=('GET', 'POST'))
def create_task():
    if request.method == 'POST':
        if all([value for value in request.form.values()]):
            tasks = op.show()
            try:
                op.create()
            except ValueError:
                return render_template("create.html",
                                       tasks=tasks)
            else:
                return render_template("create.html",
                                       tasks=tasks)
        else:
            return render_template("create.html")
    else:
        return render_template("create.html")


@crud.post('/<id>/delete')
def delete_task(id):
    op.delete(id)
    return redirect(url_for('task_list.show_all_tasks'))


@crud.route('/<id>/update', methods=('GET', 'POST'))
def update_task(id):
    if request.method == 'POST':
        op.update(id)
    return render_template('update.html', id=id)
