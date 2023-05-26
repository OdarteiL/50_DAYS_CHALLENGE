import math

def divide_or_square (a):
    if a % 5 == 0:
        print(math.sqrt(a))
    else:
        print(a) 

divide_or_square(11)


# ---------------- Second Question ---------------------

def longest_value(a):
    long_val = a.values()
    new_value = list(long_val)

    max_value = None
    max_length = 0

    max_value = max(new_value, key=len)
    print(max_value)

    # for value in new_value:
    #     if len(value) > max_length:
    #         max_length = len(value)
    #         max_value = value
    # print(max_value)

name = {"Ghana":"Accra", 
        "Algeria":"Algiers",  
        "Madagascar":"Antananarivo",
        "Angola":"Luanda"
    }

longest_value(name)



