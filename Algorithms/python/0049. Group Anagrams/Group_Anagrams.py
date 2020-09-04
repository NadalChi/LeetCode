class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
        dict = collections.defaultdict(list)
        for i in strs:
            key = 1
            for j in i:
                key += math.log(prime[ord(j) - ord('a')])
            #print(round(key, 10))
            dict[round(key, 10)].append(i)
        return dict.values()
        # dict = {}
        # for i in strs:
        #     dict.setdefault(tuple(sorted(i)), []).append(i)
            #dict[tuple(sorted(i))] = dict.setdefault(tuple(sorted(i)), []) + [i]
            #dict[tuple(sorted(i))] = dict.get(tuple(sorted(i)), []) + [i]
            #dict[tuple(sorted(i))] = dict.get(tuple(sorted(i)), []).append(i)#'NoneType' object has no attribute 'append'
            #https://stackoverflow.com/questions/26367812/appending-to-list-in-python-dictionary
        return dict.values()