$( document ).ready(function() {
	window.setInterval(function(){
  		updateBoards()
  		//alert("Updating boards");
	}, 5000);
});

function updateBoards(){
    // $.get("http://developer.mbta.com/lib/gtrtfs/Departures.csv", dataType="jsonp", function(data, status){
    //     alert("Data: " + data + "\nStatus: " + status);
    // });

    $.ajax({
	    type: 'GET',
	    // dataType: "json",
	    crossDomain: true,
	    url: "http://developer.mbta.com/lib/gtrtfs/Departures.csv",
	    success: function (responseData, textStatus, jqXHR) {
	        console.log("in");
	        // var data = JSON.parse(responseData['AuthenticateUserResult']);
	        console.log(data);
	    },
	    error: function (responseData, textStatus, errorThrown) {
	        console.log("GET failed");
	    }
	});
};