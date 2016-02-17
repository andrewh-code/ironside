function jsFunction(){
    
    //declare variable
    var txt_input;
    var cb_50day;
    var cb_200day;
    var cb_historicalClosing;
    
    txt_input = document.getElementById("stock_input").value;
    //cb_50day = document.getElementsByClassName("50ma").value;
    //cb_200day = document.getElementsByClassName("200ma").value;
    //cb_historicalClosing = document.getElementsByClassName("historicalClosing").value;
    
    if (document.getElementById("50ma").checked){
        cb_50day = txt_input.concat("_50ma.json");    
    }
    
    if (document.getElementById("200ma").checked){
        cb_200day = txt_input.concat("_200ma.json");
    }
    
    if (document.getElementById("hc").checked){
        cb_historicalClosing = txt_input.concat("_historicalclosing.json");
    }
    
    
    //append .json file extension 
    txt_input = txt_input.concat(".json");
    
    
    document.getElementById("output").innerHTML = txt_input;
    document.getElementById("outputTechnicalIndicator").innerHTML = cb_200day;
    document.getElementByID("js_chart").innerHTML = test();
}

function checkTechnicalIndicators(input, indicator){

    var txt_indicator = '';
    
    if (input.checked){
        txt_indicator = indicator.concat(".json");        
    }
    
    document.getElementById("outputTechnicalIndicator").innerHTML = txt_indicator;
}

//http://codereview.stackexchange.com/questions/24172/get-the-value-of-the-name-attribute-of-each-element-with-class-class

function test () {
    
    var files = new Array('bbry.json', 'apple_stock.json');
    //$.getJSON('msft.json', function (data) {
    $.getJSON('http://www.highcharts.com/samples/data/jsonp.php?filename=aapl-c.json&callback=?', function (data) {  
        console.log(data);
        // Create the chart
        $('#container').highcharts('StockChart', {


            rangeSelector : {
                selected : 1
            },

            title : {
                text : 'BBRY Stock Prices'
            },

            series : [{
                name : 'BBRY',
                data : data,
                tooltip: {
                    valueDecimals: 2
                }
            }]
        });
    });
    
    
   //$('#container').highcharts().show();
};

//http://jsfiddle.net/lorwynz_11/sSLnn/3/
//http://jsfiddle.net/NxEnH/89/
//http://www.java2s.com/Tutorials/highcharts/Example/Series_Event/Hide_series_in_click_event.htm
//http://jsfiddle.net/gh/get/jquery/1.9.1/highslide-software/highcharts.com/tree/master/samples/stock/members/chart-addseries/

