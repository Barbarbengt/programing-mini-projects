import random



binarylist=[0,0,0,0,0,0,0,0]
i = 0
binar = "";
rNum="";
while i < 8:
        
    rNum= str(random.randint(0,1))
    binar+= rNum
    binarylist[i]= rNum
    i += 1 


print("Guess the decimal! :) \n")
dificulty = input("Select dificulty [E]asy or [H]ard:  ");

if(dificulty.upper() == "E"):
    print("\nYou have selected Easy mode, a help table to calcualte binary is now provided.\n")
    print("|128|64 |32 |16 | 8 | 4 | 2 | 1 |")
else: print("Hard mode selected \n")
print("|",binarylist[0],"|",binarylist[1],"|",binarylist[2],"|",binarylist[3],"|",binarylist[4],"|",binarylist[5],"|",binarylist[6],"|",binarylist[7],"|")
decimal_num = int(binar, 2);

decimal_guess = input("Enter number in Binary Format: ");
#print(binar,"in Decimal =",decimal_num);


while(str(decimal_num) != str(decimal_guess)):
    decimal_guess = input("Enter number in Binary Format: ");

print("Congrats! You did it! :)")