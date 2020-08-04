# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 16:01:54 2020

@author: Dan
"""

def insertion_sort_recursive(v, lgt = len(v)):
    if lgt <= 1:
        return
    insertion_sort_recursive(v, lgt-1)
    key = v[lgt-1]
    i = lgt - 2
    string = ""
    for j in range(0, len(lgt)):
        string += v[j]
    
    while i >= 0 and v[i] > key:
        v[i+1] = v[i]






vector = [7, 3, 2, 5, 6, 1]
InsertionSortRecursive(vector);



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