from flask import Flask, request, render_template_string

app = Flask(__name__)

# Your existing mailing list variable
mailing_list = []

HTML_FORM = """
<!doctype html>
<html>
<head>
    <title>Subscribe to Daily Quotes</title>
</head>
<body style="font-family: Arial; max-width: 600px; margin: auto; padding: 20px;">
    <h2>📩 Subscribe to Daily Spiritual Quotes</h2>
    <form method="POST">
        <input type="email" name="email" placeholder="Enter your email" required style="padding: 10px; width: 80%;">
        <button type="submit" style="padding: 10px;">Subscribe</button>
    </form>
    <p style="color: green;">{{ message }}</p>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def subscribe():
    message = ""
    if request.method == "POST":
        email = request.form.get("email").strip()
        if email:
            if email not in mailing_list:
                mailing_list.append(email)
                message = "✅ You have been subscribed successfully!"
            else:
                message = "⚠️ This email is already subscribed."
    return render_template_string(HTML_FORM, message=message)
    
print("Mailing list initialized. Current subscribers:", mailing_list)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6969)
