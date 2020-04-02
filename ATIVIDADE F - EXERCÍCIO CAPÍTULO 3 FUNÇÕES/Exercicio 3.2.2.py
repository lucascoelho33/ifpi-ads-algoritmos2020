def do_twice(function, a):
    function(a)
    function(a)



def print_spam(nome):
    print(nome)



do_twice(print_spam, 'Lucas')
