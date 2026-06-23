import json
from datetime import datetime

def save_tracking(tracking_id):

    data = {
        "tracking_id": tracking_id,
        "dispatch_date": str(datetime.now()),
        "status": "Dispatched"
    }

    with open("phase5_filing/generated_docs/tracking.json", "w") as f:
        json.dump(data, f, indent=4)

    return data