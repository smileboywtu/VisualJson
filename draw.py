# @ brief
#       draw the tree to an image
# @ build
#       2015 / 12 / 1

import ast
import json
import base64
from graphviz import Graph
from tkinter  import Label
from tkinter  import Toplevel
from tkinter  import PhotoImage


__all__ = ["Draw"]


class Draw(Toplevel):
    "draw the tree to picture"

    def __init__(self, parent):
        """
            @ brief
                initializa the Draw class
            @ params
                self    -- new instance
                """
        super(Draw, self).__init__(parent)
        self.transient(parent)
        self.title("current view")
        self.grab_set()

    def initDot(self):
        "init the pane"
        self.__dot = Graph()
        self.__dot.format = "gif"
        self.__dot.filename = "instance"
        self.__dot.attr('node', shape="circle")

    def setSource(self, source, with_label):
        "set the source text"
        self.node_suffix = 0
        self.__tree = ast.literal_eval(source)
        if with_label:
            self.draw = self.__drawHasLabel
        else:
            self.draw = self.__drawNoLabel

    def getTree(self):
        "return the tree"
        return self.__tree

    def __drawNoLabel(self, tree, root="tree"):
        "draw the tree without label on edge"
        self.__dot.body.extend(["rank=same", "rankdir=TD"])
        for key in tree.keys():
            self.__dot.edge(root, key)
            if type(tree[key]) is dict:
                self.__drawNoLabel(tree[key], str(key))
            else:
                node_name = str(key) + str(self.node_suffix)
                self.__dot.node(node_name, str(tree[key]))
                self.__dot.edge(str(key), node_name)
                self.node_suffix += 1
        return self.__dot.pipe(format="gif")

    def __drawHasLabel(self, tree):
        "draw the tree with label on edge"
        self.__dot.body.extend(["rank=same", "rankdir=TD"])
        for key in tree.keys():
            if type(tree[key]) is dict:
                for key_ in tree[key]:
                    if type(tree[key][key_]) is dict:
                        child = next(iter(tree[key][key_].keys()))
                        self.__dot.edge(key, child, str(key_))
                        self.__drawHasLabel(tree[key][key_])
                    else:
                        node_name = str(key) + str(self.node_suffix)
                        self.__dot.node(node_name, tree[key][key_])
                        self.__dot.edge(key, node_name, str(key_))
                        self.node_suffix += 1
        return self.__dot.pipe(format="gif")

    def show(self):
        "show the image"

        tree = self.getTree()
        image = self.draw(tree)
        if image is not None:
            label_image = PhotoImage(data=base64.b64encode(image))
            image_label = Label(self, image=label_image)
            image_label.photo = label_image
        else:
            image_label = Label(self, text="no image view")

        image_label.pack()
        self.wait_window(self)
