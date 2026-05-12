class Solution {
public:
    bool isValid(string s) {
        std::stack<char> stack;

        std::map<char, char> closeToOpen = {
            {')', '('},
            {'}', '{'},
            {']', '['}
        };

        for (int i = 0; i < s.size(); i++){
            auto it = closeToOpen.find(s[i]);
            if (it != closeToOpen.end()){
                if(!stack.empty() && stack.top() == it->second){
                    stack.pop();
                }
                else{
                    return false;
                }
            }
            else{
                stack.push(s[i]);
            }  
        }

        return stack.empty();
        
    }
};
