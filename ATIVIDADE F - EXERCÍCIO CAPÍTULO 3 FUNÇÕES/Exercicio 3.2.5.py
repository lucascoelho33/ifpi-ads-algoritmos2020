def do_twice(function, c):
    function(c)
    function(c)


def print_twice(lucas):
    print(lucas)
    print(lucas)


def do_four(function, c):
    do_twice(function, c)
    do_twice(function, c)


do_four(print_twice, 'spam')
