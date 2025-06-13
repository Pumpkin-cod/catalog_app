# Product Catalog API

A simple Flask-based REST API for managing product catalog data with MySQL database backend.

## Features

- Retrieve all products via REST API
- JSON response format
- MySQL database integration
- Error handling and health checks

## Requirements

- Python 3.8+
- MySQL 5.7+
- Flask
- Flask-SQLAlchemy
- PyMySQL

## Installation

1. **Clone or download the project files**

2. **Install Python dependencies:**
   ```bash
   pip install flask flask-sqlalchemy pymysql
   ```

3. **Set up MySQL database:**
   ```sql
   CREATE DATABASE catalog;
   CREATE USER '<username>'@'localhost' IDENTIFIED BY '<password>';
   GRANT ALL PRIVILEGES ON catalog.* TO '<username>'@'localhost';
   FLUSH PRIVILEGES;
   ```

4. **Create the products table:**
   ```sql
   USE catalog;
   CREATE TABLE products (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255) NOT NULL,
       description TEXT,
       price FLOAT NOT NULL
   );
   ```

5. **Add sample data (optional):**
   ```sql
   INSERT INTO products (name, description, price) VALUES 
   ('Laptop', 'A high-end laptop', 1200.0),
   ('Phone', 'Latest smartphone', 800.0);
   ```

## Usage

1. **Start the application:**
   ```bash
   python app.py
   ```

2. **Access the API:**
   - **Get All Products:** `GET http://108.130.67.29:5000/products`



## API Endpoint

**Response:**

### GET /products
Returns all products in the catalog.

**Response:**
```json
[
  {
    "id": 1,
    "name": "Laptop",
    "description": "A high-end laptop",
    "price": 1200.0
  },
  {
    "id": 2,
    "name": "Phone", 
    "description": "Latest smartphone",
    "price": 800.0
  }
]
```

## Configuration

Database connection settings in `app.py`:
```python
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://<username>:<password>@localhost/catalog"
```

Update the connection string with your MySQL credentials as needed.

## Development vs Production

**Current setup is for development only.** The Flask development server shows this warning:
```
WARNING: This is a development server. Do not use it in a production deployment.
```

For production deployment:
- Use a production WSGI server (Gunicorn, uWSGI)
- Set `debug=False`
- Use environment variables for database credentials
- Add proper logging and monitoring

## Troubleshooting

**Table doesn't exist error:**
- Ensure the `products` table exists in your MySQL database
- Check that `__tablename__ = 'products'` matches your actual table name

**Connection errors:**
- Verify MySQL is running
- Check database credentials and hostname
- Ensure the `catalog` database exists

**Import errors:**
- Install required packages: `pip install flask flask-sqlalchemy pymysql`
