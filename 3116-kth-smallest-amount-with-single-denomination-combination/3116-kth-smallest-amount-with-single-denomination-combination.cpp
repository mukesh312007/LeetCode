class Solution {
public:
    using ll = long long;

    ll lcm(ll a, ll b) {
        return a / std::gcd(a, b) * b;
    }

    ll count(ll x, vector<int>& coins) {
        int n = coins.size();
        ll total = 0;

        for (int mask = 1; mask < (1 << n); mask++) {
            ll L = 1;
            int bits = 0;
            bool overflow = false;

            for (int i = 0; i < n; i++) {
                if (mask & (1 << i)) {
                    bits++;

                    L = lcm(L, (ll)coins[i]);

                    if (L > x) {
                        overflow = true;
                        break;
                    }
                }
            }

            if (overflow)
                continue;

            ll cnt = x / L;

            if (bits % 2 == 1)
                total += cnt;
            else
                total -= cnt;
        }

        return total;
    }

    long long findKthSmallest(vector<int>& coins, int k) {
        ll low = 1;
        ll high = 1LL * (*min_element(coins.begin(), coins.end())) * k;

        while (low < high) {
            ll mid = low + (high - low) / 2;

            if (count(mid, coins) >= k)
                high = mid;
            else
                low = mid + 1;
        }

        return low;
    }
};