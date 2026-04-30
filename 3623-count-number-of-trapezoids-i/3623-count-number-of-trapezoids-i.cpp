class Solution {
public:
    static const int MOD = 1e9 + 7;

    int countTrapezoids(vector<vector<int>>& points) {
        unordered_map<long long, long long> countY;

        // count points per y
        for (auto &p : points) {
            countY[p[1]]++;
        }

        vector<long long> ways;

        // compute C(cnt,2) for each level
        for (auto &[y, cnt] : countY) {
            if (cnt >= 2) {
                long long val = cnt * (cnt - 1) / 2;
                ways.push_back(val % MOD);
            }
        }

        long long sum = 0, sumSq = 0;

        for (long long w : ways) {
            sum = (sum + w) % MOD;
            sumSq = (sumSq + (w * w) % MOD) % MOD;
        }

        // (sum^2 - sumSq) / 2
        long long result = ( (sum * sum) % MOD - sumSq + MOD ) % MOD;

        // divide by 2 using modular inverse
        long long inv2 = (MOD + 1) / 2;
        result = (result * inv2) % MOD;

        return result;
    }
};