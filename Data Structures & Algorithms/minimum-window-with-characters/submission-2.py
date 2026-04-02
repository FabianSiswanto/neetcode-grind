class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        t converted to need map:
        s: counter -> decrease counter if find match -> stop when all counter is 0

        is_valid -> missing is 0, start with len(t)

        r move until is_valid
        l move while is_valid

        return s[l: r + 1]
        '''
        if t == "":
            return ""

        need_map = Counter(t)
        need = len(need_map)

        have_map = defaultdict(int)
        have = 0

        l = 0
        res = (0, 0)
        res_len = float("inf")

        for r in range(len(s)):
            c = s[r]
            have_map[c] += 1

            # update have condition
            if c in need_map and have_map[c] == need_map[c]:
                have += 1

            # check have and need condition
            while have == need:
                # update res
                cur_len = r - l + 1
                if cur_len < res_len:
                    res = [l, r]
                    res_len = cur_len

                # popleft
                to_remove = s[l]
                have_map[to_remove] -= 1

                # update have condition
                if to_remove in need_map and have_map[to_remove] < need_map[to_remove]:
                    have -= 1

                l += 1

        l, r = res
        return s[l: r + 1] if res_len != float("inf") else ""



            



        