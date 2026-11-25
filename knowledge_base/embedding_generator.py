
from sentence_transformers import SentenceTransformer

from knowledge_base.chunk_processor import create_chunks


# =====================================
# LOAD EMBEDDING MODEL
# =====================================

MODEL_NAME = "all-MiniLM-L6-v2"

print("\nLoading embedding model...")

model = SentenceTransformer(MODEL_NAME)


# =====================================
# GENERATE PRODUCT EMBEDDINGS
# =====================================

def generate_embeddings():

    chunks = create_chunks()

    texts = [chunk["text"] for chunk in chunks]

    embeddings = model.encode(texts)

    results = []

    for index, chunk in enumerate(chunks):

        results.append({
            "id": chunk["id"],
            "text": chunk["text"],
            "metadata": chunk["metadata"],
            "embedding": embeddings[index]
        })

    return results


# =====================================
# TEST EMBEDDING GENERATION
# =====================================

if __name__ == "__main__":

    embedded_documents = generate_embeddings()

    print("\nELECTROHELP AI - EMBEDDING RESULTS")

    print("----------------------------------")

    print(f"Total embeddings generated: {len(embedded_documents)}")

    print("----------------------------------")

    for document in embedded_documents:

        print(f"\nProduct: {document['metadata']['name']}")

        print(f"Embedding dimensions: {len(document['embedding'])}")

        print(f"First 5 vector values: {document['embedding'][:5]}")

        print("\n----------------------------------")
