names = {"John", "Achara"}
for name in names:
    if name.startswith("J"):
        print("Found")
        break
else:
    print("Not Found")

# Else in for-else works when for loop is not broken while completeley iterated

# Other languages are listed below.

# names = {"John", "Achara"}
# Found = False
# for name in names:
#     if name.startswith("J"):
#         print("Found")
#         Found = True
#         break
# if not Found:
#     print("Not Found")