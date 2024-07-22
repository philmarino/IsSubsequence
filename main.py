def isSubsequence(long, short):
    offset = 0
    for letter in short:
        offset = long.find(letter, offset)
        if offset < 0:
            return False

    return True

# Example 1:
# Input: 
s = "abc"
t = "ahbgdc"
print(isSubsequence(t, s))
# Output: true

# Example 2:
# Input: 
s = "axc"
t = "ahbgdc"
print(isSubsequence(t, s))
# Output: false
 