console.log('Hello Console!');


var map = {
	"pathways" : [
		{
			"name" : "base",
			"x" : [0.628],
			"y" : [0.521]
		},
		{
			"name" : "career",
			"x" : [0.627, 0.5795, 0.5795],
			"y" : [0.425, 0.4, 0.3]
		},
		{
			"name" : "collaboration",
			"x" : [0.540, 0.463, 0.400],
			"y" : [0.416, 0.305, 0.190]
		},
		{
			"name" : "college",
			"x" : [0.47, 0.55, 0.38],
			"y" : [0.525, 0.5165, 0.515]
		},
		{
			"name" : "change_agency",
			"x" : [0.648, 0.582, 0.495],
			"y" : [0.58, 0.65, 0.735]
		}
	]
}

var progress = {
	"base" : 1,
	"career" : 3,
	"collaboration" : 3,
	"college" : 3,
	"change_agency" : 3
}

function loadNodes() {
	var map_element = document.getElementById("map");
	var bg_img = document.getElementById("background-img");
	var offsetX = bg_img.offsetLeft;
	var width = bg_img.offsetWidth;
	var height = bg_img.offsetHeight;
			
	console.log(height)
	
	for (var i = 0, n = map.pathways.length; i < n; i++) {
		
		var pathway = map.pathways[i];
		
		for(var j = 0, num = progress[pathway.name]; j < num; j++)
		{
			var new_node = document.createElement("div");
			new_node.className = "node";
			new_node.style.position = "absolute";
			new_node.style.left = (map.pathways[i].x[j] * width) + offsetX;
			new_node.style.top = (map.pathways[i].y[j] * height);
			
			
			
			map_element.appendChild(new_node);
		}
	}
	
}

window.onload = function() {
	loadNodes();
	//window.addEventListener('resize', updateNodes, false);
}
