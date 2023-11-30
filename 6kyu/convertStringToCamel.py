""" 
DESCRIPTION:
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"

 """


def to_camel_case(text):
    words = text.replace("-", " ").replace("_", " ").split()
    if len(words) != 0:
        for i in range(1, len(words)):
            words[i] = words[i][0].upper() + words[i][1:]
        return "".join(words)
    else:
        return ""
