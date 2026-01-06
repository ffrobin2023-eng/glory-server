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
    
    # এটিই হলো সঠিক লিঙ্ক যা আপনার কোডের ভেতরে থাকবে
url = "https://freefire.api.garena.com/api/guild/glory_boost"
"
    
    headers = {
        "x-ga-uid": uid, 
        "x-ga-token": key, 
        "Content-Type": "application/json",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 12;)"
    }
    
    payload = {"guild_id": gid}
    
    try:
        # ভিপিএন বা প্রক্সি জ্যাম এড়াতে টাইমআউট বাড়ানো হয়েছে
        response = requests.post(url, json=payload, headers=headers, timeout=20)
        return jsonify({
            "status": response.status_code,
            "server_response": response.json() if response.status_code == 200 else response.text
        }), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
