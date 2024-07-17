#include <iostream>

struct Node {
    int data;
    Node* next;
};

void InsertAtBeginning(Node*& head, int data) {
    Node* newNode = new Node();
    newNode->data = data;
    newNode->next = head;
    head = newNode;
}

void InsertAtEnd(Node*& head, int data) {
    Node* newNode = new Node();
    newNode->data = data;
    newNode->next = nullptr;

    if(head == nullptr) {
        head = newNode;
        return;
    }

    Node* temp = head;

    while (temp->next != nullptr)
        temp = temp->next;

    temp->next = newNode;
}

void insertAtPosition(Node*& head, int data, int position) {
    if (position == 1) {
        InsertAtBeginning(head, data);
        return;
    }

    Node* newNode = new Node();
    newNode->data = data;
    Node* temp = head;
    for (int i = 1; i< position - 1; i++) {
        if (temp == nullptr) return;
        temp = temp->next;
    }

    newNode->next = temp->next;
    temp->next = newNode;
}

int main()
{
    std::cout << "Hi" << std::endl;
    return 0;
}