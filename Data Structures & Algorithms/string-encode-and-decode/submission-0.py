class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_string = ""
        for i in strs:
            new_str = str(len(i)) + "#" + i
            enc_string += new_str
        return enc_string

    def decode(self, s: str) -> List[str]:
        array_str = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            lenght = int(s[i:j])
            word = s[j+1 : j+1+lenght]
            array_str.append(word)

            i = j + 1 + lenght


        return array_str

