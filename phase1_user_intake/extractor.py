import json
import os
from google import genai
from dotenv import load_dotenv
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def extract_issue(text):

    prompt = f"""
You are an expert government complaint analyzer.

Analyze the complaint and return STRICT VALID JSON only.

Required fields:
- issue_type
- department_hint
- location
- severity
- confidence

Rules:
1. Output must be valid JSON.
2. Use double quotes only.
3. Use commas correctly.
4. No explanation.
5. No markdown.
6. No extra text.
7. Be specific.

Department mapping hints:
- ration card -> Food Department
- potholes -> Municipal Corporation
- water -> Water Board
- electricity -> Electricity Board
- land records -> Revenue Department

Example:
{{
    "issue_type": "water_supply",
    "department_hint": "Water Board",
    "location": "Chennai",
    "severity": "high",
    "confidence": 0.95
}}

Complaint:
{text}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    response_text = response.text.strip()

    try:
        return json.loads(response_text)
    except json.JSONDecodeError:
        print("Gemini returned invalid JSON:")
        print(response_text)
        return None