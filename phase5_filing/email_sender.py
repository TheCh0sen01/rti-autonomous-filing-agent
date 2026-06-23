import os
import base64
from email.message import EmailMessage

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]


def authenticate_gmail():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds:
        flow = InstalledAppFlow.from_client_secrets_file(
            "phase5_filing/credentials/credentials.json",
            SCOPES
        )
        creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return creds


def send_email(recipient_email, pdf_path):

    creds = authenticate_gmail()
    service = build("gmail", "v1", credentials=creds)

    message = EmailMessage()
    message["To"] = recipient_email
    message["Subject"] = "RTI Application Submission"

    message.set_content(
        "Please find attached my RTI application under RTI Act 2005."
    )

    with open(pdf_path, "rb") as f:
        file_data = f.read()

    message.add_attachment(
        file_data,
        maintype="application",
        subtype="pdf",
        filename=os.path.basename(pdf_path)
    )

    encoded_message = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()

    sent_message = service.users().messages().send(
        userId="me",
        body={"raw": encoded_message}
    ).execute()

    return {
        "status": "sent",
        "message_id": sent_message["id"],
        "recipient": recipient_email
    }