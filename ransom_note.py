def canConstruct2(ransomNote: str, magazine: str) -> bool:
    for letter in ransomNote:
        if letter not in magazine:
            return False
        magazine = magazine.replace(letter, "", 1)
    return True

def canConstruct(ransomNote: str, magazine: str) -> bool:
    if len(magazine) < len(ransomNote):
        return False
    letters = {}
    for letter in magazine:
        if not letters[letter]:
            letters[letter] = 1
    print(letters)
    return True

print(canConstruct("a", "b"))  # False
print(canConstruct("aa", "ab"))  # False
print(canConstruct("aa", "aab"))  # True
print(canConstruct("paymenow", "aemnopyy"))  # False
print(canConstruct("paymenow", "aemnopyyw"))  # True
