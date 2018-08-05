# def is_permutation(a_string, b_string):
# 	if len(a_string) != len(b_string):
# 		return False
# 	else:
# 		sorted_a = sorted(a_string)
# 		sorted_b = sorted(b_string)

# 		return sorted_a == sorted_b

def is_permutation(a_string, b_string):
	sorted_a = sorted(a_string)
	sorted_b = sorted(b_string)

	return sorted_a == sorted_b
assert not is_permutation('wer', 'wert')
assert not is_permutation('wer', 'werr')
assert is_permutation('wre', 'wer')
assert is_permutation('wreeee', 'eweere')