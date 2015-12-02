# @ brief
#       this is the main module to start the application
# @ build
#       2015 / 12 / 1

from tkinter import Tk
from application import Application


def main():
    "main function"

    root = Tk()

    # set title
    root.title("Visual Dictionary Tree")

    app = Application(root)

    app.mainloop()


if __name__ == "__main__":
    main()
