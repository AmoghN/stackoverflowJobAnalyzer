import getStats
from flask import Flask, request, render_template, url_for, jsonify, redirect
import encodings.idna


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('result.html', page = "index",success = True)

# search GET request from stackOverFlow and get stats
@app.route('/search', methods=['GET'])
def drawGraph():
    try:      
        searchTerm = request.args.get('q')
        getResults = getStats.getResults(searchTerm)
        topLangs = getResults["topLangs"]
        topLocations = getResults["topLocations"]
        topEmployers = getResults["topEmployers"]
        totalRemote = getResults["totalRemote"]
        totalResults = getResults["totalResults"]
        success = getResults["success"]
        return render_template(
            'result.html'
            ,searchTerm = searchTerm
            ,topLangs=topLangs
            ,topLocations = topLocations
            ,topEmployers = topEmployers
            ,totalRemote = totalRemote
            ,totalResults = totalResults
            ,success = success
            ,page = "result"
            )
    except Exception as e:
        success = False   
        return render_template(
            'result.html'
            ,searchTerm = searchTerm
            ,success = success)

if __name__ == "__main__":
    app.run(debug=False)
