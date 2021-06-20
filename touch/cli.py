from sys import argv


def create_file():
    try:
        file_name = argv[1]
        open(file_name, 'a').close()
    except IndexError:
        print('''Filename missing
Correct Syntax:
$ touch <filename>''')

    return


if __name__ == "__main__":
    create_file()
