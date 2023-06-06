def canConstruct(ransomNote: str, magazine: str) -> bool:
    for letter in ransomNote:
        if letter not in magazine:
            return False
        else:
            magazine = magazine.replace(letter, "", 1)
    return True


print(canConstruct("a", "b"))
print(canConstruct("aa", "ab"))
print(canConstruct("aa", "aab"))
