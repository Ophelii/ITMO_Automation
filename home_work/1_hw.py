def test_hw1():
    assert ('home', 'work') == ('home', 'work')


def test_hw2():
    assert 'QA' == 'QC'


def test_hw3():
    assert not (1, 1, 2, 3, 5) == (2, 3, 5)
