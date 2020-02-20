

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation += "K"
            else:
                translation += "k"
        else:
            translation += letter
    return translation

print(translate("Egg"))
