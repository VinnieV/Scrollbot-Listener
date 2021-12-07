#! /usr/bin/python3
import scrollphathd as sphd
from flask import Flask, request

APIKEY = "changeme"

# Init SPHD
sphd.rotate(180)

app = Flask(__name__)

@app.route("/scrollbot",methods=["GET"])
def scrollbot_message():
    try:
        apiKey = request.headers.get('x-scrollbot-auth','')
        if apiKey == APIKEY:
            message = request.args.get('message', '')
            #sphd.write_string(message)
            print(f"Showing message: {message}")
            return "Success!"
        else:
            return "Auth error!"
    except:
        return "Error!"

# Run webapp
app.run(host='0.0.0.0', port=8080)
