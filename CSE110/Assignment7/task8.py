# Function to show a single palindromic sequence
def show_palindrome(n):
    # Printing the increasing part from 1 to n
    for i in range(1, n+1):
        print(i, end=" ")
    
    # Printing the decreasing part from n-1 to 1
    for i in range(n-1, 0, -1):
        print(i, end=" ")
    
    # Move to the next line after each sequence
    print()

# Function to print the palindromic triangle
def show_palindromic_triangle(rows):
    for i in range(1, rows+1):
        # Printing leading spaces for alignment
        print(" " * (rows - i), end=" ")
        
        # Reusing the show_palindrome function to print the palindromic row
        show_palindrome(i)

# Example function call
show_palindromic_triangle(5)
