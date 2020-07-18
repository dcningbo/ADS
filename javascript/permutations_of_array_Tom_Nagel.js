// generate 2D array containing all permutations of input array
​
//insert a new element into an array at a given index
function insert(arr, x, i){
    //ensure target index is valid
    if (i > arr.length || i < 0){
        return false;
    }
    var out = [];
    
    //copy values up to target index
    for (let j = 0; j < i; j++){
        out.push(arr[j]);
    }
    //insert x
    out.push(x);
    //copy values after target index
    for (let k = i; k < arr.length; k++){
        out.push(arr[k]);
    }
    return out;
}
​
//generate permutations
//work from last values in arrays to enable use of push/pop
function perms(inArray){
    //copy input array to preserve original
    var arr = [...inArray];

    //initialise 'stacks'
    var r = [];
    var s = [];
    
    //stack r starts with subarray of length 1 containing final value in input
    r.push([arr.pop()]);

    //generate permutaions of last n elements of array using permuations of last n-1 elements
    while (arr.length > 0){
        //get last value left in input
        let newVal = arr.pop();

        //run for each prevously generated permuation
        while (r.length > 0){
            //topmost previous permuation
            let rLast = r.length-1;
            
            //insert newVal in each position in active permuation
            for (let i = 0; i <= r[rLast].length; i++){
                let p = insert(r[rLast],newVal,i);
                s.push(p);
            }
            //remove last sub-array in r
            r.pop();
        }
        
        //move everything back from s to r
        r = [...s];
        s = [];
    }
    return r;
}
​
var seed = ['a','b','c','d','e'];
var permutations = perms(seed);
console.log('Generated ' + permutations.length + ' permutations of ' + seed);
console.log(permutations);