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
			
			var dims = [
			{
				"color": "#453325",
				"width": 40,
				"xoffset": -10,
				"yoffset": 2
			},
			{
				"color": "#34261C",
				"width": 22,
				"xoffset": 0,
				"yoffset": 0
			},
			{
				"color": line.color,
				"width": 20,
				"xoffset": 0,
				"yoffset": 0
			}];
			
			for(var c = 0; c < 3; c++)
			{
				ctx.beginPath();              
				ctx.lineWidth = dims.width;
				ctx.strokeStyle = dims.color; 
				ctx.moveTo(line.x[0] + dims[c].xoffset,
						line.y[0] + dims[c].yoffset);
				
				for(var i = 1, n = line.x.length; i < n; i++)
				{
					ctx.lineTo(line.x[i] + dims[c].xoffset,
							line.y[i] + dims[c].yoffset);
				}
					
				ctx.stroke();
			}
			
		}
	}
}

window.onload = function() {
	drawMap();
	window.addEventListener('resize', drawMap, false);
}
