from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend requests from browser (JS fetch)

# Configurations
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://catalog_user:catalog_pass@localhost/catalog"
app.config["JWT_SECRET_KEY"] = "super-secret-key"

# Init DB and JWT
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Dummy login credentials
USERS = {
    "admin": "password123"
}

# Product model
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)

# ---------------------------
# ROUTES
# ---------------------------

# Login Page UI
@app.route("/", methods=["GET"])
def home():
    return render_template("login.html")  # Ensure templates/login.html exists

# Login API (POST)
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    if username in USERS and USERS[username] == password:
        token = create_access_token(identity=username)
        return jsonify(access_token=token), 200
    return jsonify({"msg": "Invalid credentials"}), 401

# 🔓 Public route to serve the HTML page
@app.route("/products-page", methods=["GET"])
def products_page():
    return render_template("products.html")

# Products UI Page
@app.route("/products", methods=["GET"])
@jwt_required()
def get_products():
    products = Product.query.all()
    return jsonify([
        {
            "id": p.id,
            "name": p.name,
            "description": p.description,
            "price": p.price
        } for p in products
    ])

# ---------------------------
# Run the server
# ---------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

