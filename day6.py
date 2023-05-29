def user_name():
    email_add = input("Please input your email address: ")
    splitted_email = email_add.split("@")
    sliced_email = splitted_email[ :1]

    for userName in sliced_email:
        return (f"Your user name is: {userName}")  
    
print(user_name())

#-----------------Second Question ----------------------------


def zeroed(a):
    if len(a) >= 2:
        a[0] = 0
        a[-1] = 0

    return a

sample_list = [1,2,3,4,5,6,7,8]

print(zeroed(sample_list))