$listaBotones = $('.cursoButton')

function escogerCategoria(evento ){
	//console.log(i)
	evento.preventDefault();
	evento.stopPropagation();
	console.log("hola")
	//$categorias = $('.comentariosBox-comentariosSet div');
	//$('.comentariosBox-comentariosSet-curso').removeattr('class');
	//$categorias[i].attr('class','comentariosBox-comentariosSet-curso');
}


for(i=0;i<$listaBotones.length;i++){
	$listaBotones[i].click(escogerCategoria);
}

