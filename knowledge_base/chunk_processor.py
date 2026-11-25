
from knowledge_base.document_processor import create_product_documents


# =====================================
# CREATE PRODUCT CHUNKS
# =====================================

def create_chunks():

    documents = create_product_documents()

    chunks = []

    for document in documents:

        chunk = {
            "id": str(document["id"]),
            "text": document["text"],
            "metadata": document["metadata"]
        }

        chunks.append(chunk)

    return chunks


# =====================================
# TEST CHUNK PROCESSING
# =====================================

if __name__ == "__main__":

    chunks = create_chunks()

    print("\nELECTROHELP AI - TEXT CHUNKING")

    print("--------------------------------")

    print(f"Total chunks created: {len(chunks)}")

    print("--------------------------------")

    for chunk in chunks:

        print(f"\nChunk ID: {chunk['id']}")

        print(f"Product: {chunk['metadata']['name']}")

        print("\nChunk Content:")

        print(chunk["text"])

        print("\n--------------------------------")

