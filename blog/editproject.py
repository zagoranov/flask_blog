from flask import Blueprint, render_template, url_for, redirect, flash, request
from flask_login import login_required, current_user
from . import db
from .models import Project
from .forms import ProjectForm

editproject_bp = Blueprint('editproject_bp', __name__)

@editproject_bp.route('/newproject/', methods=['GET', 'POST'])
@login_required
def create_project():
    projectform = ProjectForm()
    if projectform.validate_on_submit():
        project = Project(title=projectform.title.data, description=projectform.description.data, user_id=current_user.id)
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('/project.html', form=projectform, project_to_update=None)


@editproject_bp.route('/editproject/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_project(id):
    projectform = ProjectForm()
    project = Project.query.filter(Project.id == id).first_or_404()
    if project == None:
        return redirect(url_for('main.index'))
    if projectform.validate_on_submit():
        project.change_project(id, request.form['description'])
        return redirect(url_for('main.index'))
    return render_template('/project.html', form=projectform, project_to_update=project)


@editproject_bp.route('/deleteproject/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_project(id):
    project = Project.query.filter(Project.id == id).first_or_404()
    db.session.delete(project)
    db.session.commit()
    flash("Project deleted")
    return redirect(url_for('main.index'))
