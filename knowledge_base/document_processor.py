
from knowledge_base.product_loader import load_products


# =====================================
# CONVERT PRODUCTS INTO TEXT DOCUMENTS
# =====================================

def create_product_documents():

    products = load_products()

    documents = []

    for product in products:

        # Product basic information
        document = f"""
Product: {product['name']}

Category: {product['category']}

Price: {product['price']} {product['currency']}

Description: {product['description']}
"""

        # Add product specifications
        document += "\nSpecifications:\n"

        for key, value in product['specifications'].items():

            document += f"{key}: {value}\n"

        # Add recommended uses
        document += "\nBest For:\n"

        for use in product['best_for']:

            document += f"- {use}\n"

        documents.append({
            "id": product["id"],
            "text": document.strip(),
            "metadata": {
                "name": product["name"],
                "category": product["category"],
                "price": product["price"]
            }
        })

    return documents


# =====================================
# TEST DOCUMENT PROCESSING
# =====================================

if __name__ == "__main__":

    documents = create_product_documents()

    print("\nELECTROHELP AI - PROCESSED DOCUMENTS")

    print("------------------------------------")

    print(f"Total documents created: {len(documents)}")

    print("------------------------------------")

    for document in documents:

        print(f"\nDocument ID: {document['id']}")

        print(document["text"])

        print("\n------------------------------------")
