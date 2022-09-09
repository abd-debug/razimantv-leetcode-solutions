// https://leetcode.com/problems/the-number-of-weak-characters-in-the-game

class Solution {
 public:
  int numberOfWeakCharacters(vector<vector<int>>& properties) {
    sort(properties.begin(), properties.end());

    int ret = 0;
    for (int n = properties.size(), i = n - 2, curworst = properties.back()[1],
             worst = 0;
         i >= 0; --i) {
      if (properties[i][0] == properties[i + 1][0])
        curworst = max(curworst, properties[i][1]);
      else
        worst = max(worst, curworst), curworst = properties[i][1];
      if (properties[i][1] < worst) ++ret;
    }
    return ret;
  }
};
