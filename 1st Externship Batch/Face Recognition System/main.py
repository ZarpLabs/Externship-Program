from flask import Flask, jsonify, request
from Recogniser import FaceIdentify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def recognize():
    # get data
    face = FaceIdentify(precompute_features_file="./features.pickle")
    detected_person = face.detect_face()
    print(detected_person)
    person = max(set(detected_person), key = detected_person.count)
    
    # send back to browser
    output = person

    # return data
    return jsonify(results=output)

if __name__ == '__main__':
    app.run(port = 5000, debug=True)
