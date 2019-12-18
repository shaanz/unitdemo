import json
from flask import Flask
application = Flask(__name__)
app=application

#Load static JSON FILE 
user_data = json.load(open("./Data/user.json"))
print(user_data["ac001"]["age"])

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/user/<uid>/details/" , methods=["GET","POST"])
def get_user_details(uid):
	return json.dumps(user_data[uid])

if __name__ == "__main__":
    app.run()