class Solution {
public:
    vector<int> parent;

    int find(int x) {
        if (parent[x] == x)
            return x;
        return parent[x] = find(parent[x]);
    }

    void unite(int a, int b) {
        a = find(a);
        b = find(b);

        if (a != b)
            parent[b] = a;
    }

    string findTheString(vector<vector<int>>& lcp) {
        int n = lcp.size();

        // Basic validation
        for (int i = 0; i < n; i++) {
            if (lcp[i][i] != n - i)
                return "";

            for (int j = 0; j < n; j++) {
                if (lcp[i][j] != lcp[j][i])
                    return "";

                if (lcp[i][j] > min(n - i, n - j))
                    return "";
            }
        }

        parent.resize(n);
        for (int i = 0; i < n; i++)
            parent[i] = i;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (lcp[i][j] > 0) {
                    unite(i, j);
                }
            }
        }

        vector<char> assigned(n, 0);
        string word(n, 'a');
        char ch = 'a';

        for (int i = 0; i < n; i++) {
            int root = find(i);

            if (assigned[root] == 0) {
                if (ch > 'z')
                    return "";

                assigned[root] = ch++;
            }

            word[i] = assigned[root];
        }

        vector<vector<int>> actual(n, vector<int>(n, 0));

        for (int i = n - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (word[i] == word[j]) {
                    actual[i][j] = 1;

                    if (i + 1 < n && j + 1 < n)
                        actual[i][j] += actual[i + 1][j + 1];
                }
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (actual[i][j] != lcp[i][j])
                    return "";
            }
        }

        return word;
    }
};