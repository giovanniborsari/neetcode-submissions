class Solution {
    public boolean isAnagram(String s, String t) {

        //Compare length, false if different
        if (s.length() != t.length()){
            return false;
        }

        //Create arrays with the strings
        char[] slist = s.toCharArray();
        char[] tlist = t.toCharArray();

        //Sort both arrays
        Arrays.sort(slist);
        Arrays.sort(tlist);
        
        //Compare sorted arrays, if true it is an anagram
        return(Arrays.equals(slist,tlist));
    }
}
