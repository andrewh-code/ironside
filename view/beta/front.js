function jsFunction(){
    
    //declare variable
    var txt_input;
    
    txt_input = document.getElementById("stock_input").value;
    
    //append .json file extension 
    txt_input = txt_input.concat(".json");
    
    document.getElementById("output").innerHTML = txt_input;
}