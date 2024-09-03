mark=int(input("Enter the student score: "))
grade=""
if mark>=90:
    grade="A"
elif mark >=80 and mark<=89:
    grade="B"
elif mark >=70 and mark<=79:
    grade="c"
elif mark >=60 and mark<=69:
    grade="D"
elif mark >=50 and mark<=59:
    grade="E"
else:
    grade="F"
print(grade)