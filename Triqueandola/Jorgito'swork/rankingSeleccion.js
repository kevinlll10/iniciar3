
function escogerCategoria(evento){
	evento.preventDefault();
	evento.stopPropagation();
	id = evento.target.id;
	$('#elected').removeAttr('id');
	$('.comentariosBox-comentariosSet-box'+id[id.length-1]).attr('id','elected');
}

for(i=1;i<=$('.comentariosBox-header-cursos ul li').length;i++){
	$('#boton'+i.toString()).click(escogerCategoria);
}
