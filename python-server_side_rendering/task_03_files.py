from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def load_from_json():
    try:
        with open("products.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def load_from_csv():
    products = []
    try:
        with open("products.csv", newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except FileNotFoundError:
        pass  # products will remain an empty list
    return products

@app.route("/products")
def display_products():
    source = request.args.get("source")
    product_id = request.args.get("id", type=int)

    # Validate source
    if source == "json":
        products = load_from_json()
    elif source == "csv":
        products = load_from_csv()
    else:
        return render_template("product_display.html", error="Wrong source", products=[])

    # Optional filtering by id
    if product_id:
        products = [p for p in products if p["id"] == product_id]
        if not products:
            return render_template("product_display.html", error="Product not found", products=[])

    return render_template("product_display.html", products=products)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
