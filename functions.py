
choise = int(input("what number would you like to choise"))

def function(choise):
    
    for num in range(1, choise):
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")
        elif num % 3 ==0:
            print("fizz")
        elif num % 5 ==0:
            print("buzz")
        else:
            print(num)
            
print("about to run the program")
function(choise)


ip = input("what is the target ip address")

def nmap(ip):
    print(f"attracking {ip} ")
    
nmap(ip)