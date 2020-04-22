import pytest
from lib import Printer
from lib import Assigner

full_list = ['Alaska', 'Northwest Territory', 'Greenland', 'Alberta', 'Ontario', 'Quebec', 'Western United States', 'Eastern United States', 'Central America', 'Venezuela', 'Peru', 'Brazil', 'Argentina', 'North Africa', 'Egypt', 'East Africa', 'Congo', 'South Africa', 'Madagascar', 'Iceland', 'Scandinavia', 'Ukraine', 'Great Britian', 'Northern Europe', 'Southern Europe', 'Western Europe', 'Indonesia', 'New Guinea', 'Western Australia', 'Eastern Australia', 'Siam', 'India', 'China', 'Mongolia', 'Japan', 'Irkutsk', 'Yakutsk', 'Kamchatka', 'Siberia', 'Afghanistan', 'Ural', 'Middle East']
array = ['Kamchatka', 'Japan', 'Eastern Australia', 'Alaska', 'Northwest Territory', 'Iceland']

subject = Printer()
assigner = Assigner()
scrambled_ters = assigner.randomise(array)
assigned_array = assigner.chunk_territories(scrambled_ters, 2)

class TestPrinter:
    def test_print_string_player1(self):
        print('subject.print_ters(assigned_array)', subject.print_ters(assigned_array))
        assert subject.print_ters(assigned_array) == "Player 1:\nKamchatka\nEastern Australia\nNorthwest Territory\n\nPlayer 2:\nJapan\nAlaska\nIceland"
  