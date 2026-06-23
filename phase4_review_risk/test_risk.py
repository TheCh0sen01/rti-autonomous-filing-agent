from risk_checker import analyze_rti

sample = """
My ration card has been pending for 8 months.
Why is the officer deliberately delaying it?
Provide Aadhaar number, salary details, and all records.
"""

result = analyze_rti(sample)

print(result)