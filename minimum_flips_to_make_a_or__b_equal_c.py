def minFlips(a: int, b: int, c: int) -> int:
    count = 0
    while a or b or c:
        if (a & 1 == 1) and (b & 1 == 1) and (c & 1 == 0):
            count += 2
        elif (a & 1 == 0 and b & 1 == 0 and c & 1 == 1
              or a & 1 == 0 and b & 1 == 1 and c & 1 == 0
              or a & 1 == 1 and b & 1 == 0 and c & 1 == 0
              ):
            count += 1
        a >>= 1
        b >>= 1
        c >>= 1
    return count


print(minFlips(2, 6, 5))  # 3
print(minFlips(4, 2, 7))  # 1
print(minFlips(1, 2, 3))  # 0
print(minFlips(7, 7, 7))  # 0
