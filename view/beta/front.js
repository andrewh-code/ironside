function jsFunction(){
    
    //declare variable
    var txt_input;
    var cb_50day;
    var cb_200day;
    var cb_historicalClosing;
    
    txt_input = document.getElementById("stock_input").value;
    cb_50day = document.getElementsByClassName("50ma").value;
    cb_200day = document.getElementsByClassName("50ma").value;
    cb_historicalClosing = document.getElementsByClassName("historicalClosing").value;
    
    //append .json file extension 
    txt_input = txt_input.concat(".json");
    if (document.getElementsByClassName("50ma"){
        cb_50day = "hello world";    
    }
    
    
    document.getElementById("output").innerHTML = cb_50day;
}

function checkTechnicalIndicators(input, indicator){

    var txt_indicator = '';
    
    if (input.checked){
        txt_indicator = indicator.concat(".json");        
    }
    
    document.getElementById("outputTechnicalIndicator").innerHTML = txt_indicator;
}

//http://codereview.stackexchange.com/questions/24172/get-the-value-of-the-name-attribute-of-each-element-with-class-class