from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Private Server is Live"

@app.route('/boost')
def boost():
    uid = request.args.get('uid')
    key = request.args.get('key')
    gid = request.args.get('gid')
    
    url = "https://freefire.api.garena.com/api/guild/glory_boost"
    headers = {
        "x-ga-uid": uid, 
        "x-ga-token": key, 
        "Content-Type": "application/json"
    }
    payload = {"guild_id": gid, "action": "start_game"}
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        return jsonify({
            "status": response.status_code,
            "message": "Request Processed",
            "server_response": response.text
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
