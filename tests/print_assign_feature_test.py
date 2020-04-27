import pytest
from lib import Printer
from lib import Assigner

full_list = ['Alaska', 'Northwest Territory', 'Greenland', 'Alberta', 'Ontario', 'Quebec', 'Western United States', 'Eastern United States', 'Central America', 'Venezuela', 'Peru', 'Brazil', 'Argentina', 'North Africa', 'Egypt', 'East Africa', 'Congo', 'South Africa', 'Madagascar', 'Iceland', 'Scandinavia', 'Ukraine', 'Great Britian', 'Northern Europe', 'Southern Europe', 'Western Europe', 'Indonesia', 'New Guinea', 'Western Australia', 'Eastern Australia', 'Siam', 'India', 'China', 'Mongolia', 'Japan', 'Irkutsk', 'Yakutsk', 'Kamchatka', 'Siberia', 'Afghanistan', 'Ural', 'Middle East']
array = ['Kamchatka', 'Japan', 'Eastern Australia', 'Alaska', 'Northwest Territory', 'Iceland']
test_array = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

subject = Printer()
assigner = Assigner()
assigned_array = assigner.chunk_territories(array, 2)
assigned_test_array = assigner.chunk_territories(test_array, 6)


class TestAll:
    def test_print_string_2_player(self):
        assert subject.print_territories(assigned_array) == 'Player 1:\nKamchatka\nEastern Australia\nNorthwest Territory\n\nPlayer 2:\nJapan\nAlaska\nIceland'
  
    def test_print_string_6_player(self):
        assert subject.print_territories(assigned_test_array) == 'Player 1:\n1\n7\n\nPlayer 2:\n2\n8\n\nPlayer 3:\n3\n9\n\nPlayer 4:\n4\n10\n\nPlayer 5:\n5\n11\n\nPlayer 6:\n6\n12'