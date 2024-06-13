class Solution {
public:
    bool isValid(string word) {
        set<char> vowels({'a','e','i','o','u','A','E','I','O','U'});
        bool vowel = false;
        bool consonants = false;
        for (char c : word){
            cout << c << endl;
            if (vowels.contains(c)){
                vowel = true;
            }
            if (isalpha(c) && !vowels.contains(c)){
                consonants = true;
            }
            if (!isdigit(c) && !isalpha(c)){
                return false;
            }
        }
        if (vowel && consonants && word.length() > 2){
            return true;
        }
        return false;
    }
    
};