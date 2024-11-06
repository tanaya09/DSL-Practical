#include<bits/stdc++.h>
using namespace std;

class Node
{
    public : 
    Node *next = NULL;
    Node* head = NULL;
    char data;
    map<char , int>p;
    vector<int>stack;
    vector<int>postfix;
    int symbols; 

    void push(char x)
    {
        Node* new_node = new Node;
        new_node->data=x;
        if(head==NULL)
        {
            head = new_node;
        }
        else
        {
            Node *temp = head;
            while(temp->next!=NULL)
            {
                temp = temp->next;
            }
            temp->next = new_node;
            new_node->next = NULL;
        }
    }

    void insert_in_map()
    {
        p['('] = 0;
        p['+'] = 1;
        p['-'] = 1;
        p['/'] = 2;
        p['*'] = 2;
        p[')'] = 3;
    }
    
    void display()
    {
        Node *temp = head;
        while(temp!=NULL)
        {
            cout<<temp->data<<"\n";
            temp = temp->next;
        }
        cout<<"\n";
    }

    void operation(int n)
    {

        Node* temp = head;
        while(temp!=NULL)
        {

            for(int i=0;i<n;i++)
            {
                if(temp->data==)
            }
            temp = temp->next;

        }

    }


    
};

int main()
{
    Node a;
    cout<<"\nEnter the size of the infix expression : ";
    int n;
    cin>>n;
    char arr[n];
    cout<<"\nEnter infix expression : ";
    cin>>arr;
    for(int i=0;i<n;i++)
    {
        a.push(arr[i]);
    }
    cout<<"\n";
    a.display();
    a.operation(n);

    return 0;
}