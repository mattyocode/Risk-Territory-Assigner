from lib import Assigner
from lib import Printer

full_list = ['Alaska', 'Northwest Territory', 'Greenland', 'Alberta', 'Ontario', 'Quebec', 'Western United States', 'Eastern United States', 'Central America', 'Venezuela', 'Peru', 'Brazil', 'Argentina', 'North Africa', 'Egypt', 'East Africa', 'Congo', 'South Africa', 'Madagascar', 'Iceland', 'Scandinavia', 'Ukraine', 'Great Britian', 'Northern Europe', 'Southern Europe', 'Western Europe', 'Indonesia', 'New Guinea', 'Western Australia', 'Eastern Australia', 'Siam', 'India', 'China', 'Mongolia', 'Japan', 'Irkutsk', 'Yakutsk', 'Kamchatka', 'Siberia', 'Afghanistan', 'Ural', 'Middle East']

def get_players():
    print("Please enter number of players (2-6): ")
    input = input()
    number = int(input)
    return number 

def check_number_of_players(number):
    if (number < 2 or number > 6): 
        return True

assigner = Assigner()
scrambled_list = assigner.randomise(full_list)
printer = Printer()

number = 0 

print("Please enter number of players (2-6): ")
input = input()
number = int(input) 
print('Printing territories for {} players...\n'.format(number))
chunked_territories = assigner.chunk_territories(scrambled_list, number)
printer.print_territories(chunked_territories)





