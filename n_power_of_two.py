def is_powerOf2(m):
    return m != 0 and ((m & (m-1)) == 0)

assert not is_powerOf2(6) 
assert is_powerOf2(8)
assert not is_powerOf2(0)