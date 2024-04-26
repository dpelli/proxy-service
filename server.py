from flask import Flask, jsonify, request, Response
import requests
from decouple import config
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

API_KEY = config("API_KEY")
BASE_URL = "https://tasty.p.rapidapi.com"


@app.route("/")
def get_recipes_list() -> Response:
    """
    Generates a list of recipes from the Tasty API
    ---
    parameters:
      - name: size
        in: query
        type: string
        required: false
        description: The number of recipes to return
      - name: tags
        in: query
        type: string
        required: false
        description: A tag by which to filter the response
    responses:
      200:
        description: A JSON response from the Proxy Service API
    """

    # Get request query params. If none, set defaults
    size = request.args.get("size", "20")
    tags = request.args.get("tags", "under_30_minutes")

    api_url = f"{BASE_URL}/recipes/list"
    querystring = {"from": "0", "size": size, "tags": tags}
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "tasty.p.rapidapi.com",
    }

    # Make request to Tasty API for recipes fitting the size and tags filters
    response = requests.get(api_url, headers=headers, params=querystring)
    data = response.json()

    # Parse Tasty API response for essential information
    results = [
        {
            "id": idx,
            "tasty_id": result.get("id", ""),
            "name": result.get("name", ""),
            "description": result.get("description", ""),
            "nutrition": result.get("nutrition", ""),
            "num_servings": result.get("num_servings", ""),
            "cook_time_minutes": result.get("cook_time_minutes", ""),
            "user_ratings": result.get("user_ratings", ""),
        }
        for idx, result in enumerate(data.get("results", []), 1)
    ]
    return jsonify({"results": results})


@app.route("/tags")
def get_tags_list() -> Response:
    """
    Generates a list of recipe tags from the Tasty API
    ---
    responses:
      200:
        description: A JSON response from the Proxy Service API
    """

    api_url = f"{BASE_URL}/tags/list"
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "tasty.p.rapidapi.com",
    }

    # Make request to Tasty API for recipe tags
    response = requests.get(api_url, headers=headers)
    data = response.json()

    # Parse Tasty API response for essential information
    results = [
        {
            "name": result.get("name", ""),
        }
        for result in data.get("results", [])
    ]
    return jsonify({"results": results})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
