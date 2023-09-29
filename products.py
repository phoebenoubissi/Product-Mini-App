from flask import Flask, request, jsonify
from flask_cors import CORS
# Imports the Flask framework, which is used to create the web application, 
# as well as other modules like request for handling HTTP requests and jsonify for converting Python objects to JSON format.

app = Flask(__name__)
#Initializes a Flask web application.
CORS(app)  # Enable CORS for the entire app
#CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080/"}}) #allow all origins from api
# Allow CORS for all routes
#CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})

# Initialize an empty list to store products
products = [
      {
        "id": 1,
        "name": "Product 1",
        "price": 100.00
      },
      {
        "id": 2,
        "name": "Product 2",
        "price": 200.00
      }
    ]
@app.route('/')
def hello():
    return 'Hello, World!'

@app.route("/products", methods=["GET", "POST"])
#This is a decorator that associates the /products URL route with the get_products function.
#  When a request is made to /products, Flask will call this function.
def get_products():
  """Returns a list of products."""

  if request.method == "GET":
    # Get all products

    return jsonify(products)
  elif request.method == "POST":
    # Create a new product
    # Create a new product
        data = request.get_json()  # Get JSON data from the request
        name = data.get("name")
        price = data.get("price")
        # Save the product to the database

  # Here, you should save the new product to your database.
        # You can use a database library like SQLAlchemy to perform this task.

        # For demonstration purposes, let's assume you have a list for storing products.
        new_product = {
            "id": len(products) + 1,  # Generate a unique ID (you may need a better approach in production)
            "name": name,
            "price": price
        }
        products.append(new_product)  # Add the new product to the list

        return jsonify(new_product)  # Return the newly created product and HTTP status code 201 (Created)

if __name__ == "__main__": #ensures that the web server is started only if this script is executed directly (not imported as a module).
  app.run(host="0.0.0.0", port=5000, debug=True) #starts the Flask development web server. The debug=True option enables debugging mode, which is useful during development.


#You can then access the microservice from your web browser by visiting http://localhost:5000/products