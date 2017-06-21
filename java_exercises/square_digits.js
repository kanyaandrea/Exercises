

function squareDigits(num){
    var sqrNumber=[];
    numberToString = num.toString();
    for(i=0; i < numberToString.length; i++){
        digit = parseInt(numberToString[i]);
        sqrNumber.push(digit*digit);
    }
    return parseInt(sqrNumber.join(""));
}


function squareDigits_2(num){
    var sqrNumber="";
    numberToString = num.toString();
    for(i=0; i < numberToString.length; i++){
        digit = parseInt(numberToString[i]);
        var square = (digit*digit);
        square.toString
        var newNumber= sqrNumber += square;
    }
    return parseInt(newNumber);
}
