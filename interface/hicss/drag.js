window.addEventListener('load',onload,false);
function onload(){
	for (var i=1;i<11;i++){
		var id = 'moment_rep'+i;
		//alert(document.getElementById(id))
		document.getElementById(id).value = ""; 
	}
}

function OnDragStart(target, evt){
	evt.dataTransfer.setData('IdElement', target.id);
}
function OnDropTarget(target, evt){
	
	var id_rep = evt.dataTransfer.getData('IdElement');
	var id_moment = target.getAttribute('id')
	//alert(id);
	//alert(id_rep);
	//alert(target);
	//alert(target.hasChildNodes());
	if (target.hasChildNodes()==false){
		target.appendChild(document.getElementById(id_rep));
		evt.preventDefault();
		document.getElementById('moment_'+id_rep).value = id_moment; 
	}
	else {
		
		evt.preventDefault();
	}
}
