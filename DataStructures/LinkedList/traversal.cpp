#include <iostream>

struct Node {
    int data;
    Node* next;
};

void traverse_linked_list(Node* head) {
    Node* current_node = head;

    while(current_node != nullptr) {
        std::cout << current_node->data << " ";
        current_node = current_node->next;
    }

    std::cout<<std::endl;
}

int main() {
    Node* head = new Node{10};

    head->next = new Node{20};
    head->next->next = new Node{30};

    traverse_linked_list(head);
    
    return 0;
}