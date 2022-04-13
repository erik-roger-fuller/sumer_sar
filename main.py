# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

import tabula

df = tabula.read_pdf("C:\\Users\\17742\\Downloads\\View PDF Statement_2021-03-31.pdf", pages = 1)[0]
print(df)

df20 = tabula.read_pdf("C:\\Users\\17742\\Downloads\\View PDF Statement_2020-12-23.pdf", pages='all', stream=True)

