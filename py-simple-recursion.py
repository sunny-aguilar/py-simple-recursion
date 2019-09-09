# recursive function that shows the base case
# and recursive
def main():
    print("Recursive subtraction")
    count_down(5)

    print("Factorials")
    print(factorial(5))


# recursive function that prints i until i = 0
def count_down(i):
    print(i)
    if i == 0:      # base case
        return
    else:           # recursive case
        count_down(i - 1)


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


# run program
main()










