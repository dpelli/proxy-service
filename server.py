from flask import Flask, jsonify
import requests
from decouple import config
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

API_KEY = config("API_KEY")
BASE_URL = "https://tasty.p.rapidapi.com"


@app.route("/")
def get_recipes_list():
    """
    Generates a list of recipes
    ---
    responses:
      200:
        description: A JSON response from the Proxy Service API
    """
    api_url = f"{BASE_URL}/recipes/list"
    querystring = {"from": "0", "size": "20", "tags": "under_30_minutes"}
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "tasty.p.rapidapi.com",
    }
    response = requests.get(api_url, headers=headers, params=querystring)
    data = response.json()
    results = [
        {
            "id": result["id"],
            "name": result["name"],
            "description": result["description"],
            "nutrition": result["nutrition"],
            "num_servings": result["num_servings"],
            "cook_time_minutes": result["cook_time_minutes"],
            "user_ratings": result["user_ratings"],
        }
        for result in data["results"]
    ]
    return jsonify({"results": results})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
