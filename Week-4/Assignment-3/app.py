from flask import Flask, render_template, url_for, redirect, flash
from forms import RegisterForm, LoginForm
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user

import pymysql

app = Flask(__name__)
app.config['SECRET_KEY'] = "sdljfaieaw'i'l;l3329pdoasiof"

conn = pymysql.connect(host = 'localhost', 
                            port=3306, 
                            user='root', 
                            passwd='1019', 
                            charset='utf8', 
                            db='assignment')

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = "login"

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods = ["POST","GET"])
def register():
    form = RegisterForm()
        
    if form.validate_on_submit():
        email_data = form.email.data
        password_data = form.password.data

        try:
            with conn.cursor() as cursor:
                # check if the email is registered
                sql = "SELECT * FROM user WHERE email = %s"
                cursor.execute(sql, (email_data,))
                existing_user = cursor.fetchone()

                if existing_user:
                    flash("Email already registered.")
                else:
                    sql = "INSERT INTO user (email, password) VALUES(%s,%s)"
                    cursor.execute(sql, (email_data, password_data))
                    conn.commit()
                    return redirect(url_for("login"))
        except:
            flash("Please try again.")


           
    return render_template("register.html",form=form)


@app.route('/login', methods = ["POST","GET"])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        email_data = form.email.data
        password_data = form.password.data

        try:
            with conn.cursor() as cursor:
                # check if the email is in database
                sql = "SELECT * FROM user WHERE email = %s AND password = %s"
                cursor.execute(sql, (email_data,password_data))
                user_in_db = cursor.fetchone()

                if user_in_db:
                    return redirect(url_for("welcome"))
                else:
                    flash("Invalid email or password.")
        except:
            flash("Please try again.")
    
    return render_template("login.html",form=form)


@app.route('/welcome')
def welcome():
    return render_template('member.html')


if __name__ == "__main__":
    app.run(debug=True, host="localhost",port=4000)
