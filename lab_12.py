def file_link():
    n = int(input('Enter amount of files \n'))
    if n == 0:
        exit("Amount of files is zero!")
    linked_files = ""
    for i in range(n):
        file_name = input('Enter name of file \n')
        try:
            file = open(file_name, "r")
        except FileNotFoundError:
            print("File not found")
            continue
        linked_files += file.read()
        file.close()
    print(linked_files)


def longest_word(file):
    m = 0
    for word in file:
        s = len(word)
        if s > m:
            m = s
    print(m)
    for word in file:
        s = len(word)
        if s == m:
            print(word)


def num_sum():
    x = input('Enter the number \n')
    ssum = 0
    while x:
        try:
            x = float(x)
        except ValueError:
            print("Not number! Enter again")
            x = input()
            continue
        ssum += float(x)
        x = input('Enter the number \n')
    print(ssum)


def main():
    # file_link()
    # longest_word(open('test.txt', "r").read().split())
    # num_sum()
    return


if __name__ == '__main__':
    main()
