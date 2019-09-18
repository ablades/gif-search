from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    """Return homepage."""
    #Extract query term from url
    search = request.args.get("search")

    params = {
    "q" : search,
    "key": '4HIPRMNS9U52',
    "limit": 9}

    button_request = request.args.get('button')
    
    r = requests.get("https://api.tenor.com/v1/search", params)
    
    #Alter request based on selection
    if button_request == "trending":
        params["q"] = None
        r = requests.get("https://api.tenor.com/v1/trending?", params)
    elif button_request == "random":
        params["q"] = "random"
        r = requests.get("https://api.tenor.com/v1/random?", params)
    
    gifs = json.loads(r.content)['results']

    return render_template("index.html", gifs=gifs)


if __name__ == '__main__':
    app.run(debug=True)
