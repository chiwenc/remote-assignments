function ajax(src, callback){
    // your code here
    
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            callback(xhttp.responseText);
        }
    };
    xhttp.open("GET", src, true);
    xhttp.send();

    
}
function render(data){
    // your code here.
    // document.createElement() and appendChild() methods are preferred.
    var new_div = document.createElement('div');
    new_div.innerHTML = data;
    document.body.appendChild(new_div); 

}
ajax("https://remote-assignment.s3.ap-northeast-1.amazonaws.com/products",
function(response){
    render(response);
}); // you should get product information in JSON format and render data in the page
    