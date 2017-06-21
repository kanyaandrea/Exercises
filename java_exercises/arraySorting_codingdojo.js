function selectionSort(items) {
    var lenght = items.length;

    for (var i = 0; i < lenght-1; i++){
        var min = i;

        for (var j = i+1 ; j < lenght; j++){
            if (items[j]< items[min]) {
                min =j;     
            }
        }
    if (min !== i) {
        var tmp = items[i];
        items[i] = items[min];
        items[min] = tmp;
       
        }
    }
}

var arrayToSort = [3, 2, 1, 4, 5];
selectionSort(arrayToSort);
console.log(arrayToSort);

