object Solution {
    def climbStairs(n: Int): Int = {
        if(n <= 2) {return n}
        var a: Int = 1
        var b: Int = 2
        var steps: Int = 2
        while(steps < n){
            var c = a + b
            a = b
            b = c
            steps = steps + 1
        }
        b
    }
}
