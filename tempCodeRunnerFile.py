@app.route('/login',methods = ["GET", "POST"])
def logIn():
    if request.method == "POST":
        return do_the_login()
    else:
        print("Show the Login Page")
        return render_template('login.html')