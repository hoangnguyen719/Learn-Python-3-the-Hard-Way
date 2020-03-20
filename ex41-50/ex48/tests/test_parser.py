from ex48.parser import Sentence

def test_init():
    s = Sentence('bear hit the princess')
    assert s.scanned_string == [('noun', 'bear'), ('verb', 'hit'), ('stop', 'the'), ('noun', 'princess')]