let parameters = {
    target: '#myFunction',
    data: [{
        fn: 'sin(x)',
        color: 'red'
    }],
    grid: true,
    yAxis: {
        domain: [-1, 1]
    },
    xAxis: {
        domain: [0, 2 * Math.PI]
    }
};


let parameters2 = {
    target: '#myFunction2',
    data: [{
        fn: 'sin(x)',
        color: 'red'
    }],
    grid: true,
    yAxis: {
        domain: [-1, 1]
    },
    xAxis: {
        domain: [0, 2 * Math.PI]
    }
};


function plot() {
    var f = document.querySelector("#function").value;
    var xMin = document.querySelector("#xMin").value;
    var xMax = document.querySelector("#xMax").value;
    var yMin = document.querySelector("#yMin").value;
    var yMax = document.querySelector("#yMax").value;
    var color = document.querySelector("#color").value;

    parameters.data[0].fn = f;
    parameters.xAxis.domain = [xMin, xMax];
    parameters.yAxis.domain = [yMin, yMax];
    parameters.data[0].color = color;

    functionPlot(parameters);
}

function plotg() {
    var g = document.querySelector("#function2").value;
    var xMin2 = document.querySelector("#xMin2").value;
    var xMax2 = document.querySelector("#xMax2").value;
    var yMin2 = document.querySelector("#yMin2").value;
    var yMax2 = document.querySelector("#yMax2").value;
    var color2 = document.querySelector("#color2").value;

    parameters2.data[0].fn = g;
    parameters2.xAxis.domain = [xMin2, xMax2];
    parameters2.yAxis.domain = [yMin2, yMax2];
    parameters2.data[0].color = color2;

    functionPlot(parameters2);
}

