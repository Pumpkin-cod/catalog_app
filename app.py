from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# MySQL connection string format:
# mysql+pymysql://username:password@hostname/database_name
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://catalog_user:catalog_pass@localhost/catalog"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Recommended to avoid warnings

db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__ = 'products'  # Fixed: double underscores
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)

@app.route("/products", methods=["GET"])
def get_products():
    try:
        products = Product.query.all()
        return jsonify([{
            "id": p.id, 
            "name": p.name, 
            "description": p.description, 
            "price": p.price
        } for p in products])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":  # Fixed: double underscores
    app.run(host="0.0.0.0", port=5000, debug=True)
