import json
from flask import Flask
application = Flask(__name__)
app=application

#Load static JSON FILE 
account_balance = json.load(open("./Data/account_balance.json"))
print(account_balance["ac001"]["Balance"])

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/user/<uid>" , methods=["GET","POST"])
def get_user_details(uid):
	return json.dumps(account_balance[uid])

if __name__ == "__main__":
    app.run()