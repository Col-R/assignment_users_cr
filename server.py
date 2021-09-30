from flask import Flask, render_template, request, session, redirect
# import the class from friend.py
from user import Users
app = Flask(__name__)

@app.route("/")
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template('index.html', users=Users.get_all())

@app.route('/users/new')
def new():
    return render_template('create.html')

@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    Users.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/users')

@app.route('/users/<int:user_id>/edit')
def edit(user_id):
    data = {
    "id": user_id
    }
    user = Users.get(data)
    return render_template('edit.html', user = user )

# @app.route('result')
# def result():

if __name__ == "__main__":
    app.run(debug=True)
