class Printer:

    def print_ters(self, arr):
        string = 'Player 1: '
        line_break = "\n"
        #for item in arr:
            # return "{}: {} {}".format(string, item, line_break) 
            # string.join(map(string,arr))
        # output = '\n'.join(arr(x) for x in arr)  # list comprehension
        output = '\n'.join(arr[0]) 
        return string + output
            # ', '.join(str(x) for x in list)
        # return string
