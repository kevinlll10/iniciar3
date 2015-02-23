
function escogerCategoria(evento){
	console.log("HOLAAA");
	evento.preventDefault();
	evento.stopPropagation();
	id = evento.target.id;
	console.log(id)
	$('#elected').removeAttr('id');
	$('.central-Lista-'+id[id.length-1]).attr('id','elected');
	
}

console.log("HOLI");

for(i=1;i<=$('.informacion-OpcionesBusqueda ul li').length;i++){
	$('#boton'+i.toString()).click(escogerCategoria);
	console.log("HOLI");

}

