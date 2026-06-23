import chromadb
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

db_path = os.path.join(BASE_DIR, "db")
kb_path = os.path.join(BASE_DIR, "legal_kb", "rti_law.txt")

client = chromadb.PersistentClient(path=db_path)
collection = client.get_or_create_collection("rti_laws")

with open(kb_path, "r", encoding="utf-8") as f:
    content = f.read()

collection.add(
    documents=[content],
    ids=["rti_law_1"]
)

print("RTI Legal Knowledge Base Built Successfully")
print("Total docs:", collection.count())