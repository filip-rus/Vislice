import bottle
import model

vislice = model.Vislice()

@bottle.get("/")
def index():
    return bottle.template("index.tpl")

@bottle.get("/img/<picture>")
def serve_pictures(picture):
    return bottle.static_file(picture,root="img")


bottle.run(reloader=True,debug=True)