console.log('Hello Console!');


var map = {
	"pathways" : [
		{
			"name" : "career",
			"color" : "#0000FF",
			"x" : [0.1, 0.6, 0.4],
			"y" : [0.4, 0.1, 0.3]
		}
	]
}

var progress = {
	"career" : 2
}

function loadNodes() {
	
	var map_element = document.getElementById("map");
	var offsetX = map_element.offsetLeft;
	var width = map_element.offsetWidth;
	var height = map_element.offsetHeight;
			
	console.log(offsetX)
	
	for (var i = 0, n = map.pathways.length; i < n; i++) {
		
		var pathway = map.pathways[i];
		
		for(var j = 1, num = progress[pathway.name]; j < num; j++)
		{
            var new_popup = document.createElement('div');
            new_popup.className = 'popup';
            new_popup.id = 'test';

			var new_node = document.createElement("div");
			new_node.className = "node";
			new_node.style.position = "absolute";
			new_node.style.left = (map.pathways[i].x[j] * width) + offsetX;
			new_node.style.top = (map.pathways[i].y[j] * height);

            new_node.onClick();

			map_element.appendChild(new_node);


		}
	}
	
}

window.onload = function() {
	loadNodes();
	//window.addEventListener('resize', updateNodes, false);
}
