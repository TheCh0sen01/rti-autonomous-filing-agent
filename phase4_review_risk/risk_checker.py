from phase4_review_risk.rules import RISK_PATTERNS

def analyze_rti(text):

    issues = []
    suggestions = []
    risk_score = 0

    lower_text = text.lower()

    for category, config in RISK_PATTERNS.items():

        for pattern in config["patterns"]:

            if pattern in lower_text:
                issues.append(f"{category}: {pattern}")
                risk_score += config["weight"]

                if config["suggestion"] not in suggestions:
                    suggestions.append(config["suggestion"])

    # Extra semantic checks
    if "why" in lower_text and "status" not in lower_text:
        issues.append("Potential opinion-based framing")

        if "Use factual wording like 'What is the reason for delay?'" not in suggestions:
            suggestions.append(
                "Use factual wording like 'What is the reason for delay?'"
            )

        risk_score += 0.15

    # Risk classification
    if risk_score == 0:
        status = "Safe"
    elif risk_score < 0.4:
        status = "Moderate"
    else:
        status = "Risky"

    return {
        "risk_score": round(min(risk_score, 1), 2),
        "status": status,
        "issues": issues,
        "suggestions": suggestions
    }