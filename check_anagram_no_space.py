def anagram(word, anagram_word):
    word = word.lower()
    ordered_word = ''.join(sorted(word))
    ordered_word = ordered_word.strip()
    
    anagram_word = anagram_word.lower()
    ordered_anagram_word = ''.join(sorted(anagram_word))
    ordered_anagram_word = ordered_anagram_word.strip()
    #print(ordered_anagram_word, ordered_word)
    if ordered_anagram_word == ordered_word:
        return 1
    else:
        return 0

assert(anagram('asdf', ' asdf')) == 1
assert(anagram('sdd', 'wer')) == 0
