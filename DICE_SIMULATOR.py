import random 
  
  
roll_again = "r"
   
while roll_again == "r": 
      
    # Gnenerates a random number 
    # between 1 and 6 (including 
    # both 1 and 6) 
    number = random.randint(1,6) 
      
    if number == 1: 
        print("  |     |") 
        print("  |  0  |") 
        print("  |     |") 
    if number == 2: 
        print("  | 0   |") 
        print("  |     |") 
        print("  |   0 |") 
    if number == 3: 
        print("  |     |") 
        print("  |0 0 0|") 
        print("  |     |") 
    if number == 4: 
        print("  |0   0|") 
        print("  |     |") 
        print("  |0   0|") 
    if number == 5: 
        print("  |0   0|") 
        print("  |  0  |") 
        print("  |0   0|") 
    if number == 6: 
        print("  |0 0 0|") 
        print("  |     |") 
        print("  |0 0 0|") 
    print("\n")      
    roll_again = input("press r to roll again:") 

    print("\n") 