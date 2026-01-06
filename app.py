from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/boost')
def boost():
    uid = request.args.get('uid')
    key = request.args.get('key')
    gid = request.args.get('gid')
    
    # এটি বর্তমানে সচল এবং ব্লক-মুক্ত লিঙ্ক
    url = "https://ff-api.garena.com/api/guild/glory_boost"
    
    headers = {
        "x-ga-uid": uid, 
        "x-ga-token": key, 
        "Content-Type": "application/json",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 12)",
        "Connection": "keep-alive"
    }
    
    payload = {"guild_id": gid}
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=20)
        return jsonify({"status": response.status_code, "data": response.json()}), response.status_code
    except:
        return jsonify({"error": "Garena Server Busy"}), 500

if __name__ == "__main__":
    app.run()
