import os
from langchain_community.llms import Ollama
import chromadb

llm = Ollama(model="qwen3:8b")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db")

client = chromadb.PersistentClient(path=db_path)
collection = client.get_or_create_collection("rti_laws")


def generate_rti(issue_data, contact_data, user_details):

    law_context = collection.query(
        query_texts=[issue_data["issue_type"]],
        n_results=1
    )

    context = law_context["documents"][0][0]

    prompt = f"""
You are an Indian RTI drafting assistant.

Use this RTI legal context:
{context}

Draft a legally valid RTI application under the RTI Act, 2005.

STRICT RULES:

1. Use OFFICIAL INDIAN LETTER FORMAT.

FORMAT MUST BE:

- Applicant full address at top
- Date
- "To,"
- Public Information Officer details
- Department name
- Department address
- Subject line
- Salutation ("Respected Sir/Madam,")

2. Do NOT use template headings like:
- Applicant Details
- Public Authority
- Body of Request
- RTI Request Number

3. Write as a formal government application.

4. Questions must be clearly numbered.

5. Use legal and procedural wording only.

6. Ask factual information only:
- current status
- reasons for delay
- officer responsible
- expected timeline
- relevant records

7. Do NOT ask accusatory or opinion-based questions.

8. Mention:
"Application fee of ₹10 through Indian Postal Order enclosed."

9. End with:
"Yours faithfully"

Applicant details:
Name: {user_details["name"]}
Address: {user_details["address"]}
Phone: {user_details["phone"]}
Email: {user_details["email"]}

Issue:
{issue_data["issue_type"]}

Department:
{contact_data["department"]}

PIO:
{contact_data["pio_name"]}

Address:
{contact_data["address"]}

Generate the final RTI exactly in official letter format.
"""

    return llm.invoke(prompt)