/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        ListNode *head = new ListNode();
        ListNode *headptr = head;
        int sum,rem,carry=0;
        while(l1!= nullptr && l2!= nullptr){
            int sum = l1->val + l2->val;
            if(sum+carry >9){
                sum = (sum+carry) % 10;
                carry = 1;
                ListNode *newNode = new ListNode();
                newNode->val = sum;
                newNode->next = nullptr;
                head->next = newNode;
                head = newNode;
                l1 = l1->next;
                l2=l2->next;
            }
            else{
                sum = sum+carry;
                carry = 0;
                ListNode *newNode = new ListNode();
                newNode->val = sum;
                newNode->next = nullptr;
                head->next = newNode;
                head = newNode;
                l1 = l1->next;
                l2=l2->next;

            }
        }


    while(l1!= nullptr){
        int sum = l1->val;
        if(sum+carry >9){
            sum = (sum+carry) % 10;
            carry = 1;
            ListNode *newNode = new ListNode();
            newNode->val = sum;
            newNode->next = nullptr;
            head->next = newNode;
            head = newNode;
            l1 = l1->next;

        }
        else{
            sum = sum+carry;
            carry = 0;
            ListNode *newNode = new ListNode();
            newNode->val = sum;
            newNode->next = nullptr;
            head->next = newNode;
            head = newNode;
            l1 = l1->next;
        }
    }

    while(l2!= nullptr){
        int sum =  l2->val;
        if(sum+carry >9){
            sum = (sum+carry) % 10;
            carry = 1;
            ListNode *newNode = new ListNode();
            newNode->val = sum;
            newNode->next = nullptr;
            head->next = newNode;
            head = newNode;
            l2=l2->next;
        }
        else{
            sum = sum+carry;
            carry = 0;
            ListNode *newNode = new ListNode();
            newNode->val = sum;
            newNode->next = nullptr;
            head->next = newNode;
            head = newNode;
            l2=l2->next;

        }
    }
    if(carry >=1){
        ListNode *newNode = new ListNode();
        newNode->val = 1;
        newNode->next = nullptr;
        head->next = newNode;
        head = newNode;
    }
    return headptr->next;
        
    }
};