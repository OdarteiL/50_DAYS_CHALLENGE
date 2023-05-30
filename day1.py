import math

def divide_or_square (a):
    if a % 5 == 0:
        return(math.sqrt(a))
    else:
        x = a %  5
        return(x) 

print(divide_or_square(21))


# ---------------- Second Question ---------------------

def longest_value(a):
    long_val = a.values()
    new_value = list(long_val)

    max_value = None
    max_length = 0

    max_value = max(new_value, key=len)
    return(max_value)


name = {"Ghana":"Accra", 
        "Algeria":"Algiers",  
        "Madagascar":"Antananarivo",
        "Angola":"Luanda"
    }

print(longest_value(name))



