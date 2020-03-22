from ex48.parser import Sentence, ParserException
import pytest
import re

length_msg = "Incorrect number of keywords: {} was given (2 to 4 required)"
error_msg = "Error keyword: {}"
format_msg = "Incorrect keyword format:\n\t(given): {}\n\t(required): {}"
format_default = "[Noun], Verb, [Number,] Noun"

def length_message(n):
    return length_msg.format(n)

def test_string_length():
    with pytest.raises(ParserException) as error1: Sentence("")
    assert error1.value.args[0] == length_message(0)
    with pytest.raises(ParserException) as error2: Sentence("bear")
    assert error2.value.args[0] == length_message(1)
    with pytest.raises(ParserException) as error3: Sentence("asdasdasdsad")
    assert error3.value.args[0] == length_message(1)
    with pytest.raises(ParserException) as error4: Sentence("one two three four five")
    assert error4.value.args[0] == length_message(5)

def error_message(w):
    return error_msg.format(w)

def test_error():
    with pytest.raises(ParserException) as error1: Sentence("Bear hit asd")
    assert error1.value.args[0] == error_message('asd')
    with pytest.raises(ParserException) as error2: Sentence("error1 error2 error3")
    assert error2.value.args[0] == error_message('error1')

def format_message(f):
    return format_msg.format(", ".join(f), format_default)

def test_format():
    with pytest.raises(ParserException) as error1: Sentence("Bear kill the")
    assert error1.value.args[0] == format_message(['noun', 'verb'])
    with pytest.raises(ParserException) as error2: Sentence("Bear the princess")
    assert error2.value.args[0] == format_message(['noun', 'noun'])
    with pytest.raises(ParserException) as error3: Sentence("Bear 0.345")
    assert error3.value.args[0] == format_message(['noun', 'number'])
    with pytest.raises(ParserException) as error4: Sentence("Bear hit 0.345")
    assert error4.value.args[0] == format_message(['noun', 'verb', 'number'])
    with pytest.raises(ParserException) as error5: Sentence("hit princess bear")
    assert error5.value.args[0] == format_message(['verb', 'noun', 'noun'])

def test_output():
    output1 = Sentence("kill bear")
    assert output1.subj == 'player'
    assert output1.verb == 'kill'
    assert output1.obj == 'bear'
    assert output1.sentence == "player kill bear"

    output2 = Sentence("the FUCKING princess HiT the bear")
    assert output2.subj == 'princess'
    assert output2.verb == 'hit'
    assert output2.obj == 'bear'
    assert output2.sentence == "princess hit bear"

    output3 = Sentence("go to 2 bear")
    assert output3.subj == 'player'
    assert output3.verb == 'go'
    assert output3.obj == '2 bear'
    assert output3.sentence == "player go 2 bear"

    output4 = Sentence("the pRiNcEsS kill 719.3 fucKiNG bear")
    assert output4.subj == 'princess'
    assert output4.verb == 'kill'
    assert output4.obj == '719.3 bear'
    assert output4.sentence == "princess kill 719.3 bear"