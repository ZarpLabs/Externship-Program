from recommendation_system import item_based_recommender
from flask import Flask, request, jsonify

item_recommender = item_based_recommender()

app = Flask(__name__)

@app.route('/', methods=['POST'])
def my_form():
    user = request.get_json(force = True)
    personal = item_recommender.personalized_recommendation(user)
    return jsonify(results = personal)

if __name__ == '__main__':
    app.run(port = 5000, debug=True)