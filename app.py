from flask import Flask, render_template, request
from flaskext.mysql import MySQL
from flask_hashing import Hashing

app = Flask(__name__)
mysql = MySQL()
hashing = Hashing(app)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'proftalents'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

connect = mysql.connect()
query = connect.cursor()

@app.route('/signin')
def signin():
    return render_template("signin.html")


@app.route('/signup')
def signup():
    return render_template("signup.html")


@app.route('/signin_post', methods=['POST'])
def signin_post():
    login = request.form['login']
    password = request.form['password']
    pass_hash = hashing.hash_value(password)
    result = query.execute("SELECT * FROM `users` WHERE `login`=%s",(login))

    pass_from_base = query.fetchone()
    if pass_from_base:
        if pass_hash == pass_from_base[1]:
            return "access granted"
        else:
            return "wrong password"
    else:
        return "user not found"


@app.route('/signup_post', methods=['POST'])
def signup_post():
    fist_name = request.form['first_name']
    second_name = request.form['second_name']
    middle_name = request.form['middle_name']
    email = request.form['email']
    birthday = request.form['birthday']
    institution = request.form['institution']
    go_to_stankin = request.form['go_to_stankin']
    personal_information = request.form['personal_information']
    return "ok"

if __name__ == '__main__':
    app.run()
