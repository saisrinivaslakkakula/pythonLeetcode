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
    ListNode* middleNode(ListNode* head) {
        int count = 0;
    ListNode *tmphead = head;
    while(tmphead!= nullptr){
        count++;
        tmphead = tmphead->next;
    }
    delete tmphead;
    int middle = (count/2)+1;
    int i=1;
    while (i!=middle){
       i++;
       head= head->next;
    }
    return head;
    }
};