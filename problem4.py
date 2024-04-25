#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# has a percent difference less than 2%
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
"""
Example:
Enter one side: 5
Enter a second side: 13
Enter third side: 12
that is a right triangle

Enter one side: 13.01
Enter a second side: 5
Enter third side: 12
that is a right triangle

Enter one side: 5
Enter a second side: 15
Enter third side: 12
that is an obtuse triangle


"""
def is_right_triangle(a, b, c):
   
    sides = sorted([a, b, c])
    a, b, c = sides[0], sides[1], sides[2]

    if abs(c**2 - (a**2 + b**2)) < 1e-6:
        return True
    else:
        return False

def triangle_type(a, b, c):
  
    sides = sorted([a, b, c])
    a, b, c = sides[0], sides[1], sides[2]

    
    if is_right_triangle(a, b, c):
        return "that is a right triangle"
    else:
        
        expected_hypotenuse = (a**2 + b**2)**0.5
        
       
        percent_difference = abs(c - expected_hypotenuse) / expected_hypotenuse * 100
        
        if percent_difference < 2:
            return "that is an acute triangle"
        else:
            return "that is an obtuse triangle"

def main():
    
    try:
        a = float(input("Enter side length a: "))
        b = float(input("Enter side length b: "))
        c = float(input("Enter side length c: "))
    except ValueError:
        print("Please enter valid numerical values.")
        return
    
   
    result = triangle_type(a, b, c)
    print(result)

if __name__ == "__main__":
    main()
