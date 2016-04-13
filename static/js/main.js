// main object
var sofAnalyzer = {}

sofAnalyzer.validateForm = function(){
	// check if the search is ridiculous 
	var search_value = $("#search_value").val();
	if(search_value.length == 0){
		alert("INVALID SERACH!");
		return false;
	}else return true;
}

if ($('#chart_results').length != 0){
	if ($('#top_langs_chart_id').length != 0){
		$('#top_langs_chart_id').highcharts({
			chart: {renderTo: 'top_langs_chart_id', type: 'column'},
			title: {"text": topLangsTitle},
			xAxis: {type: 'category'},
			yAxis: {title: {text: 'Percentage (%)'}},
			// onclick function bar graph
			plotOptions: {
	            series: {
	                cursor: 'pointer',
	                point: {
	                    events: {
	                        click: function () {
	                        	$('#search_value').val(this.name);
	                        	$('#btn_analyze_search_value').click();
	                        }
	                    }
	                }
            	}
            },
			series: [{name: 'Skill', data: topLangs}]
		});
	}
	if ($('#top_locations_chart_id').length != 0){
		$('#top_locations_chart_id').highcharts({
			chart: {renderTo: 'top_locations_chart_id', type: 'pie'},
			title: {"text": topLocationsTitle},
			series: [{name: 'Percent', data: topLocations}]
		});		
	}
}

