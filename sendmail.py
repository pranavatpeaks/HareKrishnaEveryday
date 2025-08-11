import yagmail
from script import mail_content
from web import mailing_list

# Example JSON data
data = mail_content

# Extract details
quote = data["quotations"][0]
chapter = data["chapter_name"]
book = data["book_title"]

# HTML Email Content
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
mail_list = mailing_list  # Get the mailing list from web.py
if not mail_list:
    print("⚠️ No subscribers found. Please ensure you have subscribers in the mailing list.")
    exit()
print(f"Mailing list: {mail_list}")
# Send Email
yag = yagmail.SMTP("thenectarbrew@gmail.com")  # already registered credentials
yag.send(
    to= mail_list,
    subject="📖 Your Daily Spiritual Quote",
    contents=html_content
)

print("✅ Styled email sent!")
