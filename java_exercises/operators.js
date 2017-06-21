
numberArray = [1,3,4,5,5,5]

function add() {
    sum = 0;
    for (var i = 0; i < numberArray.length; i++) {
        sum += numberArray[i];
    }
    return sum;
}

function multiply() {
    sum = 0;
    for (var i = 0; i < numberArray.length; i++) {
        sum *= numberArray[i];
    }
    return sum;
}
