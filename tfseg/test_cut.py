
from tfseg import cut, lcut
from tfseg import posseg


def test_cut():
    ret = cut('我爱北京天安门')
    for x in ret:
        assert isinstance(x, str)


def test_lcut():
    ret = lcut('我爱北京天安门')
    assert isinstance(ret, list)
    assert isinstance(ret[0], str)


def test_posseg_cut():
    ret = posseg.cut('我爱北京天安门')
    for x in ret:
        assert isinstance(x, tuple)
        assert isinstance(x[0], str)
        assert isinstance(x[1], str)


def test_posseg_lcut():
    ret = posseg.lcut('我爱北京天安门')
    assert isinstance(ret, list)
    assert isinstance(ret[0], tuple)
    assert isinstance(ret[0][0], str)
    assert isinstance(ret[0][1], str)
