import os
import json
import yagmail
from dotenv import load_dotenv
from script import mail_content

# Load environment variables
load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

if not EMAIL_USER or not EMAIL_PASS:
    raise ValueError("❌ EMAIL_USER or EMAIL_PASS not set in environment variables.")

# Load subscribers from file
subscribers_file = "subscribers.json"
if os.path.exists(subscribers_file):
    with open(subscribers_file, "r") as f:
        subscribers = json.load(f)
else:
    subscribers = []

print(f"📬 Mailing list initialized. Current subscribers: {subscribers}")

if not subscribers:
    print("⚠️ No subscribers found. Please ensure you have subscribers in the mailing list.")
    exit()

# Prepare HTML content
quote = mail_content["quotations"][0]
chapter = mail_content["chapter_name"]
book = mail_content["book_title"]

html_content = f"""
<html>
<body style="font-family: Arial, sans-serif; background-color: #f5f5f5; padding: 20px;">
    <div style="max-width: 600px; margin: auto; background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
        <h2 style="color: #4a4a4a; text-align: center;">📖 Daily Spiritual Quote</h2>
        <blockquote style="font-style: italic; color: #333; line-height: 1.6; border-left: 4px solid #ff9900; padding-left: 15px; margin: 20px 0;">
            {quote}
        </blockquote>
        <p style="color: #666; font-size: 14px; text-align: right; margin-top: 20px;">
            — <b>{chapter}</b><br>
            <i>{book}</i>
        </p>
    </div>
</body>
</html>
"""

# Send emails without using keyring
yag = yagmail.SMTP(user=EMAIL_USER, password=EMAIL_PASSWORD, oauth2_file=None)

for email in subscribers:
    try:
        yag.send(to=email, subject="📖 Your Daily Spiritual Quote", contents=html_content)
        print(f"✅ Email sent to {email}")
    except Exception as e:
        print(f"❌ Failed to send email to {email}: {e}")