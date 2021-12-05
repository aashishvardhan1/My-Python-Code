def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "😀",
        ":(": "😥"
    }
    output = ''
    for word in words:
        output += emojis.get(word, word) + " "
    return output


text = input('>')
print(emoji_converter(text))




# Refer this code in EmojiConverter.py of Excercises directory!