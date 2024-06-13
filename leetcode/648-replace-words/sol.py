class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        s = set(dictionary)
        arr = sentence.split(" ")
        for i in range(len(arr)):
            sub = ""
            for j in range(len(arr[i])):
                sub += arr[i][j]
                if sub in s:
                    arr[i] = sub
                    break
        return " ".join(arr)