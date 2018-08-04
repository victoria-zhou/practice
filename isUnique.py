# def is_unique(a_String):
# 	string_set = set(a_String)
# 	return len(a_String) == len(string_set)


# def is_unique(a_string):
# 	char_count = {}
# 	for char in a_string:
# 		if char in char_count:
# 			return False
# 		else:
# 			char_count[char] = 1
# 	return True


def is_unique(a_string):
	char_count = set()
	for char in a_string:
		if char in char_count:
			return False
		else:
			char_count.add(char)
	return True
assert is_unique('asbcdefg xyz')
assert not is_unique('asdefef')			
