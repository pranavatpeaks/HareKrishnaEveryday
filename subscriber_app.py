import yagmail
from script import mail_content
import json

# Load subscribers from JSON
with open("subscribers.json", "r") as f:
    subscribers = json.load(f)

if not subscribers:
    print("No subscribers found.")
    exit()

# Extract details from mail_content
quote = mail_content["quotations"][0]
chapter = mail_content["chapter_name"]
book = mail_content["book_title"]

# HTML email template
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

# Send to each subscriber
yag = yagmail.SMTP("thenectarbrew@gmail.com")  # registered credentials
for email in subscribers:
    yag.send(to=email, subject="📖 Your Daily Spiritual Quote", contents=html_content)
    print(f"✅ Email sent to {email}")