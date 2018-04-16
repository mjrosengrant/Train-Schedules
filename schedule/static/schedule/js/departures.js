
$( document ).ready(function() {
    window.setInterval(function(){
        updateBoards();
    }, 15000);
});

function updateBoards(){
    $.ajax({
        type: 'GET',
        dataType: "json",
        url: "api/",
        success: function (responseData, textStatus, jqXHR) {
            console.log("GET successful");
            var trHTMLNorth = '';
            var trHTMLSouth = '';
            var timestamp = responseData["North Station"][0].TimeStamp;

            $.each(responseData["North Station"], function (i, departure) {
                scheduledTime = new Date(departure.ScheduledTime*1000)
                trHTMLNorth += 
                '<tr>' +
                '<td>' + departure.Origin + '</td>' +
                '<td>' + departure.Trip + '</td>' +
                '<td>' + departure.Destination + '</td>' + 
                '<td>' + scheduledTime.toTimeString() + '</td>' + 
                '<td>' + departure.Lateness + '</td>' + 
                '<td>' + departure.Track + '</td>' + 
                '<td>' + departure.Status + '</td>' + 
                '</tr>';
            });

            $.each(responseData["South Station"], function (i, departure) {
                scheduledTime = new Date(departure.ScheduledTime*1000)
                trHTMLSouth += 
                '<tr>' +
                '<td>' + departure.Origin + '</td>' +
                '<td>' + departure.Trip + '</td>' +
                '<td>' + departure.Destination + '</td>' + 
                '<td>' + scheduledTime.toTimeString() + '</td>' + 
                '<td>' + departure.Lateness + '</td>' + 
                '<td>' + departure.Track + '</td>' + 
                '<td>' + departure.Status + '</td>' + 
                '</tr>';
            });

            datetime = new Date(timestamp*1000);
            $('#timestamp').text(datetime.toTimeString());

            $("#northStationTable > tbody tr").remove();
            $('#northStationTable').find('tbody:last').append(trHTMLNorth);

            $("#southStationTable > tbody tr").remove();    
            $('#southStationTable').find('tbody:last').append(trHTMLSouth);
        },
        error: function () {
            console.log("GET failed");
        }
    });
}
