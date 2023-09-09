from flask import Flask, jsonify, request
from utils import * 

app = Flask(__name__)
app.json.sort_keys = False

@app.route("/muftawu/api")
def get_details():
    slack_name = request.args.get("slack_name")
    track = request.args.get("track")

    DATA = {
    "slack_name": slack_name,
    "current_day": get_day_of_week(),
    "utc_time": get_utc_time(),
    "track": track,
    "github_profile_url": "",
    "github_repo_url": "",
    "status_code": 200,
    }

    return jsonify(DATA)

if __name__ == '__main__':
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)
    app.run(debug=True)