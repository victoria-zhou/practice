#!/bin/python3
import logging
logger = logging.getLogger()


def max_value(num, top_cut):
    return top_cut-1 if ((top_cut-1) | top_cut) <= num else top_cut-2


if __name__ == '__main__':
    test_data = (
        (5, 2, 1),
        (8, 5, 4),
        (2, 2, 0),
    )
    for num, top_cut, expected_value in test_data:
        assert max_value(num, top_cut) == expected_value
        logger.warning(
        f'max_value({num}, {top_cut}) -> {max_value(num, top_cut)} == {expected_value} <- (expected_value)')
