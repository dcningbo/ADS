function LLNode(data) {
    this.data = data;
    this.next = null;
}
var head = new LLNode(4);
console.log(head);
console.log(head.data);
console.log(head.next);

head.next = new LLNode(6);
console.log(head.next.data);
console.log(head.next.next);

head.next.next = new LLNode(8);
console.log(head.next.next.data);
console.log(head.next.next.next);

head.next.next.next = new LLNode(10);
console.log(head.next.next.next.data);
console.log(head.next.next.next.next);

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

console.log(searchLL(8,8));