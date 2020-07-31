function InsertionSortRecursive(vector, lgt = vector.length)
{
    if (lgt <= 1)
        return;
    // Recursively call the same function
    InsertionSortRecursive(vector, lgt - 1);
    var key = vector[lgt - 1];
    var i = lgt - 2;
    var str = "";
    for (j = 0; j < lgt; j++)
    {
        str += vector[j];
    }
    console.log("Before sort -> " + str);
    // Sort the array
    while (i >= 0 && vector[i] > key)
    {
        vector[i + 1] = vector[i];
        str = "";
        for (j = 0; j < lgt; j++)
        {
            str += vector[j];
        }
        console.log("Shifting during sort -> " + str);
        i--;
    }
    vector[i + 1] = key;
    str = "";
    for (j = 0; j < lgt; j++)
    {
        str += vector[j];
    }
    console.log("After sort -> " + str);
}
var vector = [7, 3, 2, 5, 6, 1]
InsertionSortRecursive(vector);
console.log("Sorted -> " + vector)