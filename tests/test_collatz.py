"""
Test the collatz module.
"""
import pytest
import collatz

def test_hotpo():
    assert 5 == collatz.hotpo(10)
    assert 16 == collatz.hotpo(5)

import unittest

class TestHotpo(unittest.TestCase):
    def test(self):
        self.assertEqual(5, collatz.hotpo(10))
        self.assertEqual(16, collatz.hotpo(5))

import pytest
from unittest.mock import Mock, call

@pytest.fixture
def mock_hotpo(monkeypatch):
    m = Mock(name='mock hotpo', side_effect=[4, 2, 1])
    monkeypatch.setattr(collatz, 'hotpo', m)
    return m

def test_iterate_from(mock_hotpo):
    results = list(collatz.iterate_from(42))
    assert results == [42, 4, 2, 1]
    assert mock_hotpo.mock_calls == [
        call(42),
        call(4),
        call(2)
    ]
