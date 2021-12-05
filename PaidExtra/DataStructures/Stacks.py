browsing_stack = []
browsing_stack.append(1)
browsing_stack.append(2)
browsing_stack.append(3)
print(browsing_stack)

last = browsing_stack.pop()
print(last)
print(browsing_stack)
print(f'Redirect to website number {browsing_stack[-1]}')

# disabling the back button

# browsing_stack2 = []
# browsing_stack2.append(1)
# browsing_stack.pop()
# if not browsing_stack2:
#     print(browsing_stack[-1])
