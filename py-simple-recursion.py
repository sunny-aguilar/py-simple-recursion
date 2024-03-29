# Sandro Aguilar
# 09/2019
# recursive functions that shows the base case
# and recursive


def main():
    print("Recursive subtraction:")
    count_down(5)

    print("\nFactorials:")
    print(factorial(5))

    print("\nArray Sum:")
    print(sum_array([1, 2, 3, 4, 5]))


# recursive function that prints i until i = 0
def count_down(i):
    print(i)
    if i == 0:      # base case
        return
    else:           # recursive case
        count_down(i - 1)

# a factorial is computed using recursion
def factorial(x):
    if x == 1:
        return 1                        # base case
    else:
        return x * factorial(x - 1)     # recursive case


# sum on an array's elements using recursion
def sum_array(array):
    if len(array) == 1:                 # base case
        print("Base case reached")
        return array[0]
    else:
        total = array[0]                # recursive case
        array.pop(0)
        return total + sum_array(array)


# run program
main()










