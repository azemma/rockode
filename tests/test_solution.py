
from creek import a001


def test_001():
    s = a001.Solution()
    ret = s.two_sum([1, 3, 5, 6], 9)
    assert ret == (3, 6)
    pass
