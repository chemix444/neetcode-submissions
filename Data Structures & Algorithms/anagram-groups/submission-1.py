class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - 97] += 1

            key = bytes(count)
            bucket = groups.get(key)
            if bucket is None:
                groups[key] = [word]
            else:
                bucket.append(word)

        return list(groups.values())
