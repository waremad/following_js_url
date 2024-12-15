from following_js_url import *

def test_readjs():
    assert readjs("test1") == "TEST1"
    assert readjs("test2") == "test2\n22"

