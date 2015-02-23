function escogerCategoria(evento){
	evento.preventDefault();
	evento.stopPropagation();
	id = evento.target.id;
	$('#elected').removeAttr('id');
	$('.rankingResumido-Clasificacion-'+id[id.length-1]).attr('id','elected');
}

for(i=1;i<=4;i++){ //En este caso siempre son cuatro
	$('#boton'+i.toString()).click(escogerCategoria);
}
