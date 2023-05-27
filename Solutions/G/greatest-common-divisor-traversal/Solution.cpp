// https://leetcode.com/problems/greatest-common-divisor-traversal/

class Solution {
 public:
  bool canTraverseAllPairs(vector<int>& nums) {
    if (nums.size() == 1) return true;

    int x = *max_element(nums.begin(), nums.end());
    vector<int> par(x + 1);
    iota(par.begin(), par.end(), 0);
    function<int(int)> parent = [&](int u) {
      return (par[u] == u) ? u : (par[u] = parent(par[u]));
    };
    unordered_set<int> seen;
    for (int x : nums) seen.insert(x);
    if (seen.count(1)) return false;

    vector<char> notprime(x + 1);
    for (int i = 2; i <= x; ++i) {
      if (notprime[i]) continue;
      int u = parent(i);
      for (int j = i; j <= x; j += i) {
        notprime[j] = 1;
        if (seen.count(j)) par[parent(j)] = u;
      }
    }

    int u = parent(*seen.begin());
    for (int x : seen)
      if (parent(x) != u) return false;
    return true;
  }
};
