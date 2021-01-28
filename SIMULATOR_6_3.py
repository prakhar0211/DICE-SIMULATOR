# Define die outcomes and probabilities
import numpy as np
import pandas as pd
roll_again = "r"
   
while roll_again == "r":
    die, probabilities, throws =[1,2,3,4,5,6], [1/8,1/8,2/8,1/8,1/8,2/8],1
    # Use np.random.choice to throw the die once and record the outcome
    outcome= np.random.choice(die, size=throws, p=probabilities)
    if outcome[0] == 1: 
        print("  |     |") 
        print("  |  0  |") 
        print("  |     |") 
    if outcome[0] == 2: 
        print("  | 0   |") 
        print("  |     |") 
        print("  |   0 |") 
    if outcome[0] == 3: 
        print("  |     |") 
        print("  |0 0 0|") 
        print("  |     |") 
    if outcome[0] == 4: 
        print("  |0   0|") 
        print("  |     |") 
        print("  |0   0|") 
    if outcome[0] == 5: 
        print("  |0   0|") 
        print("  |  0  |") 
        print("  |0   0|") 
    if outcome[0] == 6: 
        print("  |0 0 0|") 
        print("  |     |") 
        print("  |0 0 0|") 
    print("\n") 
    roll_again = input("press r to roll again:")
    print("\n")                 #Leaves a line before printing next result