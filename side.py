import requests as req

# Acessar musica pelo nome
def api_req(pattern):
    url = "http://www.songsterr.com/a/ra/songs.json?pattern="
    resp = req.get(url+pattern.lower())
    return resp.json()
        #return f"{i['artist']['name']} - {i['title']} - {i['id']}"

#print(api_req('You know Im no good'))



