import Math.min


object Solution {
    def longestCommonPrefix(strs: Array[String]): String = {
        strs.reduceLeft(_longestCommon)
    }

    private def _longestCommon(first: String, second: String): String = {
        var result = ""
        for(i <- 0 to min(first.length(), second.length())-1) {
            if(first.charAt(i) == second.charAt(i)) {
                result = result + first.charAt(i)
            } else return result
        }
        result
    }
}