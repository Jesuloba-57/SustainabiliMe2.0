from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route("/")
def L_page():
    return render_template('L_page.html')


@views.route("/about")
def about():
    return render_template('about.html')
