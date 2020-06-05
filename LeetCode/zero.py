# 题目大意：
# 给定一个数组nums，编写函数将数组内所有0元素移至数组末尾，并保持非0元素相对顺序不变。
#
# 例如，给定nums = [0, 1, 0, 3, 12]，调用函数完毕后， nums应该是 [1, 3, 12, 0, 0]。
#
# 注意：
#
# 你应该“就地”完成此操作，不要复制数组。
# 最小化操作总数。


def move_zeros1(nums):
    l = len(nums)
    j = 0
    for i in range(0, l):
        if nums[i] == 0 and nums[j] == 0:
            pass
        elif nums[i] == 0 and nums[j] != 0:
            j = i
        elif nums[i] != 0 and nums[j] == 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
        elif nums[i] != 0 and nums[j] != 0:
            pass


def move_zeros2(nums):
    l = len(nums)
    j = 0
    for i in range(0, l):
        if nums[i] == 0 and nums[j] != 0:
            j = i
        elif nums[i] != 0 and nums[j] == 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1


def move_zeros3(nums):
    l = len(nums)
    j = 0
    for i in range(0, l):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1


def main():
    nums = [2, 0, 1, 0, 3, 12, 0, 0, 0, 0, 0, 0, 0, 12, 8, 0]
    move_zeros2(nums)
    print(nums)


if __name__ == '__main__':
    main()


