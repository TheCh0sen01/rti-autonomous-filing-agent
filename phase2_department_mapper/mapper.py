import chromadb

client = chromadb.PersistentClient(path="./db")
collection = client.get_collection("departments")

def map_department(issue_type):
    result = collection.query(
        query_texts=[issue_type],
        n_results=1
    )

    return result["metadatas"][0][0]