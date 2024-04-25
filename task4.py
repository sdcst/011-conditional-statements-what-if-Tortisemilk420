#! python3

"""
Have the user enter in a sentence. 
Check to see if the word "password" is located in the sentence

Inputs:
a sentence

Outputs:
"the sentence contains password"
"the sentence does not contain password"

Examples:
Enter a sentence: I will not buy this record, it is scratched.
the sentence does not contain password

Enter a sentence: The best password is no password.
the sentence contains password
"""
word = "password"
sentence = "The best password is no password."
if word in sentence:
    print(f"the word '{word}' is found in the phrase'{sentence}'")

elif word not in sentence:
  print(f"the word '{word}' is not found in the phrase'{sentence}'")
 
   