class Printer:

    def print_ters(self, array):
        string = ''
        counter = 0
        for i in array:
            counter += 1
            if counter > 1:
                string += '\nPlayer {}:'.format(counter)
            else:
                string += 'Player {}:'.format(counter)
            
            for x in i:
                string += '\n{}'.format(x)
        return string
