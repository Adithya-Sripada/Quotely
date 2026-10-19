# Quotely

**Quotely** is an automated Python service that delivers a curated daily quote directly to your inbox. By combining **Pandas** for efficient dataset manipulation, the **Google Gmail API** for secure OAuth 2.0 email dispatch, and a Unix **cron job** for background scheduling, Quotely runs hands-free with zero manual intervention.

---

## Features

* **Automated Data Extraction:** Reads, filters, and samples from a local dataset of quotes using `pandas`.
* **Secure Email Delivery:** Uses the official **Gmail API** (`google-api-python-client`) and **OAuth 2.0** instead of less secure SMTP password methods.
* **MIME Formatting:** Constructs clean, readable emails (plain-text/HTML) with quote text and author attribution.
* **Zero-Touch Scheduling:** Configured to trigger automatically at a set time every day via `cron`.

---

## Tech Stack

* **Language:** Python 3.x
* **Libraries:** `pandas`, `google-api-python-client`, `google-auth-httplib2`, `google-auth-oauthlib`
* **API:** Google Workspace / Gmail API
* **Automation:** Unix Cron (`crontab`)

---

## Project Structure

```text
Quotely/
├── main.py              # Core script: samples quote and dispatches via Gmail API
├── quotes.csv           # Dataset containing quotes and authors
├── credentials.json     # Google Cloud OAuth 2.0 client credentials (gitignored)
├── token.json           # Generated OAuth access/refresh tokens (gitignored)
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
