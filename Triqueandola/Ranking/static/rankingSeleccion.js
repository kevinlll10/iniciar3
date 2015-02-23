
function escogerCategoria(evento){
	evento.preventDefault();
	evento.stopPropagation();
	id = evento.target.id;
	$('#elected').removeAttr('id');
	$('.clasificacion-'+id[id.length-1]).attr('id','elected');
}

for(i=1;i<=$('.rankingResumido-Botones a').length;i++){
	$('#boton'+i.toString()).click(escogerCategoria);
}
