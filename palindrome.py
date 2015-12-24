def reverse(s):
    new = ''
    for x in range(len(s)-1, -1, -1):
        new+=s[x]
    return new

def is_palindrome(s):
    return s == reverse(s)

print (is_palindrome('aba'))
print (is_palindrome('abc'))

#other method of reversing string
def other(s):
    new = ''
    for x in s:
        new = x + new
    return new

print (other('help'))
