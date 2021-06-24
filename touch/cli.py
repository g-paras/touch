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


if __name__ == "__main__":
    create_file()
