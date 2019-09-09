
def main():
    count_down(5)


# recursive function that prints i until i = 0
def count_down(i):
    print(i)
    if i == 0:      # base case
        return
    else:           # recursive case
        count_down(i - 1)

# begin program
main()










