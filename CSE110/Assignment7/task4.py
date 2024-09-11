def function_name(a):
    u_count=0
    l_count=0
    for i in a:
        if ord(i)>=65 and ord(i)<=90:
            u_count+=1
        elif ord(i)>=97 and ord(i)<=122:
            l_count+=1
    return f"No. of Uppercase characters : {u_count}\n No. of Lowercase Characters: {l_count}"
print(function_name('HaRRy PotteR'))
