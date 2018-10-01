# Given two strings, determine if they share a common substring. A substring may be as small as one character.

#For example, the words "a", "and", "art" share the common substring . The words "be" and "cat" do not share a substring.

def two_strings(s1, s2):
    return 'YES' if set(s1).intersection(set(s2)) else 'NO'

assert two_strings('hello', 'world') == 'YES'
assert two_strings('hi', 'world') == 'NO'