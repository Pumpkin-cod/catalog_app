from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required
from auth import auth_bp  # Import blueprint

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://catalog_user:catalog_pass@localhost/catalog"
app.config["JWT_SECRET_KEY"] = "super-secret-key"

db = SQLAlchemy(app)
jwt = JWTManager(app)

# Register the auth blueprint
app.register_blueprint(auth_bp)

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)

@app.route("/products", methods=["GET"])
@jwt_required()
def get_products():
    products = Product.query.all()
    return jsonify([
        {"id": p.id, "name": p.name, "description": p.description, "price": p.price}
        for p in products
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

