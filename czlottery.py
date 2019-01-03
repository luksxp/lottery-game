import random 

start = True
        

def menu():
    #lottery menu, play or exit    
    print("Choose 1 to play")
    print("Choose 2 to exit")  
    

def numbers_checker(usernums, winnums):
    #matching user's and random numbers
    counter = 0
    for i in range(0, 6):
        for y in range(0, 6):
            if winnums[i] == usernums[y]:
                print("You have match. It was " + str(usernums[y]))
                y = y + 1
                counter = counter + 1
    print("Winning numbers are:")
    print(str(winnums)[1:-1])
    print("Your numbers are:")
    print(str(usernums)[1:-1])
    
    #adding prizes according to matched numbers
    if counter == 1:
        print("You had " + str(counter) + " match.")
        print("Your price is 10 CZK")
    elif counter == 2:
        print("You had " + str(counter) + " matches.")
        print("Your price is 100 CZK")
    elif counter == 3:
        print("You had " + str(counter) + " matches.")
        print("Your price is 1000 CZK")
    elif counter == 4:
        print("You had " + str(counter) + " matches.")
        print("Your price is 10000 CZK")
    elif counter == 5:
        print("You had " + str(counter) + " matches.")
        print("Your price is 100000 CZK")
    elif counter == 6:
        print("You had " + str(counter) + " matches.")
        print("Your price is 1000000 CZK.")
    else:
        print("No win.")       
        
       
def user_numbers():
    # User inputs numbers 
    usernums = []
    while len(usernums) < 6:
        nums = int(input("Pick a 6 unique numbers form 1 through 49, each number-single line: "))        
        if 1 <= nums <= 49:
            if nums not in usernums:
                usernums.append(nums)
            else:
                print("Error, repeating number")
        else:
            input("Wrong input. Press any key to continue")
    return sorted(usernums)


def random_numbers():
    # Generating random unique numbers
    return sorted(random.sample(range(1,50), 6))     
   
    
def main():
    # Calling another functions
    usernums = user_numbers()
    winnums = random_numbers()
    numbers_checker(usernums, winnums)     


# Starting menu function
while start:
    menu()
    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        print("Your choice is to play")
        start = False
        main()
    elif choice == '2':
        print("Your choice is to leave game")
        start = False
    else:
        input("Error, press any key to continue") 

    

    



