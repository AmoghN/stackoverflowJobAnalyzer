import time
import encodings.idna
from flask import Flask, request, render_template, url_for, jsonify, redirect

import getStats


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('result.html', page = "index", success = True), 200

# search GET request from stackOverFlow and get stats
@app.route('/search', methods=['GET'])
def drawGraph():
    try:
        time1 = time.time()
        
        searchTerm = request.args.get('q')
        getResults = getStats.getResults(searchTerm)
        topLangs = getResults["topLangs"]
        topLocations = getResults["topLocations"]
        topEmployers = getResults["topEmployers"]
        totalRemote = getResults["totalRemote"]
        totalResults = getResults["totalResults"]
        success = getResults["success"]

        print(f'Query Time: {time.time() - time1} seconds')

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
            ), 200
    except Exception as e:
        print(f"Error : {e}")
        success = False
        return render_template(
            'result.html'
            ,searchTerm = searchTerm
            ,success = success), 400

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=80)
