def check_character(str):
    words_list = str.split(' ')

    return len(words_list)


assert check_character('this is for test only') == 5
assert check_character('should be four words') == 4 