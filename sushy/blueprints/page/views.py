from flask import Blueprint, render_template

page = Blueprint('page', __name__, template_folder='templates')


@page.route('/')
def home():
    return render_template('page/home.j2')


@page.route('/terms')
def terms():
    return render_template('page/terms.j2')


@page.route('/privacy')
def privacy():
    return render_template('page/privacy.j2')
