def function_name(a):
    lst=[]
    count=0
    for i in a:
        c=lst.count(i)
        if c<2:
            lst.append(i)
        else:
            count+=1
    print(f"Removed: {count}\n{lst}")
            
function_name([10, 10, 15, 15, 20])



