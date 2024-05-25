use std::cmp;

impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 {
            return false;
        }
        if (x == 0){
            return true;
        }
        let digits = x.abs().ilog(10) + 1;
        for i in 0..(digits / 2){
            let digitl = Self::find_digit_from_left(x, i, digits);
            let digitr = Self::find_digit_from_left(x, digits - (i + 1), digits);
            println!("{} {} {}", digitl, digitr, digits);
            if digitl != digitr{
                
                return false;
            }
        }
        return true;
    }

    fn find_digit_from_left(num: i32, ind: u32, digits: u32) -> i32{
        let digit: i32 = (num / 10_i32.pow(digits - 1 - ind)) % 10;
        return digit;
    }
}