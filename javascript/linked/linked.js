function LLNode(data) {
    this.data = data;
    this.next = null;
}
var head = new LLNode(5);
console.log(head);
console.log(head.data);
console.log(head.next);

head.next = new LLNode(10);
console.log(head.next.data);
console.log(head.next.next);

head.next = new LLNode(8);
console.log(head.next.data);
console.log(head.next.next);

head.next = new LLNode(6);
console.log(head.next.data);
console.log(head.next.next);

head.next = new LLNode(4);
console.log(head.next.data);
console.log(head.next.next);

function searchLL(head, item) {
    var temp = head;
    while (temp !== null) {
        if (temp.data === item) {
            return true;
        }
        temp = temp.next;
    }
    return false;
}

// searchLL(8,8);