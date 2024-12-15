from following_js_url import *

def test_readjs():
    assert readjs("test1") == "TEST1"
    assert readjs("test2") == "test2\n22"

def test_deln():
    assert deln("") == ""
    assert deln("abc") == "abc"
    assert deln("qed\nabo") == "qedabo"
    assert deln("qed\nabo\n\nqed\nabo") == "qedaboqedabo"

def test_picurl():
    assert picurl("ふぃいあんヴぃ\"http:test\"daghjpe") == ["http:test"]

