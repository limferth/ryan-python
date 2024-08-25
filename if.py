fnum = input("What is the first number ")
snum = input("What is the second number ")

if fnum > snum:
    print("the first number is bigger")
elif snum > fnum:
    print("the second number es bigger")
else:
    print("the numbers are the same")
    
# exercises

score = input("what was your test score?")
score = int(score)

if score >= 98:
    age = int(input("what is your age? "))
    if age < 18:
        print("ypur grade is an A+ ")
    else:
        print("your grade is an A")
elif score >= 80:
    age = int(input("what is your age? "))
    if age < 18:
        print("ypur grade is an B+ ")
    else:
        print("your grade is an B")
elif score >= 65:
    age = int(input("what is your age? "))
    if age < 18:
        print("ypur grade is an C+ ")
    else:
        print("your grade is an C")
else:
    print("next study more")
