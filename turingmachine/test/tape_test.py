import pytest

from turingmachine.tape import Tape


def test_read():
    tape = Tape(list('foo'))

    assert tape.read(0) == 'f'
    assert tape.read(1) == 'o'
    assert tape.read(2) == 'o'
    assert tape.read(3) is None

def test_read_negative():
    tape = Tape(list('foo'))

    with pytest.raises(IndexError):
        tape.read(-1)

def test_write():
    tape = Tape(list('foo'))

    tape.write(0, 'b')
    tape.write(1, None)

    assert tape.read(0) == 'b'
    assert tape.read(1) == None

def test_write_negative():
    tape = Tape(list('foo'))

    with pytest.raises(IndexError):
        tape.write(-1, 'a')

def tape_list():
    tape = Tape(list('foo'))
    tape.write(4, 'a')

    assert tape.list() == ['f', 'o', 'o', None, 'a']

def test_str():
    tape = Tape(list('foobar'))
    tape.write(8, None)

    assert str(tape) == 'foobar___'
