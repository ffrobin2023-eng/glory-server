from flask import Flask, request, jsonify
import requests
import random

app = Flask(__name__)

@app.route('/')
def home():
    return "🔥 High-Speed Booster Server is Online"

@app.route('/boost')
def boost():
    uid = request.args.get('uid')
    key = request.args.get('key')
    gid = request.args.get('gid')
    
    # একাধিক ডোমেইন ট্রাই করার সিস্টেম
    urls = [
        "https://ff-api.garena.com/api/guild/glory_boost",
        "https://freefire.api.garena.com/api/guild/glory_boost"
    ]
    
    headers = {
        "x-ga-uid": uid, 
        "x-ga-token": key, 
        "Content-Type": "application/json",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 12; Pixel 6 Build/SD1A.210817.036)",
        "Connection": "Keep-Alive"
    }
    
    payload = {"guild_id": gid}
    
    success = False
    last_response = ""

    for url in urls:
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=15)
            if response.status_code == 200:
                return jsonify({"status": 200, "msg": "Success", "data": response.json()}), 200
            last_response = response.text
        except:
            continue

    return jsonify({"status": 500, "error": "Server Blocked or Token Expired", "details": last_response}), 500

if __name__ == "__main__":
    app.run()
