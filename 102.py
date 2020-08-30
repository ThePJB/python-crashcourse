def check(message, a, b):
    # in case you are wondering about this crazy stuff, it changes the colour of text in the terminal if you print it out
    make_text_red = "\033[031m"
    make_text_green = "\033[032m"
    make_text_normal =  "\033[037m"

    if (a == b):
        print(make_text_green, message, ": correct (", a, ")", make_text_normal)
    else:
        print(make_text_red, message, ": incorrect (should have been", b, "but it was", a,")", make_text_normal)

def main():
    check("fizzbuzz 2", fizzbuzz(2), '2')
    check("fizzbuzz 3", fizzbuzz(3), 'fizz')
    check("fizzbuzz 5", fizzbuzz(5), 'buzz')
    check("fizzbuzz 9", fizzbuzz(9), 'buzz')
    check("fizzbuzz 15", fizzbuzz(15), 'fizzbuzz')
    check("fizzbuzz 45", fizzbuzz(45), 'fizzbuzz')

    check("fibonacci 0", fibonacci(0), 1)
    check("fibonacci 5", fibonacci(5), 21) # check
    check("fibonacci 8", fibonacci(8), 999898) # check

    check("factorial 0", factorial(0), 1)
    check("factorial 5", factorial(5), 120)
    check("factorial 10", factorial(10), 3628800)

    check("quadratic_roots x2 - 1", quadratic_roots((1, 0, 1)), (-1, 1))
    check("quadratic_roots x2 + 6x + 9", quadratic_roots((1, 6, 9)), (-3, -3))
    check("quadratic_roots -x2 + 5x + 6", quadratic_roots((-1, 5, 6)), (-6, -1))

    check("list sort [3 2 1]", list_sort([3, 2, 1]), [1, 2, 3])
    check("list sort [6 88 3 0 0 0 -3 2]", list_sort([6, 88, 3, 0, 0, 0, -3, 2]), [-3, 0, 0, 0, 2, 3, 6, 881, 2, 3])
    check("list sort [123 45 -55 -1 -infinity]", list_sort([123, 45, -55, -1, float("-inf")]), [float("-inf"), -55, -1, 45, 123])
    
    check("custom list sort [4 5 6 7 3 2 1], a < b", custom_list_sort([4, 5, 6, 7, 3, 2, 1], lambda a, b: a > b), [1, 2, 3, 4, 5, 6, 7])
    check("custom list sort [4 5 6 7 3 2 1], a > b", custom_list_sort([4, 5, 6, 7, 3, 2, 1], lambda a, b: a < b), [7, 6, 5, 4, 3, 2, 1])
    check("custom list sort [hello, this is a string, a, 1234, 1234567890], len a < len b", 
        custom_list_sort(["hello", "this is a string", "a", "1234", "1234567890"], lambda a,b: len(a) > len(b)),
        ["a", "1234", "hello", "1234567890", "this is a string"])

    check("list unique [a a a a b]", list_unique(["a", "a", "a", "a", "b"]), ["a", "b"])
    check("list unique [1,2,3,4]", list_unique([1,2,3,4]), [1,2,3,4])
    check("list unique [1,2,3,4,4,3,2,1,5]", list_unique([1,2,3,4,4,3,2,1,5]), [1,2,3,4,5])

    check("custom list remove [1, 2, 3, 4, 5, 6, 7, 8], x < 4", custom_list_remove([1,2,3,4,5,6,7,8], lambda x: x < 4), [5,6,7,8])
    check("custom list remove [1, 2, 3, 4, 5, 6, 7, 8], x even", custom_list_remove([1,2,3,4,5,6,7,8], lambda x: x % 2 == 0), [1,3,5,7])

    check("parse sum 3 + 4", parse_sum("3 + 4"), 7)
    check("parse sum 1+2+3+4", parse_sum("1+2+3+4"), 10)
    check("parse sum 0 + 9 + 234234 + 2", parse_sum("10 + 9 + 234234 + 2"), 234255)
    
def fizzbuzz(x):
    return ""

def fibonacci(x):
    return 0

def factorial(x):
    return 0

# takes 3 tuple
# return 2 tuple in ascending order
# duplicate roots are ok
def quadratic_roots(quadratic):
    return (0,0,0)

# ascending
def list_sort(xs):
    return [] 

def custom_list_sort(xs, comparison_func):
    return []

def list_unique(xs):
    return []

def custom_list_remove(xs, removal_func):
    return []

def parse_sum(s):
    return 0

main()

