def count_holes(countee):
    holey = {"4": 1, "6": 1, "8": 2, "9": 1, "0": 1}
    holes = [holey[i] for i in str(countee) if i in holey.keys()]
    return sum(holes)

if __name__ == "__main__":
    try:
        countee = int(input('Please enter an integer: '))
        print(count_holes(countee))
    except ValueError:
        print('Error')
