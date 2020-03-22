# DO BETTER RELATIVE IMPORT HERE BY USING PATH
from ex48 import lexicon

def test_directions():
    assert lexicon.scan("NORTH") == [('direction', 'north')]
    result = lexicon.scan("north SOUTH east")
    assert result == [('direction', 'north'),
                      ('direction', 'south'),
                      ('direction', 'east')]

def test_verbs():
    assert lexicon.scan("GO") == [('verb', 'go')]
    result = lexicon.scan("go KILL eat")
    assert result == [('verb', 'go'),
                      ('verb', 'kill'),
                      ('verb', 'eat')]

def test_stops():
    assert lexicon.scan("THE") == [('stop', 'the')]
    result = lexicon.scan("the in OF")
    assert result == [('stop', 'the'),
                      ('stop', 'in'),
                      ('stop', 'of')]

def test_nouns():
    assert lexicon.scan("BEAR") == [('noun', 'bear')]
    result = lexicon.scan("bear princess")
    assert result == [('noun', 'bear'),
                      ('noun', 'princess')]

def test_numbers():
    assert lexicon.scan("1234") == [('number', 1234)]
    result = lexicon.scan("3 91234")
    assert result == [('number', 3),
                     ('number', 91234)]

def test_errors():
    assert lexicon.scan("ASDASDASD") == [('error', 'ASDASDASD')]
    result = lexicon.scan("bear IAS PRINCESS")
    assert result == [('noun', 'bear'),
                      ('error', 'IAS'),
                      ('noun', 'princess')]

def test_empty():
    assert lexicon.scan("") == []