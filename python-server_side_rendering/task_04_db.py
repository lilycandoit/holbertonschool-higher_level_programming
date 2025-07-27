from flask import Flask, render_template, request
import json, csv, sqlite3

app = Flask(__name__)

def load_from_json():
    with open("products.json", "r") as f:
        return json.load(f)

def load_from_csv():
    products = []
    with open("products.csv", newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

def load_from_sql(product_id=None):
    try:
        # Use 'with' for automatic connection management
        with sqlite3.connect("products.db") as conn:
            # Use Row factory to get dict-like rows
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            query = "SELECT id, name, category, price FROM Products"
            params = []

            if product_id:
                query += " WHERE id = ?"
                params.append(product_id)

            cursor.execute(query, params)
            rows = cursor.fetchall()
            # Convert Row objects to standard dictionaries
            return [dict(row) for row in rows]
    except sqlite3.Error as e:
        print("SQLite error:", e)
        return None # Return None to indicate a database-level error

@app.route("/products")
def display_products():
    source = request.args.get("source")
    product_id = request.args.get("id", type=int)

    products = None
    error = None

    if source == "json":
        products = load_from_json()
    elif source == "csv":
        products = load_from_csv()
    elif source == "sql":
        # SQL loader handles the product_id filtering internally
        products = load_from_sql(product_id)
        if products is None:
            error = "Database error occurred."
    else:
        error = "Wrong source specified. Please use 'json', 'csv', or 'sql'."

    # If we have a list of products and a product_id, filter it (for non-SQL sources)
    if products is not None and product_id and source != 'sql':
        products = [p for p in products if p.get("id") == product_id]

    # After loading and filtering, check if the result is empty when an ID was specified
    if product_id and not error and not products:
        error = "Product not found."

    return render_template("product_display.html", products=products or [], error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
