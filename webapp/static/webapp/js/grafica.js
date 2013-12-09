/* 
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

$(function () {
        $('#container1').highcharts({
            title: {
                text: 'Potencia Actual',
                x: -20 //center
            },
            subtitle: {
                text: 'Actualización online',
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
                name: 'Potencia Actual',
                data: [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6],
                color: '#0000FF'
            }]
        });
    });
    
    $(function () {
        $('#container2').highcharts({
            title: {
                text: 'Factor de Potencia',
                x: -20 //center
            },
            subtitle: {
                text: 'Actualización online',
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
                name: 'Factor de Potencia',
                data: [-0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1, 14.1, 8.6, 2.5],
                color: '#00FFFF'
            }]
        });
    });
    
    $(function () {
        $('#container3').highcharts({
            title: {
                text: 'Potencia Reactiva',
                x: -20 //center
            },
            subtitle: {
                text: 'Actualización online',
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
                name: 'Potencia Reactiva',
                data: [-0.9, 0.6, 3.5, 8.4, 13.5, 17.0, 18.6, 17.9, 14.3, 9.0, 3.9, 1.0],
                color: '#00FF00'
            }]
        });
    });
    
    $(function () {
        $('#container4').highcharts({
            title: {
                text: 'Potencia Aparente',
                x: -20 //center
            },
            subtitle: {
                text: 'Actualización online',
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
                name: 'Potencia Aparente',
                data: [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8],
                color: '#FFFF00'
            }]
        });
    });
    
    $(function () {
        $('#container5').highcharts({
            title: {
                text: 'Frecuencia',
                x: -20 //center
            },
            subtitle: {
                text: 'Actualización online',
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
        $('#container6').highcharts({
            title: {
                text: 'Voltaje',
                x: -20 //center
            },
            subtitle: {
                text: 'Actualización online',
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
        $('#container7').highcharts({
            title: {
                text: 'Intensidad',
                x: -20 //center
            },
            subtitle: {
                text: 'Actualización online',
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