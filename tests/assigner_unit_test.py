import pytest
import random
from lib import Assigner

array = ['Kamchatka', 'Japan', 'Eastern Australia', 'Alaska', 'Northwest Territory', 'Iceland']
full_list = ['Alaska', 'Northwest Territory', 'Greenland', 'Alberta', 'Ontario', 'Quebec', 'Western United States', 'Eastern United States', 'Central America', 'Venezuela', 'Peru', 'Brazil', 'Argentina', 'North Africa', 'Egypt', 'East Africa', 'Congo', 'South Africa', 'Madagascar', 'Iceland', 'Scandinavia', 'Ukraine', 'Great Britian', 'Northern Europe', 'Southern Europe', 'Western Europe', 'Indonesia', 'New Guinea', 'Western Australia', 'Eastern Australia', 'Siam', 'India', 'China', 'Mongolia', 'Japan', 'Irkutsk', 'Yakutsk', 'Kamchatka', 'Siberia', 'Afghanistan', 'Ural', 'Middle East']

subject = Assigner()
class TestRandomiser:
    def test_randomise_returns_shuffled_array(self):
        assert subject.randomise(array) != array

class TestRandChunkTerritories:
    def test_iterate_over_shortlist_split_between_2(self):
        assert subject.rand_chunk_territories(array, 2) == [['Kamchatka', 'Eastern Australia', 'Northwest Territory'], ['Japan', 'Alaska', 'Iceland']]

    def test_iterate_over_shortlist_split_between_3(self):
        assert subject.rand_chunk_territories(array, 3) == [['Kamchatka', 'Alaska'], ['Japan', 'Northwest Territory'], ['Eastern Australia', 'Iceland']]

    def test_assign_full_list_to_6_players(self):
        assert subject.rand_chunk_territories(full_list, 6) == [['Alaska', 'Western United States', 'Argentina', 'Madagascar', 'Southern Europe', 'Siam', 'Yakutsk'], ['Northwest Territory', 'Eastern United States', 'North Africa', 'Iceland', 'Western Europe', 'India', 'Kamchatka'], ['Greenland', 'Central America', 'Egypt', 'Scandinavia', 'Indonesia', 'China', 'Siberia'], ['Alberta', 'Venezuela', 'East Africa', 'Ukraine', 'New Guinea', 'Mongolia', 'Afghanistan'], ['Ontario', 'Peru', 'Congo', 'Great Britian', 'Western Australia', 'Japan', 'Ural'], ['Quebec', 'Brazil', 'South Africa', 'Northern Europe', 'Eastern Australia', 'Irkutsk', 'Middle East']]

    def test_equal_nums_of_territories_when_6_players(self):
        assert len(subject.rand_chunk_territories(full_list, 6)[0]) == 7
        assert len(subject.rand_chunk_territories(full_list, 6)[5]) == 7

    def test_unequal_nums_of_ters_when_4(self):
        ters = subject.rand_chunk_territories(full_list, 4)
        assert len(ters[0]) == 11
        assert len(ters[1]) == 11
        assert len(ters[2]) == 10
        assert len(ters[3]) == 10
    
    def test_unequal_nums_of_ters_when_5(self):
        ters = subject.rand_chunk_territories(full_list, 5)
        assert len(ters[0]) == 9
        assert len(ters[1]) == 9
        assert len(ters[2]) == 8
        assert len(ters[3]) == 8
        assert len(ters[4]) == 8