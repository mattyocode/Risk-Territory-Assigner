import pytest
import random
from lib import Assigner

array = ['Kamchatka', 'Japan', 'Eastern Austrlia', 'Alaska', 'Northwest Territory']

subject = Assigner()

def test_split():
    assert subject.randomise(array, 2) != array