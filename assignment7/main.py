from flask import Flask,render_template,request,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

#import pymysql
app = Flask(__name__)
#conn = pymysql.connect('localhost','root','','register_db')

@app.route('/')
def index():
    return "Hello MAR"

@app.route('/member')
def member():
    return render_template('member.html')

@app.route('/member',methods=["POST"])
def register():
    return 'xyz';

@app.route('/member2', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/member')
    return render_template('registerFrm.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
