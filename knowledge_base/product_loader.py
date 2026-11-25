
import json
from pathlib import Path

# =====================================
# PRODUCT DATABASE LOCATION
# =====================================

BASE_DIR = Path(__file__).resolve().parent

PRODUCT_FILE = BASE_DIR / "products.json"


# =====================================
# LOAD PRODUCTS
# =====================================

def load_products():

    try:

        with open(PRODUCT_FILE, "r", encoding="utf-8") as file:

            products = json.load(file)

        return products

    except FileNotFoundError:

        print("Product database not found.")

        return []

    except json.JSONDecodeError:

        print("Error: Invalid JSON format.")

        return []


# =====================================
# DISPLAY PRODUCTS
# =====================================

if __name__ == "__main__":

    products = load_products()

    print("\nELECTROHELP AI PRODUCT DATABASE")

    print("--------------------------------")

    print(f"Total products loaded: {len(products)}")

    print("--------------------------------")

    for product in products:

        print(f"\nProduct: {product['name']}")

        print(f"Category: {product['category']}")

        print(f"Price: ${product['price']} {product['currency']}")

        print(f"Description: {product['description']}")
