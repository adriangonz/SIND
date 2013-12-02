/* 
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

function comprobFecha(obj)
{
    var fecha = obj.tbDate.value;
    var error = document.getElementById("errDate");
    
    var val = true;
    
    if(estaVacio(fecha))
    {
      
        val = false;
        error.innerHTML = "<strong>ERROR</error>. La fecha no puede estar vacia";
        
    }
    else if(validarFecha(fecha))
    {
        val = false;
         error.innerHTML = "<strong>ERROR</error>. Formato de fecha incorrecto";
    }
    else
    {
         error.innerHTML = "";
    }
     
     return val;
}


function cambiarFecha(obj)
{
    alert("Fecha modificada");
}

function estaVacio(n)
{
	var vacio = false;
	
	if(n == "" || n == null || n.indexOf(" ")==0 || n.indexOf("\t")==0)
		vacio = true;
	
	return vacio;
}

function validarFecha(texto)
{
    var error = true;
    
    var text = texto.split(" ");
    
    if(text.length == 2)
    {
	var fecha = text[0].split("/");
	var hora = text[1].split(":");

	if(fecha.length == 3 && hora.length == 3)
	{
	
		var Dia = fecha[0]; 
		var Mes = fecha[1]; 
		var Ano = fecha[2];
                var hor = hora[0];
                var min = hora[1];
                var seg = hora[2];

	    var fechaReal = new Date(Ano,Mes-1,Dia,hor,min,seg);
	    
	    if(Dia == fechaReal.getDate() && (Mes-1) == fechaReal.getMonth() && Ano == fechaReal.getFullYear() && hor == fechaReal.getHours() && min == fechaReal.getMinutes() && seg == fechaReal.getSeconds())
	    {
	    	error = false;
	    }
	    
        }
       
        
    }

  return error

	

}