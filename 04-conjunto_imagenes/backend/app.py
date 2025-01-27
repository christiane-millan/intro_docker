from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/getMyInfo')
def getMyInfo():
    value = {
        "name": "Christian",
        "lastname": "Millán",
        "socialMedia":
        {
            "facebookUser": "christiane-millan",
            "instagramUser": "christiane-millan",
            "xUser": "christiane-millan",
            "linkedin": "christiane-millan",
            "githubUser": "christiane-millan"
       }, 
        "blog": "https://christianmillan.com",
        "author": "Christian Millan"
    }
    
    return jsonify(value)

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=5000)
    app.run(port=5001)