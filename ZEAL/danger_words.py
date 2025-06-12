

def load_danger_words(file_path):
    with open(file_path) as words_file:
        danger_words = [word.rstrip() for word in words_file]
    return danger_words

def GetDangerWords():
    return load_danger_words("concerning_words.txt")

def depressive_thought():
    return load_danger_words("depressive.txt")

def potential_struggle():
    return load_danger_words("potential_struggle.txt")

def destructive_thought():
    return load_danger_words("self_destructive.txt")
