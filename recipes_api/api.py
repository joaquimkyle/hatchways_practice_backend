from flask import Flask, json, request
from flask_restful import Api, Resource
from .constants import DATAFILE, RECIPES_ENDPOINT, RECIPE_DETAILS_ENDPOINT

data = {}
datafilePath = ""

class RecipesResource(Resource):
    """
    RecipesResource GET method. Retrieves names of all recipes found in the datafile.
    
    :return: JSON, 200 HTTP status code
    """
    def get(self):
        recipeList = []
        for i in data['recipes']:
            recipeList.append(i['name'])
        resp = {
            "recipeNames": recipeList
        }
        return resp, 200
        
    def post(self):
        body = request.get_json(force=True)
        recipeList = []
        for i in data['recipes']:
            recipeList.append(i['name'])
        if body['name'] in recipeList:
            resp = {
                "error" : "Recipe already exists"
            }
            return resp, 400
        else:
            data['recipes'].append(body)
            with open(datafilePath, 'w') as f:
                json.dump(data, f, sort_keys = False, indent = 2, ensure_ascii = False)
            return '', 201
            
    def put(self):
        body = request.get_json(force=True)
        for i in data['recipes']:
            if i['name'] == body['name']:
                i['ingredients'] = body['ingredients']
                i['instructions'] = body['instructions']
                with open(datafilePath, 'w') as f:
                    json.dump(data, f, sort_keys = False, indent = 2, ensure_ascii = False)
                return '', 204
   
        resp = {
            "error" : "Recipe does not exist"
        }
        return resp, 404
        
class RecipeDetailsResource(Resource):
    def get(self, recipeName):
        resp = {}
        for i in data['recipes']:
            if i['name'] == recipeName:
                resp = {
                    "details": {
                        "ingredients" : i['ingredients'],
                        "numSteps" : len(i['ingredients'])
                    }
                }
        return resp, 200
    
def create_app(datafile):
    
    app = Flask(__name__)
    global data
    global datafilePath
    datafilePath = datafile
    with open(datafile) as f:
        data = json.load(f)
    
    api = Api(app)
    api.add_resource(RecipesResource, RECIPES_ENDPOINT)
    api.add_resource(RecipeDetailsResource, f"{RECIPE_DETAILS_ENDPOINT}<string:recipeName>") 
    return app
    
if __name__ == "__main__":
    app = create_app(DATAFILE)
    app.run(debug=True)