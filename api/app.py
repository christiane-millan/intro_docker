import json
from flask import Flask
app = Flask(__name__)

@app.route('/getMyInfo')
def getMyInfo():
    value = {
        "name": "Christian",
        "lastname": "Millán",
        "socialMedia":
        [
            {"facebookUser": "christiane-millan"},
            {"instagramUser": "christiane-millan"},
            {"xUser": "christiane-millan"},
            {"linkedin": "christiane-millan"},
            {"githubUser": "christiane-millan"}
        ],
        "blog": "https://christianmillan.com",
        "author": "Christian Millan"
    }
    return json.dumps(value)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)