import pytest
from lib import Printer
from lib import Assigner

test_array = [['1', '7'], ['2', '8'], ['3', '9'], ['4', '10'], ['5', '11'], ['6', '12']]

subject = Printer()

class TestPrinter:  
    def test_print_string_6_player(self):
        assert subject.print_territories(test_array) == 'Player 1:\n1\n7\n\nPlayer 2:\n2\n8\n\nPlayer 3:\n3\n9\n\nPlayer 4:\n4\n10\n\nPlayer 5:\n5\n11\n\nPlayer 6:\n6\n12'