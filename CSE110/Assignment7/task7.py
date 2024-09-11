def show_palindrome(num):
    for i in range(1,num+1):
        print(i,end="")
        if i==num:
            for j in range(num-1,0,-1):
                print(j,end="")
            break
show_palindrome(3)