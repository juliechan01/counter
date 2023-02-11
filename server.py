from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = '1998' # set security key for security purposes; has to be a string!

@app.route('/')
def counter():
    if "num" in session:
        session["num"] = session["num"] + 1
    else:
        session["num"] = 0
    return render_template("index.html")

@app.route('/another_route', methods=['POST'])
def two_button():
    if "num" in session:
        session["num"] = session["num"] + 2
    else:
        session["num"] = 0
    return render_template("index.html")

@app.route('/add', methods=['POST'])
def add():
    print(request.form["AddVisits"])
    session["num"] = session["num"] + int(request.form["AddVisits"])
    return render_template("index.html")

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect ('/')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=5500)    # Run the app in debug mode.