# import required packages
from app import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# inti the app
app=Flask(__name__)

# Create a route for flask_hellow
@app.route("/flask_hellow", methods = ["GET"])
def get_flask_hellow_messages():
    return jsonify({"message": "flask_hellow"})

# run server
if__name__= "__main__"
app.run(debug=True)

