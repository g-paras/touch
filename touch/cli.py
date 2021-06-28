'''Implementation of touch command'''

from sys import argv


def create_file():
    # get all the arguments
    files = argv[1:]

    # print error message and return none if no arguments
    if not len(files):
        print("Filename missing")
        return

    # iterate over all the file names and create
    for file in files:
        try:
            open(file, 'a').close()
        except FileNotFoundError:
            print(f"'{file}' is an invalid path")
            return

    return


def read_file():
    if len(argv) != 2:
        print("Too many values to unpack" if len(
            argv) > 1 else "Filename missing")
        return
    else:
        filename = argv[1]
        try:
            with open(filename) as file:
                print(file.read())
        except FileNotFoundError:
            print(f"{filename} does not exist")
        except PermissionError:
            print("Access denied")
    return


if __name__ == "__main__":
    create_file()
