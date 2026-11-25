
from pathlib import Path

import chromadb

# Import the embedding model from the knowledge_base folder
from knowledge_base.embedding_generator import model


# =====================================
# DATABASE CONFIGURATION
# =====================================

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = PROJECT_DIR / "chroma_db"

# Initial experimental relevance threshold
RELEVANCE_THRESHOLD = 1.55


# =====================================
# CONNECT TO CHROMADB
# =====================================

client = chromadb.PersistentClient(
    path=str(DATABASE_PATH)
)

collection = client.get_collection(
    name="electrohelp_products"
)


# =====================================
# PRODUCT SEARCH FUNCTION
# =====================================

def search_products(question, results_count=2):
    """
    Convert a customer question into an embedding,
    retrieve relevant products, and filter weak matches.
    """

    total_products = collection.count()

    if total_products == 0:
        return []

    # Convert customer question into a vector
    question_embedding = model.encode([question]).tolist()

    # Search ChromaDB
    results = collection.query(
        query_embeddings=question_embedding,
        n_results=min(results_count, total_products),
        include=["documents", "metadatas", "distances"]
    )

    # Organize relevant search results
    matching_products = []

    for index, product_id in enumerate(results["ids"][0]):

        distance = results["distances"][0][index]

        # Reject products that are not sufficiently relevant
        if distance > RELEVANCE_THRESHOLD:
            continue

        matching_products.append({
            "id": product_id,
            "text": results["documents"][0][index],
            "metadata": results["metadatas"][0][index],
            "distance": distance
        })

    return matching_products


# =====================================
# TEST PRODUCT SEARCH
# =====================================

if __name__ == "__main__":

    print("\nELECTROHELP AI - PRODUCT SEARCH")
    print("--------------------------------")

    customer_question = "Which product has a long battery life?"

    print(f"Customer question: {customer_question}")

    search_results = search_products(customer_question)

    print("\nSEARCH RESULTS")
    print("--------------------------------")

    for product in search_results:

        print(f"\nProduct: {product['metadata']['name']}")
        print(f"Category: {product['metadata']['category']}")
        print(f"Price: ${product['metadata']['price']}")
        print(f"Distance: {product['distance']:.4f}")
        print(f"Description: {product['text']}")

    print("\n--------------------------------")
