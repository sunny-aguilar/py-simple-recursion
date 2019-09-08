
def main():
    count_down(5)


def count_down(i):
    print(i)
    if i == 0:
        return 1
    else:
        count_down(i - 1)

main()










