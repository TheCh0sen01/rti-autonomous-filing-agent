import json
import re
from langchain_community.llms import Ollama

llm = Ollama(model="qwen3:8b")


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
    "issue_type": "ration card delay",
    "department_hint": "Food Department",
    "location": "Chennai",
    "severity": "High",
    "confidence": 0.85
}}

Complaint:
{text}
"""

    response = llm.invoke(prompt)

    print("RAW RESPONSE:", response)

    # Try direct JSON parsing
    try:
        return json.loads(response)

    except Exception:
        pass

    # Extract JSON block if model adds extra text
    try:
        match = re.search(r'\{.*\}', response, re.DOTALL)
        if match:
            cleaned_json = match.group()

            # Fix common missing comma issues
            cleaned_json = re.sub(
                r'"\s*\n\s*"',
                '",\n"',
                cleaned_json
            )

            return json.loads(cleaned_json)

    except Exception:
        pass

    # Final fallback
    return {
        "issue_type": text,
        "department_hint": "Unknown",
        "location": "Not Provided",
        "severity": "Medium",
        "confidence": 0.5
    }