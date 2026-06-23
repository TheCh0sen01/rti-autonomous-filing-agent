import chromadb
import pandas as pd

client = chromadb.PersistentClient(path="./db")
collection = client.get_or_create_collection("departments")

df = pd.read_csv("phase2_department_mapper\\knowledge_base\\departments.csv")

for idx, row in df.iterrows():
    collection.add(
        documents=[row["issue_type"]],
        metadatas=[{
            "department": row["department"],
            "pio_name": row["pio_name"],
            "email": row["email"],
            "address": row["address"]
        }],
        ids=[str(idx)]
    )

print("Knowledge Base Built Successfully")