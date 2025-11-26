from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask running in Docker on AWS EC2 🎉"

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    # For local testing only; in Docker we'll use gunicorn
    app.run(host="0.0.0.0", port=5000, debug=True)
