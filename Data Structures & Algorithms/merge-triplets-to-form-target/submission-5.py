class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found_indexes = set()

        for triplet in triplets:
            # if triple has value larger than target -> cannot be used
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue

            # here, all valid triplets can be used
            # look for value
            for i in range(3):
                if triplet[i] == target[i]:
                    found_indexes.add(i)

        return len(found_indexes) == 3


        