# working with strings and the in statement

password = "12345"

#check to see if the password is "password"
if password == "password":
    print('passowrd is correct')

#check to see if the password is not "password"
if password != "password":
    print("the password is not correct")

#check to see if the word "pass" is contained somewhere in the password variable
if "pass" in password:
    print(f"pass is found in the password: {password}")

#check to see if the word "dog" is not located anywhere in your password
if "dog" not in password:
    print(f"dog is not found anywhere in {password}")

#check to see if a variable contents is found inside another variable
word = "cat"
phrase = "cat in the hat"
if word in phrase:
    print(f"the word '{word}' is found in the phrase'{phrase}'")