import stackOverFlowJobsAnalysis as sofja
from flask import Flask, request, render_template, url_for, jsonify, redirect


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('result.html', page = "index",success = True)

# search GET request from stackOverFlow and get stats
@app.route('/search', methods=['GET'])
def drawGraph():
    try:
        searchTerm = request.args.get('q')
        getResults = sofja.getResults(searchTerm)
        topLangs = getResults["topLangs"]
        topLocations = getResults["topLocations"]
        topEmployers = getResults["topEmployers"]
        totalResults = getResults["totalResults"]
        success = getResults["success"]
        title = ['Top ' + str(len(topLangs)) + ' tech. skills to combine with ' + searchTerm.upper(), 
                'Top ' + str(len(topLocations)) + ' locations for ' + searchTerm.upper()]
        return render_template(
            'result.html'
            ,searchTerm = searchTerm
            ,topLangs=topLangs
            ,topLocations = topLocations
            ,topEmployers = topEmployers
            ,totalResults = totalResults
            ,title = title
            ,success = success
            ,page = "result"
            )
    except Exception as e:
        success = False   
        return render_template(
            'result.html'
            ,searchTerm = searchTerm
            ,success = success)

# if __name__ == "__main__":
#     app.run(debug=True)
