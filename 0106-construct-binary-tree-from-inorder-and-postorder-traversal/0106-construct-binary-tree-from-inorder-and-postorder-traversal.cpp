class Solution {
public:
    unordered_map<int, int> inMap;
    int postIndex;

    TreeNode* build(vector<int>& inorder, vector<int>& postorder, int left, int right) {
        if (left > right) return nullptr;

        int rootVal = postorder[postIndex--];
        TreeNode* root = new TreeNode(rootVal);

        int index = inMap[rootVal];

        // IMPORTANT: build right first (because postorder is L-R-Root)
        root->right = build(inorder, postorder, index + 1, right);
        root->left = build(inorder, postorder, left, index - 1);

        return root;
    }

    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        postIndex = postorder.size() - 1;

        for (int i = 0; i < inorder.size(); i++) {
            inMap[inorder[i]] = i;
        }

        return build(inorder, postorder, 0, inorder.size() - 1);
    }
};