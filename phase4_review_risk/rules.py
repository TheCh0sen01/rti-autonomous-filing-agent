RISK_PATTERNS = {
    "opinion_based": {
        "patterns": [
            "why are you",
            "why did you",
            "corrupt",
            "negligent",
            "malpractice",
            "deliberately delaying",
            "fraud",
            "illegal action",
            "irregularities"
        ],
        "weight": 0.25,
        "suggestion": "Use factual wording instead of accusations."
    },

    "privacy_sensitive": {
        "patterns": [
            "aadhaar",
            "salary details",
            "bank account",
            "personal address",
            "family details",
            "medical records"
        ],
        "weight": 0.30,
        "suggestion": "Remove personal/private information requests."
    },

    "broad_requests": {
        "patterns": [
            "everything",
            "all records",
            "all details",
            "internal memos",
            "communications",
            "complete file"
        ],
        "weight": 0.20,
        "suggestion": "Ask for specific documents instead of broad requests."
    },

    "security_sensitive": {
        "patterns": [
            "security system",
            "classified",
            "confidential",
            "surveillance data"
        ],
        "weight": 0.35,
        "suggestion": "Avoid requesting security-sensitive information."
    }
}