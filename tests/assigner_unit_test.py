import pytest
import random
from lib import Assigner

array = ['Kamchatka', 'Japan', 'Eastern Australia', 'Alaska', 'Northwest Territory', 'Iceland']


subject = Assigner()

def test_randomise_returns_shuffled_array():
    assert subject.randomise(array) != array

def test_assign_shuffled_arrays_to_2_players():
    print('subject.assign(array, 2)', subject.assign(array, 2))
    assert subject.assign(array, 2) == [['Kamchatka', 'Japan', 'Eastern Australia'], ['Alaska', 'Northwest Territory', 'Iceland']]

def test_assign_shuffled_arrays_to_3_players():
    print('subject.assign(array, 3)', subject.assign(array, 3))
    assert subject.assign(array, 3) == [['Kamchatka', 'Japan'], ['Eastern Australia', 'Alaska'], ['Northwest Territory', 'Iceland']]
