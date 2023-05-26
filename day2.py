def convert_add (a):
    new_a = list(map(int, a))
    sum_a = sum(new_a)
    return sum_a


my_list = ["20", "100", "3", "10", "30"]
print(convert_add(my_list))

# ------------------- Second Question -------------------------

def check_duplicates(a):
    unique_list = []
    duplicate_list = []
    
    for duplicate in a:
        if duplicate not in unique_list:
            unique_list.append(duplicate)
        elif duplicate not in duplicate_list:
            duplicate_list.append(duplicate)
            new_list = duplicate_list

    if duplicate_list:
        return duplicate_list 


    else:
        print("no duplicates")
        return None


my_name = ["name", "kofi", "Me"] 
my_list = ["3", "100", "3", "10", "100", "100", "90", "4", "13", "4", "100", "100", "4", "19", "19"]

print(check_duplicates(my_name))



