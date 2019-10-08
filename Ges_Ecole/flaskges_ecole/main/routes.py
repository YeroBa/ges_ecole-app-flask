from flask import render_template, request, Blueprint, redirect, url_for


main = Blueprint('main', __name__)

@main.route('/')
def home():
    return redirect(url_for('users.login'))

@main.route('/dashbord')
def dashbord():
    return render_template('pages/dashbord.html', title='Dashbord')
