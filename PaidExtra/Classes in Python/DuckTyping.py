from abc import ABC, abstractmethod


class TextBox():
    def draw(self):
        print("TextBox")


class DropDownList():
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()


# there is no need of using a base class for acheiving polymorphism.
# If we have individual draw methods for the objects that we pass in draw function,
#then python has no problem in executing like a polymorphism technique.
# "If it walks like duck and quacks like duck the it is a duck".