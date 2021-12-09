class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
# print(cloud.__tags)
cloud.add("python")
cloud.add("python")
cloud.add("python")
# print(cloud.__tags["PYTHON"])
print(cloud._TagCloud__tags)

# To make any of the attributes not accessible from out side the class, we 
# can rename that method or attribute to '__attribute'.
# Although it is made inaccesible, we can still view the type as shown in line 27.