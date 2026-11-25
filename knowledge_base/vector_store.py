
from pathlib import Path

import chromadb

from knowledge_base.embedding_generator import generate_embeddings


# =====================================
# DATABASE CONFIGURATION
# =====================================

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = PROJECT_DIR / "chroma_db"

client = chromadb.PersistentClient(
    path=str(DATABASE_PATH)
)

collection = client.get_or_create_collection(
    name="electrohelp_products"
)


# =====================================
# STORE PRODUCT EMBEDDINGS
# =====================================

def store_product_embeddings():

    print("\nGenerating product embeddings...")

    embedded_documents = generate_embeddings()

    ids = []
    documents = []
    metadatas = []
    embeddings = []

    for item in embedded_documents:

        ids.append(str(item["id"]))
        documents.append(item["text"])
        metadatas.append(item["metadata"])
        embeddings.append(item["embedding"].tolist())

    collection.upsert(
        ids=ids,
        documents=documents,
        metadatas=metadatas,
        embeddings=embeddings
    )

    print("\nELECTROHELP AI - VECTOR DATABASE")
    print("--------------------------------")
    print(f"Products stored: {collection.count()}")
    print(f"Collection name: {collection.name}")
    print(f"Database location: {DATABASE_PATH}")
    print("--------------------------------")


if __name__ == "__main__":
    store_product_embeddings()

