def find_largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c
def count_vowels(word):
    vowels = "aeiou"
    count = 0
    for i in word.lower():
      if i in vowels:
         count += 1
         return count
def is_palindrome(word):
            word = word.lower()
            return word == word[::-1]
def reverse_string(s):
    return s[::-1]
def find_longest_word(sentence):
     words = sentence.split()
     longest_word = max(words, key=len)
      return longest_word
