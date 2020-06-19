function genRandomArray(n) {
	var arr = [];
	for (var i = 0; i < n; i++) {
		arr[i] = Math.round(10 * Math.random());
	}
	return arr;
}

function swap(array, index1, index2) {
	var saveElement = array[index1];
	array[index1] = array[index2];
	array[index2] = saveElement;
	return array;
}

function bubbleSort(array) {
	var n = array.length;
	for (var i = 1; i < n; i++) {
		var count = 0;
		for (var j = 0; j < n - 1; j++) {
			if (array[j + 1] < array[j]) {
				count++;
				swap(array, j, j + 1);
			}
		}
		if (count == 0) {
			break;
		}
	}
	return array;
}
// return a Boolean: true if x is in array, and false otherwise
function binarySearch(array, x) {
    var beginIndex = 0;
    var endIndex = array.length - 1;
    while (beginIndex < endIndex) {
		var midPoint = Math.floor((beginIndex + endIndex) / 2);
		if (array[midPoint] == x) {
			return true
		} else if (x < array[midPoint]) {
			endIndex = midPoint - 1;
		} else {
			beginIndex = midPoint + 1
		}
    }
	return false;
}

var arr = genRandomArray(14);

console.log(bubbleSort(arr));
console.log(binarySearch(bubbleSort(arr), 2));


// Do not modify the code below this point--------------------------------
// module.exports = {
// 	genRandomArray: genRandomArray,
// 	swap: swap,
// 	bubbleSort: bubbleSort,
// 	binarySearch: binarySearch
// }