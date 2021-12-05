const values_list = JSON.parse(document.getElementById('values').textContent);
const values_json = JSON.parse(values_list) 


console.log(values_json)

let values = []
let dates = []
let currency = values_json[0].fields.currency
values_json.forEach(element => {
	values.push([Date.parse(element.fields.date), parseFloat(element.fields.value)])
});


Highcharts.chart('container', {	

    title: {
        text: 'Currency rates against USD - 5 days interval'
    },

    subtitle: {
        text: 'Source: https://www.vatcomply.com/'
    },

    yAxis: {
        title: {
            text: 'Value'
        }
    },

    xAxis: {
		type: 'datetime',
		minorTicks: false,
		minorTickInterval: null,
        title: {
            text: 'Date'
        }
    },

    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle'
    },

    series: [{
        name: currency,
        data: values
    }],

});