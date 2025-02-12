# Copyright (c) Recommenders contributors.
# Licensed under the MIT License.

from recommenders.utils.general_utils import invert_dictionary, get_number_processors


def test_invert_dictionary():
    d = {"a": 1, "b": 2}
    d_inv = invert_dictionary(d)
    assert d_inv == {1: "a", 2: "b"}


def test_get_number_processors():
    assert get_number_processors() >= 1
