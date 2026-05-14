import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from pandas import read_csv
import os
import random

filename = 'quotes.csv'
names = ['Author', 'Quotes']
data = read_csv(filename)
quotes = data['Quote']
authors = data['Author']

q_index = random.randint(0, len(quotes)-1)
quote = quotes[q_index]
author = authors[q_index]

if author == "":
    author = "Unknown"
quote = quote + " - " + author


def get_credentials():
    creds = Credentials(
        token=None,
        refresh_token=os.environ["GMAIL_REFRESH_TOKEN"],
        client_id=os.environ["GMAIL_CLIENT_ID"],
        client_secret=os.environ["GMAIL_CLIENT_SECRET"],
        token_uri="https://oauth2.googleapis.com/token",
        scopes=["https://www.googleapis.com/auth/gmail.send"],
    )
    creds.refresh(Request())
    return creds


def create_message(to, subject, body, html=False):
    if html:
        msg = MIMEMultipart("alternative")
        msg["To"] = to
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "html"))
    else:
        msg = MIMEText(body)
        msg["To"] = to
        msg["Subject"] = subject

    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    return {"raw": raw}

def send_email(to, subject, body, html=False):
    creds = get_credentials()
    service = build("gmail", "v1", credentials=creds)

    message = create_message(to, subject, body, html)
    result = service.users().messages().send(userId="me", body=message).execute()

    print(f"Email sent! Message ID: {result['id']}")
    return result

# Plain text
send_email("AMMA", "Quote of the Day", quote)
send_email("NANA", "Quote of the Day", quote)
send_email("MYSELF", "Quote of the Day", quote)
