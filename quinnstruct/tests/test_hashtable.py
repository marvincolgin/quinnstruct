import pytest
from ..hashtable import HashTable


def test_exists():
    assert HashTable


def test_hash_makeHash_deterministic():
    ht = HashTable()
    assert ht._makeHash('taco') == ht._makeHash('taco')


def test_hash_makeHash_deterministic_diff():
    ht = HashTable()
    assert not ht._makeHash('taco') == ht._makeHash('bell')


def test_hash_delete():
    ht = HashTable()
    ht.add('spam','eggs')
    ht.delete('spam')

    with pytest.raises(ValueError):
        ht.get('spam')

def test_hash_update():
    ht = HashTable()
    ht.add('spam', 'eggs')
    ht.update('spam', 'email')
    ht.get('spam') == 'email'


def test_hash_add():
    ht = HashTable()
    ht.add('spam','eggs')
    assert ht.get('spam') == 'eggs'


def test_hash_add_alreadyexists():
    ht = HashTable()
    ht.add('spam','eggs')

    with pytest.raises(ValueError):
        ht.add('spam','email')

def test_get_missing():
    ht = HashTable()

    # do this or test for return of None if you go that way
    with pytest.raises(ValueError):
        ht.get('spam')


def test_contains():
    ht = HashTable()
    ht.add('spam','eggs')
    assert ht.contains('spam')


def test_not_contains():
    ht = HashTable()
    assert not ht.contains('spam')


def test_hashIdx_in_range():
    ht = HashTable()
    assert  0 <= ht._getHashIndex(ht._makeHash('eggs')) < len(ht._data)


def test_collision():
    ht = HashTable()
    ht.add('spam','spammy stuff')
    ht.add('maps', 'mappy stuff')
    assert ht.get('spam') == 'spammy stuff'
    assert ht.get('maps') == 'mappy stuff'

def test_export_keys():
    ht = HashTable()
    for x in range(10):
        ht.add(str(x), 1)
    actual = ht.export_keys()
    expected = []
    for x in range(10):
        dict = {
            'name': str(x),
            'value': 1
        }
        expected.append(dict)
    actual = sorted(actual, key = lambda i: i['name'])
    expected = sorted(expected, key = lambda i: i['name'])
    assert expected == actual