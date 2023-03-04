from pathlib import Path

# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

current =   Path("./data")
fichiers = current.glob("*.*")

mapping = {}

def ajouterRegle(nomChamp, colDebut, longueur):
    champ = {}
    champ[nomChamp] = longueur
    mapping[nomChamp] = colDebut

def listerRegles():
    for regle in mapping:
        print(regle, "\n")



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
