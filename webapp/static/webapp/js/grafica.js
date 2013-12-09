/* 
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

var chartP;
var fecha;

$(function () {
    
    Highcharts.setOptions({
		global : {
			useUTC : false
		}
	});
    
        chartP = new Highcharts.Chart({
                chart: {
                    renderTo: 'contP',
                    defaultSeriesType: 'line'
                },
            title: {
                text: 'Potencia activa , Pot. reactiva , Pot. aparente',
                x: -20 //center
            },
            subtitle: {
                text: 'Actualizacion online',
                x: -20
            },
            xAxis: {
                categories: ['time1', 'time2', 'time3', 'time4', 'time5', 'time6',
                    'time7', 'time8', 'time9', 'time10', 'time11', 'time12']
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
                valueSuffix: ' W'
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'middle',
                borderWidth: 0
            },
            series: [{
                name: 'P Activa',
                data: [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6],
                color: '#0000FF'
            },{
                name: 'P Reactiva',
                data: [3.4, 5.9, 7.0, 1.5, 2.2, 5.5, 10.2, 12.5, 7.3, 6.3, 0.9, 2.6],
                color: '#00FD00'
            },{
                name: 'P Aparente',
                data: [20.0, 21.9, 22.5, 30.5, 12.2, 5.5, 3.2, 6.5, 10.3, 12.3, 11.9, 15.6],
                color: '#FF0000'
            }]
        });
    });
    
    //Factor de Potencia
    
    $(function () {
        $('#contFP').highcharts('StockChart',{
            title: {
                text: 'Factor de Potencia',
                x: -20 //center
            },
            subtitle: {
                text: 'Actualizacion online',
                x: -20
            },
            chart : {
			events : {
				load : function() {

                                        prueba();
                                    // set up the updating of the chart each second
					var series = this.series[0];
					setInterval(function() {     
						var x = fecha.getTime(), // current time
						y = Math.round(Math.random() * 100);
						series.addPoint([x, y], true, true);
					}, 1000);
				}
			}
		},
		rangeSelector: {
			buttons: [{
				count: 1,
				type: 'minute',
				text: '1M'
			}, {
				count: 5,
				type: 'minute',
				text: '5M'
			}, {
				type: 'all',
				text: 'All'
			}],
			inputEnabled: false,
			selected: 0
		},
		
		
		exporting: {
			enabled: false
		},
		
		
		
		series : [{
			name : 'Factor Potencia',
			data : (function() {
				// generate an array of random data
				var data = [], time = (new Date()).getTime(), i;

				for( i = -999; i <= 0; i++) {
					data.push([
						time + i * 1000,
						Math.round(Math.random() * 100)
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
                categories: ['time1', 'time2', 'time3', 'time4', 'time5', 'time6',
                    'time7', 'time8', 'time9', 'time10', 'time11', 'time12']
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
                data: [51133.7, 1361.8, 32.5, 126.7, 21651.9, 61165.2, 1318946.4, 551.9, 11214.2, 1013.3, 676.6, 41.8],
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
                categories: ['time1', 'time2', 'time3', 'time4', 'time5', 'time6',
                    'time7', 'time8', 'time9', 'time10', 'time11', 'time12']
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
                data: [43.9, 74.2, 55.7, 38.5, 111.9, 215.2, 167.0, 146.6, 134.2, 11.3, 64.6, 47.8],
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
                categories: ['time1', 'time2', 'time3', 'time4', 'time5', 'time6',
                    'time7', 'time8', 'time9', 'time10', 'time11', 'time12']
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
                data: [32.9, 34.2, 54.7, 87.5, 111.9, 75.2, 47.0, 66.6, 44.2, 20.3, 61.6, 14.8],
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