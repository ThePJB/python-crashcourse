def check(message, a, b):
    make_text_red = "\033[031m"
    make_text_green = "\033[032m"
    make_text_normal =  "\033[037m"

    if (a == b):
        print(make_text_green, message, ": correct (", a, ")", make_text_normal)
    else:
        print(make_text_red, message, ": incorrect (should have been", b, "but it was", a,")", make_text_normal)


def main():
    check("double 3", double(3), 6)
    check("double 8", double(8), 16)
    check("double 453405098", double(453405098), 906810196)

    check("cube 1", cube(1), 1)
    check("cube 2", cube(2), 8)
    check("cube 123123", cube(123123), 1866455185461867)

    check("cube_if_even 1", cube_if_even(1), 1)
    check("cube_if_even 2", cube_if_even(2), 8)
    check("cube_if_even 3", cube_if_even(3), 3)

    check("collatz 1", collatz(1), 0)
    check("collatz 4", collatz(4), 2)
    check("collatz 10", collatz(10), 6)
    check("collatz 69", collatz(69), 14)
    check("collatz 1069", collatz(1069), 23)

    check("add 1 2", add(1,2), 3)
    check("add 1 100", add(1,100), 101)
    check("add 169 1300", add(169,1300), 1469)
    
    check("max 0 2", max(0,2), 2)
    check("max -10 100", max(-10,100), 100)
    check("max 1234345 345345987", max(1234345,345345987), 345345987)

    check("max3 0 2 5", max3(0,2,5), 5)
    check("max3 -10 100 13", max3(-10,100, 13), 100)
    check("max3 1234345 345345987 1", max3(1234345,345345987,1), 345345987)

    check("which_max3 0 2 5", which_max3(0,2,5), 2)
    check("which_max3 -10 100 13", which_max3(-10,100, 13), 1)
    check("which_max3 345345987 1 2", which_max3(345345987,1,2), 0)

    check("euclid_gcd 9 13", euclid_gcd(9,13), 1)
    check("euclid_gcd 27 36", euclid_gcd(27,36), 9)
    check("euclid_gcd 49 63", euclid_gcd(49,63), 7)

    check("head 1 2 3 4 5 6", head([1,2,3,4,5,6]), 1)
    check("head 69 100 200", head([69, 100, 200]), 69)
    check("head 4", head([4]), 4)

    check("tail 1 2 3 4 5 6", tail([1,2,3,4,5,6]), [2,3,4,5,6])
    check("tail 69 100 200", tail([69, 100, 200]), [100,200])
    check("tail 4", tail([4]), [])

    check("sum_list 1 2 3 4 5 6", sum_list([1,2,3,4,5,6]), 21)
    check("sum_list -10 100 -200 301", sum_list([-10, 100, -200, 301]), 191)
    check("sum_list -10 -50 -20 -5", sum_list([-10, -50, -20, -5]), -85)
    
    check("max_list 1 2 5 4 3 7 6", max_list([1, 2, 5, 4, 3, 7, 6]), 7)
    check("max_list 100 200 605 600", max_list([100, 200, 605, 600]), 605)
    check("max_list -80 -60 10 20", max_list([-80, -60, 10, 20]), 20)

    check("max_index 1 2 5 4 3 7 6", max_index([1, 2, 5, 4, 3, 7, 6]), 5)
    check("max_index 100 200 605 600", max_index([100, 200, 605, 600]), 2)
    check("max_index -80 -60 10 20", max_index([-80, -60, 10, 20]), 3)

    check("e_to_3 I need help", e_to_3("I need help"), "I n33d h3lp")
    check("e_to_3 e_to_3", e_to_3("e_to_3"), "3_to_3")
    check("e_to_3 eee333eee", e_to_3("eee333eee"), "333333333")

    check("delete_second_word", delete_second_word("I need help"), "I help")
    check("im no good at programming", delete_second_word("im no good at programming"), "im good at programming")
    check("pineapple on pizza", delete_second_word("pineapple on pizza"), "pineapple pizza")



# general tips:
# if you get should have been X but it was None: maybe you forgot to return from the function
# feel free to make your own test cases or call your functions down before main etc
# if you are confused print stuff out, you can also print out the type of something with print(type(x))
# check that its a list if you are trying to do list stuff on it etc

# single variable

def double(x):
    return 0

def cube(x):
    return 0

def cube_if_even(x):
    return 0

'''
See the collatz conjecture
keep doing this until you get 1:
    if x is even, divide it by 2
    if x is odd, times 3 plus 1

count how many steps it took and return that
'''
def collatz(x):
    count = 0
    while x > 1:
        count += 1
        if x % 2 == 0:
            x = x / 2
        else:
            x = x * 3 + 1
    return count



# multiple variables
def add(x,y):
    return x+y

# return which is greater
def max(x,y):
    if x > y:
        return x
    return y

# as before but there are 3 variables
def max3(x,y,z):
    if x > y:
        if x > z:
            return x
        if z > y:
            return z
    else:
        if y > z:
            return y
        return z

# return the position of the max one, i.e. 0 for x, 1 for y, 2 for z
def which_max3(x,y,z):
    if x > y:
        if x > z:
            return 0
        if z > y:
            return 2
    else:
        if y > z:
            return 1
        return 2

'''
return the greatest common divisor of x and y

google euclids algorithm (google is the main skill of software development)
'''
def euclid_gcd(x,y):
    if x == 0:
        return y
    if y == 0:
        return x
    return euclid_gcd(y % x, x)

# lists
# return just the first element of the list
def head(xs):
    return xs[0]

# return all but the first element of the list
def tail(xs):
    return xs[1:]

# hint: for x in xs:
def sum_list(xs):
    acc = 0
    for x in xs:
        acc += x
    return acc

def max_list(xs):
    max = float('-inf')
    for x in xs:
        if x > max:
            max = x
    return max


# hint: for (i,x) in enumerate(xs):
def max_index(xs):
    max = float('-inf')
    max_index = 0
    for (i,x) in enumerate(xs):
        if x > max:
            max = x
            max_index = i
    return max_index

# strings
# hint: list stuff works on strings as well
# you can concatenate strings with +

# replace all e's with 3's
# hint: writing to the loop variable doesnt work because its a copy
def e_to_3(s):
    acc  = ""
    for c in s:
        if c == 'e':
            acc += '3'
        else:
            acc += c
    return acc

# hint: s.split()
def delete_second_word(s):
    acc = ""
    ss = s.split()
    acc += ss[0]
    for x in ss[2:]:
        acc += ' '
        acc += x
    return acc

main()

