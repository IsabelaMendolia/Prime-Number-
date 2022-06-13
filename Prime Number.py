n=int(input("Enter a number:"))
if n>1:
    for i in range(2,n//2):
        if(n%i)==0:
            print(n,"*Number input is Not a Prime Number*")
            break
    else:
        print(n,"*Number Input Is a Prime Number*")
else:
    print(n,"*Number Input is neither prime nor composite*")