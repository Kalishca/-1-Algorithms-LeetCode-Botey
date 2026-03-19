class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}                     # создаём пустой словарь
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hmap:    # проверяем, есть ли разница в словаре
                return hmap[difference], i  # возвращаем индекс, если условие True
            hmap[nums[i]] = i         # иначе запоминаем текущее число и его индекс