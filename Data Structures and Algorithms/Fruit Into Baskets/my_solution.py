class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        max_cnt = 0
        count = {}

        for right in range(len(fruits)):
            fruit = fruits[right]
            count[fruit] = count.get(fruit, 0) + 1

            while len(count) > 2:
                count[fruits[left]] -= 1

                if count[fruits[left]] == 0:
                    del count[fruits[left]]

                left += 1

            max_cnt = max(max_cnt, right - left + 1)

        return max_cnt
