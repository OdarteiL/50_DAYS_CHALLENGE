def register_check(a):
    in_school = a.values()
    list_in_school = list(in_school)
    num_in_school = list_in_school.count("yes")

    return num_in_school


register = {'Michael':'yes',
            'John': 'no',
            'Peter':'yes', 
            'Mary': 'yes'
        }

print(register_check(register))

# --------------------- Second Question -------------------------

