from flask import (Flask, render_template, request, 
                   url_for, redirect, make_response)

app = Flask(__name__)

# Assignment-1
@app.route("/")
def index():
    return render_template("index.html")

# Assignment-2
@app.route("/data")
def value(number=0):
    number = request.args.get("number")
    
    if number is None:
        return "Lack of Parameter"
    else: 
        try: 
            sum = (1 + number) * number / 2
            return f"total: {sum}"
        except:
            return "Wrong Parameter"

# Assignment-3
@app.route("/sum.html")
def sum():
    return render_template("sum.html")

# Assignment-4
@app.route("/myName", methods = ["GET","POST"])
def enterpage():
    user_data = request.cookies.get("user_name")
    
    if user_data:
        return f"Hello {user_data}, I have set your cookies!"
    else:
        return render_template("enterpage.html")

@app.route("/trackname", methods = ["GET","POST"])
def trackname():
    user_data = request.args.get("name")
    
    if user_data:
        response = make_response(redirect(url_for("enterpage")))
        response.set_cookie("user_name",user_data)
        return response
    else:
        return "Input Error!"
    
if __name__ == "__main__":
    app.run(debug=True, host="localhost",port=3000)