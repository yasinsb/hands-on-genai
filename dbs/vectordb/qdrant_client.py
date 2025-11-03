import uuid
from qdrant_client import QdrantClient


DB_PATH = "my_db"

client = QdrantClient(path=DB_PATH)

# Optionally set the embedding model - default is BAAI/bge-small-en
client.set_model("BAAI/bge-small-en")


def clean_collection(collection_name: str):
    """Clean a collection."""
    client.delete_collection(collection_name)
    return "Collection cleaned successfully"


def add_documents(
    collection_name: str,
    documents: list[str],
    ids: list[str] = None,
    metadata: list[dict] = None,
):
    """Add a document to the collection. Collection will be auto-created if it doesn't exist."""
    if ids is None:
        ids = [str(uuid.uuid4()) for _ in documents]

    client.add(
        collection_name=collection_name,
        documents=documents,
        metadata=metadata,
        ids=ids,
    )
    return "Document added successfully"


def search_documents(collection_name: str, query: str, k: int = 3):
    """Search for similar documents in the collection."""
    results = client.query(
        collection_name=collection_name,
        query_text=query,
        limit=k,
    )
    return results
