def canMakeArithmeticProgression(arr: list[int]) -> bool:
    sorted_arr = sorted(arr)
    diff = sorted_arr[1] - sorted_arr[0]
    for i in range(1, len(sorted_arr)):
        if sorted_arr[i] - sorted_arr[i - 1] != diff:
            return False
    return True


print(canMakeArithmeticProgression([3, 5, 1]))
print(canMakeArithmeticProgression([1, 2, 4]))
print(canMakeArithmeticProgression([40, 1]))
