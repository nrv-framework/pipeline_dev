import pytest
from nrvplinet import collatz

def test_collatz():
    assert collatz(6) == 3
    assert collatz(3) == 10
    assert collatz(1) == 4