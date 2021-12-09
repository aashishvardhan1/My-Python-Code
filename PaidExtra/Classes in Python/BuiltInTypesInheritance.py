class Text(str):
    def duplicate(self):
        return self +" "+ self


text = Text("Python")
print(text.duplicate())


class TrackableList(list):
    def append(self, object):
        print("Append Called")
        super().append(object)

list = TrackableList()
list.append("1")

# here we are not replacing any method, instead we are extending the properties
# of the built-in list class.

# In the above one, we are inheriting all the str methods to Text class.
# Also we can add new methods like duplicate, which doesn't exist in str class.