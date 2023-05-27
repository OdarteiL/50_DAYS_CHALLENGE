def only_floats(a, b):
    
    if isinstance(a, float) and isinstance(b, float):
        return 2
    elif isinstance(a, float) or isinstance(b, float):
        return 1
    else:
        return 0
    
print(only_floats(12.43, 3))

#-------------------- Second Question ----------------------

def word_index(a):
    max_length = 0
    max_index = 0 

    for index, word in enumerate(words1):
        if len(word) > max_length:
            max_length = len(word)
            max_index = index
        elif len(word) == max_length:
            return 0 
    return (max_index)

words1 = ["Hate", "vengeance", "remorse", "vengeance", "Hate"]

print(word_index(words1))