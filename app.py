from flask import Flask, request,jsonify,redirect
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)

import config
import openai
openai.api_key=config.API_KEY
question="hola"
@app.route("/send",methods=['POST'])
@cross_origin()

def who():
    question=request.json["question"]
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=1024,
        n=1,
        stop= None,
        temperature=0.8
    )
    return jsonify(response)

@app.route("/details",methods=['GET'])
@cross_origin()

def alo():
    return question

if __name__=="__main__":
    app.run()