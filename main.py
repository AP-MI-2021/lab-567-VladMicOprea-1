from Tests.testsAll import runAllTests
from UI.console import runMenu
from UI.console_comands import Menu2


def main():
    runAllTests()
    print("1.consola veche")
    print("2.consola noua")
    console=int(input("dati nr consolei pe care vreti sa o alegeti"))
    if console == 1:
        runMenu([])
    elif console == 2:
        Menu2([])

if __name__ == '__main__':
    main()
