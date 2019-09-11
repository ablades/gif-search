from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    #Extract query term from url
    search = request.args.get("search")

    #Make 'params' dict with query term and API key
    params = {
        "q" : search,
        "key": '4HIPRMNS9U52',
        "limit": 10}

    #Make an API call to Tenor using the 'requests' library
    r = requests.get("https://api.tenor.com/v1/search", params)

    gifs = json.loads(r.content)['results']

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter
    return render_template(
        "index.html", gifs=gifs)

if __name__ == '__main__':
    app.run(debug=True)
