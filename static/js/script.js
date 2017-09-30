console.log('Hello Console!');

var map = {
	"lines" : [
		{
			"name" : "career",
			"color" : "#0000FF",
			"x" : [10, 101],
			"y" : [50, 35]
		}
	]
}

function drawMap() {
	
	// Get and resize canvas
	var canvas = document.getElementById('map_canvas');
				
	// Draw the base icon
	if (canvas.getContext) {
		var ctx = canvas.getContext('2d');
		
		canvas.width = window.innerWidth;
		canvas.height = window.innerHeight - 15;
		
		ctx.translate(ctx.canvas.width/2, ctx.canvas.height/2);
		
		// For each line
		for (var lineId = 0, numLines = map.lines.length; lineId < numLines; lineId++) {
			
			
			var line = map.lines[lineId];
			
			ctx.beginPath();              
			ctx.lineWidth = "10";
			ctx.strokeStyle = line.color; 
			ctx.moveTo(line.x[0], line.y[0]);
			
			for(var i = 1, n = line.x.length; i < n; i++)
			{
				ctx.lineTo(line.x[i], line.y[i]);
			}
				
			ctx.stroke();
			
		}
	}
}

window.onload = function() {
	drawMap();
	window.addEventListener('resize', drawMap, false);
}