from assigner import Assigner
from printer import Printer

full_list = ['Alaska', 'Northwest Territory', 'Greenland', 'Alberta', 'Ontario', 'Quebec', 'Western United States', 'Eastern United States', 'Central America', 'Venezuela', 'Peru', 'Brazil', 'Argentina', 'North Africa', 'Egypt', 'East Africa', 'Congo', 'South Africa', 'Madagascar', 'Iceland', 'Scandinavia', 'Ukraine', 'Great Britian', 'Northern Europe', 'Southern Europe', 'Western Europe', 'Indonesia', 'New Guinea', 'Western Australia', 'Eastern Australia', 'Siam', 'India', 'China', 'Mongolia', 'Japan', 'Irkutsk', 'Yakutsk', 'Kamchatka', 'Siberia', 'Afghanistan', 'Ural', 'Middle East']

assigner = Assigner()
scrambled_list = assigner.randomise(full_list)
printer = Printer()
printer.print_ters(assigner.chunk_territories(scrambled_list, 6))