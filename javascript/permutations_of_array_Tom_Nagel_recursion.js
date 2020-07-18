//generate permutations recursively
function recPermute(arr){
    ​
        //if 1 element, return it in an array (basis step)
        if (arr.length == 1){
            return [arr];        
        }
        //variable to hold permuations of arr
        var perms = [];
    ​
        for (let i = 0; i < arr.length; i++){
            //create smaller array with all arr except element i
            var arr2 = [];
            for (let j = 0; j < arr.length; j++){
                if (j != i){
                    arr2.push(arr[j]);
                }
            }
    ​
            //get permuations of smaller array (recursive step)
            var arr2perms = recPermute(arr2);
    ​
            //for each permutation in arr2perms, insert arr[i] at end
            for (let k = 0; k < arr2perms.length; k++){
                let temp = arr2perms[k];
                temp.push(arr[i]);
                perms.push(temp);
            }
        }
    ​
        return perms;
    }
    ​
    var seed = ['a','b','c','d'];
    var permutations = recPermute(seed);
    console.log('Generated ' + permutations.length + ' permutations of ' + seed);
    console.log(permutations);