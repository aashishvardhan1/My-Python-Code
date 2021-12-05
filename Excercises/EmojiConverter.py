message = input(">")
words = message.split(" ")

# print(words)    # Test this by removing hash for understanding how split method works

emojis = {
    ":)": "😀",
    ":(": "😥"
}
output = ''
for word in words:
    output += emojis.get(word,word) + " "

print(output)