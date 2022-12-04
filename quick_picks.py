import random


def main():
    number_line = 6
    max_number = 45
    min_number = 1
    quick_picks = int(input("how many quick picks ? :"))
    while quick_picks < 0:
        print("not working try again")
        quick_picks = int(input("how many quick picks ? :"))

    for i in range(quick_picks):
        quick_pick = []
        for j in range(number_line):
            number = random.randint(min_number, max_number)
            while number in quick_pick:
                number = random.randint(min_number, max_number)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
