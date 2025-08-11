from flask import Flask, request, render_template_string
import json
import os

app = Flask(__name__)

SUBSCRIBERS_FILE = "subscribers.json"

# HTML template
HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Subscribe to Daily Quote</title>
</head>
<body style="font-family: Arial; text-align: center; margin-top: 50px;">
    <h2>📖 Subscribe to Daily Spiritual Quote</h2>
    <form method="POST">
        <input type="email" name="email" placeholder="Enter your email" required style="padding: 10px; width: 250px;">
        <br><br>
        <button type="submit" style="padding: 10px 20px;">Subscribe</button>
    </form>
    {% if message %}
        <p style="color: green; margin-top: 20px;">{{ message }}</p>
    {% endif %}
</body>
</html>
"""

def load_subscribers():
    if os.path.exists(SUBSCRIBERS_FILE):
        with open(SUBSCRIBERS_FILE, "r") as f:
            return json.load(f)
    return []

def save_subscribers(subscribers):
    with open(SUBSCRIBERS_FILE, "w") as f:
        json.dump(subscribers, f, indent=2)

@app.route("/", methods=["GET", "POST"])
def subscribe():
    message = None
    if request.method == "POST":
        email = request.form.get("email").strip().lower()
        subscribers = load_subscribers()

        if email not in subscribers:
            subscribers.append(email)
            save_subscribers(subscribers)
            message = f"{email} has been subscribed successfully!"
        else:
            message = "You are already subscribed!"

    return render_template_string(HTML_FORM, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6969)