// https://leetcode.com/problems/faulty-keyboard/

class Solution {
 public:
  string finalString(string s) {
    string ret;
    for (char c : s) {
      if (c == 'i')
        reverse(ret.begin(), ret.end());
      else
        ret += c;
    }
    return ret;
  }
};
