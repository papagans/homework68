// var i = 1;
// function pashArman() {
//     div = document.createElement('div');
//     div.className = 'element';
//     text = document.createTextNode("Element " + i.toString());
//     div.appendChild(text);
//     document.getElementById("container").appendChild(div);
//     i += 1;
//     var letters = ['red', 'green', 'purple', 'blue', 'yellow'];
//     var cvet = '';
//     cvet += letters[Math.floor(Math.random() * 5)];
//     div.style.color = cvet;
//     console.log(cvet)
// }
const container = document.getElementById("container");
var math = ["add", "subtract", "multiply", "divide"];

function pashArman(){
    var num1 = document.createElement("input");
        num1.setAttribute('type', 'number');
        num1.setAttribute('id', 'num1');
        container.appendChild(num1);
    var num2 = document.createElement("input");
        num2.setAttribute('type', 'number');
        num2.setAttribute('id', 'num2');
        container.appendChild(num2);
     for (var i = 0; i < math.length; i++) {
        // var div = document.createElement('div');
        // div.className = 'element';
        // var text = document.createTextNode("Element " + math[i]);
        // div.appendChild(text);
        // container.appendChild(div);
        let countryLink = document.createElement('button');
        countryLink.setAttribute('id', math[i]);
        countryLink.append(math[i]);
        container.appendChild(countryLink);

    }
}
pashArman();

function numberList(){
    var numberA = document.getElementById('num1').value;
    var numberB = document.getElementById('num2').value;
    var buttonId = event.target;
    var myButton = buttonId.getAttribute('id');
    return JSON.stringify({
        A: numberA,
        B: numberB,
        Button: myButton,
    });
}

$('#add').click(
    function () {
        let link = 'http://127.0.0.1:8000/add/';
        jqueryLoadIndex(link);
        var buttonId = event.target;
        var myButton = buttonId.getAttribute('id');
        console.log(buttonId.getAttribute('id'), 'TARGET')
    }
);

$('#subtract').click(
    function () {
        let link = 'http://127.0.0.1:8000/subtract/';
        jqueryLoadIndex(link);
    }
);

$('#multiply').click(
    function () {
        let link = 'http://127.0.0.1:8000/multiply/';
        jqueryLoadIndex(link);
    }
);

$('#divide').click(
    function () {
        let link = 'http://127.0.0.1:8000/divide/';
        jqueryLoadIndex(link);
    }
);

function ajaxError(status) {
    console.log(status);
    console.log(response);

}


function jqueryLoadIndex(link) {

    $.ajax({
        url: link,
        data: numberList(),
        method: 'POST',
        success: serverSuccessData,
        error: ajaxError
    });
}


function serverSuccessData(response) {
        var result = document.createElement("text");
        result.append(response);
        var div = document.createElement('div');
        div.setAttribute('id', 'element');
        var text = document.createTextNode(response);
        div.appendChild(text);
        console.log(document.getElementById("element"));
        // if (document.getElementById("element")){div.replaceChild(text, text)}
        // else {
        document.getElementById("container").appendChild(div)
        // }
        var num = Number(response);
        if (num){
            div.style.backgroundColor = 'green';
        }
        else {
            div.style.backgroundColor = 'red';
        }
        console.log(typeof response);


}




