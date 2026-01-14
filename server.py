from flask import Flask, request, render_template_string

app = Flask(__name__)

latest_message = "No message yet"

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>ESP32 AI Server</title>
</head>
<body>
    <h2>ESP32 AI Message Panel</h2>

    <form method="POST">
        <input type="text" name="msg" placeholder="Type your message" style="width:300px" required>
        <button type="submit">Send</button>
    </form>

    <h3>Current Message:</h3>
    <p>{{ message }}</p>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    global latest_message
    if request.method == "POST":
        latest_message = request.form.get("msg")
    return render_template_string(HTML_PAGE, message=latest_message)

@app.route("/get")
def get_message():
    return latest_message

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
