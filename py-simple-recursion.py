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
    sum_array([1, 2, 3])


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


# adding each element of an array using recursion
def sum_array(array):
    print()



# run program
main()










