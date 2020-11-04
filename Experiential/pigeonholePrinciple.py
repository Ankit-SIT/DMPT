# Ankit Das
# 19070122023
# PigeonHole Principle

# can find any value given the other two values


#! /usr/bin/env python
# minimumPigeons = (((pigeons - 1)/holes) + 1)

import math

# functions to find values
def findMinimumPigeons(pigeons,holes):

    # check for discrepancies like 0 denominator or pigeons less than holes
    if(pigeons < holes or holes == 0): 
        print("INVALID INPUT!")
        raise(KeyboardInterrupt)

    else:
        return math.ceil(((pigeons - 1)/holes) + 1)

def findPigeons(holes,minimumPigeons):
    return math.ceil((holes * (minimumPigeons - 1)) + 1)

def findHoles(pigeons,minimumPigeons):
    if(minimumPigeons != 1):
        return math.ceil((pigeons - 1) / (minimumPigeons - 1))
    
    else:
        return 0


def main():
    while(True):    
        try:
            print("\n\n-- MENU --")

            # find minimum number of pigeons in one hole given the number of holes and pigeons
            print("1. FIND MINIMUM PIGEONS: ") 

            # find number of pigeons given the number of holes and minimum pigeons in one hole
            print("2. FIND NUMBER OF PIGEONS: ")

            #find number of holes given the number of pigeons and minimum pigeons in one hole
            print("3. FIND NUMBER OF HOLES: ")
            print("4. EXIT")
            choice = int(input("\nENTER CHOICE: "))

            if(choice == 1):
                # get number of pigeons and holes from user
                pigeons = int(input("ENTER NUMBER OF PIGEONS: "))
                holes = int(input("ENTER NUMBER OF HOLES: "))

                # print result
                print("ONE OF THE PIGEONHOLE MUST CONTAIN ATLEAST {} PIGEONS".format(findMinimumPigeons(pigeons,holes)))
            
            elif(choice == 2):
                # get number of holes and minimum from user
                holes = int(input("ENTER NUMBER OF HOLES: "))
                minimumPigeons = int(input("ENTER MINIMUM NUMBER OF PIGEONS IN ONE HOLE: "))
                
                # print result
                print("THERE ARE {} PIGEONS".format(findPigeons(holes,minimumPigeons)))

            
            elif(choice == 3):
                # get number of pigeons and minimum from user
                pigeons = int(input("ENTER NUMBER OF PIGEONS: "))
                minimumPigeons = int(input("ENTER MINIMUM NUMBER OF PIGEONS IN ONE HOLE: "))

                # print result
                print("THERE ARE {} HOLES".format(findHoles(pigeons,minimumPigeons)))
            
            
            elif(choice == 4):
                raise(KeyboardInterrupt)

            else:
                print("INVALID CHOICE! TRY AGAIN!")

        except ValueError:
            print("INVALID INPUT! TRY AGAIN")

        

if __name__=="__main__":
    try:
        main()

    except KeyboardInterrupt:
            print("EXITING PROGRAM!")
            exit(0)
