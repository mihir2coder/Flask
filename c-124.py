import numbers
from flask import Flask, jsonify

Contacts=[
{"Name":"Zohair","Num":"12345678"},{"Name":"Mihir","Num":"87654321"}
]
app=Flask(__name__)


@app.route("/") #takes to normal ip adress
def first():
    return "Home.."


@app.route("/Welcome")
def WelcomeToFlask():
    return jsonify({"data":Contacts})

@app.route("/Post")
def Post():
    c1={"Name":"Putin","Num":"911"}
    Contacts.append(c1)
    return jsonify({"data":Contacts})


if __name__=="__main__":
    app.run(debug=True)

