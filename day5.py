def my_discount ():
    price = int(input("Please enter the price: "))
    discount_percentage = int(input("Please enter the discount: "))

    discount = price - (price * (discount_percentage/100))

    return discount

print(my_discount())

#---------------- Second question -----------------

def tuple_of_student_sex(a):
    male = []
    female = []


    for gender in students:
        if gender.lower() == "male":
            male.append(gender)
        elif gender.lower() == "female":
            female.append(gender)
        
        male_num = len(male)
        female_num = len(female)
        
        result_male = 'Male', male_num
        result_female = 'Female', female_num
        
        result = [result_male, result_female]

    return result

students = ['Male', 'Female', 'female', 'male', 'male', 'male', 'male',
'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female', 'female']

print(tuple_of_student_sex(students))