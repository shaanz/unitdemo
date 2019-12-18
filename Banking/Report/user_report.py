import json, requests
from flask import Flask
application = Flask(__name__)
app=application

#Load static JSON FILE 




@app.route("/")
def hello():
    return "Hello World!"

@app.route("/user/<uid>" , methods=["GET","POST"])
def get_user_report(uid):
   url_user = "http://localhost:8080/user/"+uid+"/details"
   url_bal = "http://localhost:8081/user/"+uid
   
   user_service= requests.get(url_user)
   print(user_service.json())
   account_balance = requests.get(url_bal)
   print(account_balance.json())
   
   rep_json = "{" + uid + ":" + json.dumps(user_service.json()) +","+ json.dumps(account_balance.json()) +"}"
   return rep_json

if __name__ == "__main__":
    app.run()