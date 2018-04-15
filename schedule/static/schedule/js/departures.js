$( document ).ready(function() {
	// window.setInterval(function(){
  	updateBoards()
  		//alert("Updating boards");
	// }, 5000);
});

function updateBoards(){
    $.ajax({
	    type: 'GET',
	    dataType: "json",
	    url: "api/",
	    success: function (responseData, textStatus, jqXHR) {
	        console.log("in");
	        var trHTMLNorth = '';
	        var trHTMLSouth = '';
	        var timestamp = responseData["North Station"][0].TimeStamp

	        $.each(responseData["North Station"], function (i, departure) {
	            trHTMLNorth += 
	            '<tr>' +
	            '<td>' + departure.Origin + '</td>' +
	            '<td>' + departure.Trip + '</td>' +
	            '<td>' + departure.Destination + '</td>' + 
	            '<td>' + departure.ScheduledTime + '</td>' + 
	            '<td>' + departure.Lateness + '</td>' + 
	            '<td>' + departure.Track + '</td>' + 
	            '<td>' + departure.Status + '</td>' + 
	            '</tr>';
	        });

	        $.each(responseData["South Station"], function (i, departure) {
	            trHTMLSouth += 
	            '<tr>' +
	            '<td>' + departure.Origin + '</td>' +
	            '<td>' + departure.Trip + '</td>' +
	            '<td>' + departure.Destination + '</td>' + 
	            '<td>' + departure.ScheduledTime + '</td>' + 
	            '<td>' + departure.Lateness + '</td>' + 
	            '<td>' + departure.Track + '</td>' + 
	            '<td>' + departure.Status + '</td>' + 
	            '</tr>';
	        });
	        $('#northStationTable').find('tbody:last').append(trHTMLNorth)
	        $('#southStationTable').find('tbody:last').append(trHTMLSouth)
	        $('#timestamp').text(timestamp);
		},
	    error: function (responseData, textStatus, errorThrown) {
	        console.log("GET failed " + textStatus);
	    }
	});
};