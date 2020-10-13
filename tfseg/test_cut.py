
from tfseg import cut, lcut
from tfseg import posseg
from tfseg.pair import pair


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
        assert isinstance(x, pair)
        assert isinstance(x.word, str)
        assert isinstance(x.flag, str)


def test_posseg_lcut():
    ret = posseg.lcut('我爱北京天安门')
    assert isinstance(ret, list)
    assert isinstance(ret[0], pair)
    assert isinstance(ret[0].word, str)
    assert isinstance(ret[0].flag, str)
