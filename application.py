# @ brief
#       this module design the application frame used in the
#       other module.
# @ author
#       smileboy
# @ build
#       2015 / 12 / 1
# @ tool
#       python3

from draw import Draw
from tkinter import Frame
from tkinter import BooleanVar
from tkinter import W, E, WORD, END
from tkinter import Button, Checkbutton, Label, Text

__all__ = ["Application"]


class Application(Frame):
    "application frame"

    def __init__(self, master):
        """
         @ brief
             initialize the frame with master
         @ params
             self    -- new instance
             master  -- root container
             """
        super(Application, self).__init__(master)

        self.grid()
        self.__createWidgets()

    def __createWidgets(self):
        """
            @ brief
                create the widgets
                """
        Label(self, text="input dictionary tree: ") \
            .grid(row=0, column=0, sticky=W)

        self.dict_with_label = BooleanVar()
        Checkbutton(self, text="label edge", variable=self.dict_with_label) \
            .grid(row=0, column=0, sticky=E)

        self.source_text = Text(self, width=40, wrap=WORD)
        self.source_text.grid(row=1, column=0, sticky=W)

        Button(self, text="visual tree",
               command=self.__submitSource) \
            .grid(row=2, column=0, sticky=W)

        Button(self, text="clear",
               command=self.__clearText)    \
            .grid(row=2, column=0, sticky=E)

    def __submitSource(self):
        "listener for visual button"
        source = self.source_text.get("1.0", END)
        if "" != source:
            current_view = Draw(self)
            current_view.initDot()
            current_view.setSource(source, self.dict_with_label.get())
            current_view.show()

    def __clearText(self):
        "clear button callback"
        self.source_text.delete(0.0, END)
