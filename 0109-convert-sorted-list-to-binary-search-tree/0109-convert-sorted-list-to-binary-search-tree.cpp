class Solution {
public:
    ListNode* curr;

    TreeNode* build(int left, int right) {
        if (left > right) return nullptr;

        int mid = (left + right) / 2;

        // build left subtree
        TreeNode* leftNode = build(left, mid - 1);

        // current node becomes root
        TreeNode* root = new TreeNode(curr->val);
        curr = curr->next;

        // build right subtree
        root->left = leftNode;
        root->right = build(mid + 1, right);

        return root;
    }

    TreeNode* sortedListToBST(ListNode* head) {
        int n = 0;
        ListNode* temp = head;
        while (temp) {
            n++;
            temp = temp->next;
        }

        curr = head;
        return build(0, n - 1);
    }
};