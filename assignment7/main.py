from flask import Flask,render_template,request,redirect,url_for
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

if __name__ == '__main__':
    app.run(debug=True)
