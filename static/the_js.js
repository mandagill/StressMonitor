
function printTest() {
	console.log("Just print stuff");
}


function startTracking() {
	// Sets tracking flag to true and calls function to supress button when successful
	// FIXME If I also call the route to start *actually* tracking, the page hangs. 
	// Implement Celery Thursday morning
	$.post("/begin_tracking", 
		{message: "Turn the tracking on plz kthx"} ,
		function (result) { 
			$("#begin-tracking").attr("disabled", true);
			$("#stop-tracking").attr("disabled", false);
			// console.log(result);
			// $.get("/track_variance");
		});
};


function stopTracking() {
	$.post("/stop_tracking",
	{message: "Okay now stop!"},
	function (result) {
		$("#begin-tracking").attr("disabled", false);
		$("#stop-tracking").attr("disabled", true);
	});
}

document.getElementById("stop-tracking").addEventListener('click', stopTracking);
document.getElementById("begin-tracking").addEventListener('click', startTracking);