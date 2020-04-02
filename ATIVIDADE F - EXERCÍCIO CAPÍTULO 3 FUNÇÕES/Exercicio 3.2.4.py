def do_twice(function, c):
    function(c)
    function(c)



def print_twice(lucas):
    print(lucas)
    print(lucas)


do_twice(print_twice, 'spam')
