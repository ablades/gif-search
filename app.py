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
    "limit": 10}

    button_request = request.args.get('button')

    r = requests.get("https://api.tenor.com/v1/search", params)
    if button_request == "trending":
        search = None
        r = requests.get("https://api.tenor.com/v1/trending?", params)
    elif button_request == "random":
        search = 'random'
        r = requests.get("https://api.tenor.com/v1/random?", params)

    #Make an API call to Tenor using the 'requests' library
    # r = requests.get("https://api.tenor.com/v1/search", params)
    #Get post request

    gifs = json.loads(r.content)['results']
    # TODO: Render the 'index.html' template, passing the gifs as a named parameter
    return render_template(
        "index.html", gifs=gifs)


if __name__ == '__main__':
    app.run(debug=True)
