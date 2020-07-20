function recPermute(arr) {
    if (arr.length == 1) {
        return [arr];
    }
    var perms = [];
    for (let i = 0; i < arr.length; i++) {
        var arr2 = [];
        for (let j = 0; j < arr.length; j++) {
            if (j != i) {
                arr2.push(arr[j]);
            }
        }
        var arr2perms = recPermute(arr2);
        for (let k = 0; k < arr2perms.length; k++) {
            let temp = arr2perms[k];
            temp.push(arr[i]);
            perms.push(temp);
        }
    }
    return perms;
}
var seed = ['a','b','c','d'];
var permutations = recPermute(seed);
console.log('Generated ' + permutations.length + ' permutations of ' + seed);
console.log(permutations);