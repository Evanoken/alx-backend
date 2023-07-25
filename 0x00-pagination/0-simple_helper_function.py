#!/usr/bin/env python3

""" Simple helper function """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ Simple Pagination. """
    multiplier: int = page - 1
    return (multiplier * page_size, page * page_size)
