// Constructor function to make linked list objects (all belonging to class LLNode).
function LLNode(data) {
    this.data = data;
    this.next = null;
}
// Assigning nodes.
let head = new LLNode(1);
head.next = new LLNode(2);
head.next.next = new LLNode(6);
head.next.next.next = new LLNode(3);
head.next.next.next.next = new LLNode(4);
head.next.next.next.next.next = new LLNode(5);
head.next.next.next.next.next.next = new LLNode(6);
// Search for data stored in linked list.
function searchLL (head, item) {
    let temp = head;
    while (temp !== null) {
        if (temp.data === item) {
            return true;
        }
        temp = temp.next;
    }
    return false;
}
// Ask feedback from online tutor on below function.
var removeElements = function(head, val) {
    let temp = head;
    while (temp !== null && temp.next !== null) {
        if (temp.next.data === val) {
            if (temp.next.next !== null) {
                temp.next = temp.next.next;
            }
            else {
                temp.next = null;
            }
        }
        temp = temp.next;
    }
    return head;
};
// Count number of times that an item appears in the linked list.
function numberLL (head, item) {
    let temp = head;
    let count = 0;
    // Search only if list is not empty; i.e. head !== null.
    while (temp !== null) {
        if (temp.data === item) {
            count++;
        }
        temp = temp.next;
    }
    // Return the new value of count which would have changed 
    // after going through the while loop;
    // Otherwise, value remains 0 meaning item doesn't appear.
    return count;
}
// Test to confirm functions work properly.
// let trial = removeElements(head, 6);
// console.log(trial);
console.log(searchLL(5,6))