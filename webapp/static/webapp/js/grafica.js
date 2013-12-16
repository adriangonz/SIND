/* 
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
 
 var date = [];
 
 
 $(function(){
 for( i = 0; i < _data.length; i++) {
        var fech = new Date((_data[i]).fields.Fecha);
            date.push([

                    fech.getHours()+":"+fech.getMinutes()+":"+fech.getSeconds()
            ]);
    }

 });
    
   $(function () { 
  

console.log(date);
      
       
        $('#contP').highcharts({
            title: {
                text: 'Potencia',
                x: -20 //center
            },
            subtitle: {
                text: 'Actualizacion online',
                x: -20
            },
            xAxis: {
                categories: date
            },
            yAxis: {
                title: {
                    text: 'Total'
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
            tooltip: {
                valueSuffix: ' Hz'
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'middle',
                borderWidth: 0
            },
            series: [{
                name: 'P Activa',
                data: (function() {
				// generate an array of random data
				var data = [];

				for( i = 0; i < _data.length; i++) {
					data.push([
						
						(_data[i]).fields.PAct
					]);
				}
                                
                          
                                
				return data;
			})(),
                color: '#0000FF'
            },{
                name: 'P Reactiva',
                data: (function() {
				// generate an array of random data
				var data = [];

				for( i = 0; i < _data.length; i++) {
					data.push([
						
						(_data[i]).fields.PReact
					]);
				}
                                
                          
                                
				return data;
			})(),
                color: '#00FD00'
            },{
                name: 'P Aparente',
                data: (function() {
				// generate an array of random data
				var data = [];

				for( i = 0; i < _data.length; i++) {
					data.push([
						
						(_data[i]).fields.PAparente
					]);
				}
                                
                          
                                
				return data;
			})(),
                color: '#FF0000'
            }]
        });
    });
    
    //Factor de Potencia
    
    $(function () {
        $('#contFP').highcharts({
            title: {
                text: 'Factor Potencia',
                x: -20 //center
            },
            subtitle: {
                text: 'Actualizacion online',
                x: -20
            },
            xAxis: {
                categories: date
            },
            yAxis: {
                title: {
                    text: 'Total'
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
            tooltip: {
                valueSuffix: ' Hz'
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'middle',
                borderWidth: 0
            },
		
		
		
		series : [{
			name : 'Factor Potencia',
			data : (function() {
				// generate an array of random data
				var data = [];

				for( i = 0; i < _data.length; i++) {
					data.push([
						
						(_data[i]).fields.FactorPotencia
					]);
				}
                                
                          
                                
				return data;
			})()
		}]
            
        });
    });
    
  
    
    
    
    $(function () {
        $('#contF').highcharts({
            title: {
                text: 'Frecuencia',
                x: -20 //center
            },
            subtitle: {
                text: 'Actualizacion online',
                x: -20
            },
            xAxis: {
                categories: date
            },
            yAxis: {
                title: {
                    text: 'Total'
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
            tooltip: {
                valueSuffix: ' Hz'
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'middle',
                borderWidth: 0
            },
            series: [{
                name: 'Frecuencia',
                data: (function() {
				// generate an array of random data
				var data = [];

				for( i = 0; i < _data.length; i++) {
					data.push([
						
						(_data[i]).fields.Frec
					]);
				}
                                
                          
                                
				return data;
			})(),
                color: '#FF0000'
            }]
        });
    });
    
    $(function () {
        $('#contV').highcharts({
            title: {
                text: 'Voltaje',
                x: -20 //center
            },
            subtitle: {
                text: 'Actualizacion online',
                x: -20
            },
            xAxis: {
                categories: date
            },
            yAxis: {
                title: {
                    text: 'Total'
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
            tooltip: {
                valueSuffix: ' V'
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'middle',
                borderWidth: 0
            },
            series: [{
                name: 'Voltaje',
                data: (function() {
				// generate an array of random data
				var data = [];

				for( i = 0; i < _data.length; i++) {
					data.push([
						
						(_data[i]).fields.V
					]);
				}
                                
                          
                                
				return data;
			})(),
                color: '#0F0F0F'
            }]
        });
    });
    
    $(function () {
        $('#contI').highcharts({
            title: {
                text: 'Intensidad',
                x: -20 //center
            },
            subtitle: {
                text: 'Actualizacion online',
                x: -20
            },
            xAxis: {
                categories: date
            },
            yAxis: {
                title: {
                    text: 'Total'
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
            tooltip: {
                valueSuffix: ' A'
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'middle',
                borderWidth: 0
            },
            series: [{
                name: 'Intensidad',
                data: (function() {
				// generate an array of random data
				var data = [];

				for( i = 0; i < _data.length; i++) {
					data.push([
						
						(_data[i]).fields.I
					]);
				}
                                
                          
                                
				return data;
			})(),
                color: '#FF00FF'
            }]
        });
    });


function prueba()
{
    
  $.ajax({
        method: "get",
        url: "/api/date",
        dataType:"json",
        success: function(res){
            fecha = new Date(res.date);
            
        }
        
    });
   
}
