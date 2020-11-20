from flask import Blueprint, render_template

page = Blueprint('page', __name__, template_folder='templates')


@page.route('/')
def home():
    return render_template('page/home.jj')


@page.route('/terms')
def terms():
    return render_template('page/terms.jj')


@page.route('/privacy')
def privacy():
    return render_template('page/privacy.jj')
