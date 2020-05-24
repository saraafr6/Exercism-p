def abbreviate(words):
    acronym=[string[0].upper() for string in words.replace("-"," ").replace("_"," ").split()]
    return "".join(acronym)