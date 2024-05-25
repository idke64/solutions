class Solution {
    public List<String> letterCombinations(String digits) {
        String[] mapping = {"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
        List<String> output = new ArrayList<String>();
        if (digits.length() == 0){
            return output;
        }
        helper(digits, output, "", mapping);
        return output;
    }
    public static void helper(String digits, List<String> output, String str, String[] mapping){
        if (str.length() == digits.length()){
            output.add(str);
        }
        else{
            int num = Character.getNumericValue(digits.charAt(str.length()));
            int ind = num - 2;
            String chars = mapping[ind];
            for (int i = 0; i < chars.length(); i++){
                helper(digits, output, str + chars.charAt(i), mapping);
            }

        }

    }
}