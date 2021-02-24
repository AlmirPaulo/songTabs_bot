import requests as req
from flask import Flask
from threading import Thread


#API request
def api_req(pattern):
    url = "http://www.songsterr.com/a/ra/songs.json?pattern="
    resp = req.get(url+pattern.lower())
    return resp.json()

#Server
app = Flask('')

@app.route('/')
def home():
  return"It's Alive!"
  
def run():
  app.run(host ='0.0.0.0', port = 8080)

def keep_alive():
  t = Thread(target = run)
  t.start()