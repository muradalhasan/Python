#Write a python program that takes an 
# integer from the user which represents the 
# number of chocolates that he/she has. He/S
# he decided to distribute the chocolates equ
# ally among 3 friends, keeping the remaining
# chocolates for him/herself. Find out the 
# number of chocolates each friend will 
# receive 
# and the number \of chocolates that will be 
# remaining.
choc=int(input("Enter the total chocolate number: "))
print(f"Each friend will receive {choc//3} chocolates")
print(f"The number of remaining chocolates is {choc%3}")