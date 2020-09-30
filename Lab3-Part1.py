from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Email

class NameForm(Form):
    name = StringField('What is your name?', validators=[InputRequired()])
    email = StringField('What is your UofT Email address?', validators=[InputRequired(), Email()])
    submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
moment = Moment(app)
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    session.pop('name', url_for('index'))
    # session.clear()
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if(old_name is not None and old_name != form.name.data):
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        # return redirect(url_for('index'))
        old_email = session.get('email')
        if(old_email is not None and old_email != form.email.data):
            flash('Looks like you have changed your email!')
        session['email'] = form.email.data
        form.name.data = ''
        form.email.data = ''
        # session.pop('name', None)
        return redirect(url_for('index'))

    return render_template('index.html', form=form, name=session.get('name'), email=session.get('email'))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
