"""
sample tests just to get started
"""


def test_one():
    assert 1 == 1


def test_two():
    expected = (1, 2)
    actual = (1, 2, 3)
    assert expected == actual


class TestSomeStuff:
     def test_three(self):
         assert {1, 2, 2} == {1, 2}

     def test_four(self):
         assert {1, 2, 2} == {1, 2}
