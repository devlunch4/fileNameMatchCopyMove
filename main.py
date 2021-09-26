# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def make_list():
    import os

    path = "./resource"

    file_list = os.listdir(path)
    print("$$$ file_list:", file_list)
    list_file = open('./resource/list.txt', 'r').read().split('\n')
    print("$$$ list_file:", list_file)

    new_copy_list = []
    for x in file_list:
        for y in list_file:
            if y in x:
                if y is not None and y != "":
                    print("x", x)
                    print("y", y)
                    new_copy_list.append(x)
    print("$$$ new_list: ", new_copy_list)
    copy_move(new_copy_list)


def copy_move(new_copy_list):
    import shutil
    i = 0
    for file in new_copy_list:
        src = './resource/' + file
        print("$$$ file: ", file)
        dst = "./resource/copy/"
        shutil.copy2(src, dst)
        i += 1
        print("cnt copy_move i:", i)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    make_list()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
