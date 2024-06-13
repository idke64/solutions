class Solution:
    def compress(self, chars: List[str]) -> int:
        curr_count = 1
        curr_ind = 0
        end = 0
        for i in range(1,len(chars) + 1):
            if i == len(chars) or chars[i] != chars[i-1]:
                digits = int(math.log10(curr_count)) + 1
                chars[curr_ind] = chars[i-1] 
                if curr_count != 1:
                    for j in range(digits):
                        chars[curr_ind + j + 1] = str(int((curr_count % (10 ** (digits - j))) / 10 ** (digits - j - 1)))
                    end = curr_ind + digits
                    curr_ind += digits
                else:
                    end = curr_ind
                curr_count = 1
                curr_ind += 1
            else:
                curr_count += 1

        return end + 1
