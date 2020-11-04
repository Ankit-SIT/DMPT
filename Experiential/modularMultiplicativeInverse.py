#! /usr/bin/env python
# modular multiplicative inverse of a mod m is a number which when multiplied with a gives a result of 1 mod m

import euclid

def inverse(integer,mod):
    integer %= mod # find remainder and store it in integer variable
    for i in range(1,mod):   # loop though mod - 1 values as inverse will always be less than mod
        if((integer * i) % mod == 1):   # if mod divides (integer) x (the value) and gives a remainder of 1, the value is the inverse
            return i          # return value

    return 1

def main():
    while(True):

        # get user inputs
        try:
            integer = int(input("ENTER INTEGER: "))
            mod = int(input("ENTER MODULUS: "))

            # make sure the numbers are coprime
            if(euclid.gcd(integer,mod) == 1):
                # calculate result
                result = inverse(integer,mod)

                # print the result
                print("MODULAR INVERSE OF ({},{}) : {}".format(integer,mod,result))
            
            # otherwise, inverse doesn't exist
            else:
                print("MODULAR INVERSE OF ({},{}) DOESN'T EXIST. NUMBERS ARE NOT COPRIME".format(integer,mod))

            # check for exit
            print("\n\nEXIT? (Y/N)")
            choice = input()
            if(choice == 'y' or choice == 'Y'):
                raise(KeyboardInterrupt)
        
        # make sure the values are valid
        except ValueError:
            print("\nINVALID INPUT! TRY AGAIN")
        
if __name__=="__main__":
    try:
        main()

    except KeyboardInterrupt:
            print("\nEXITING PROGRAM!")
            exit(0)
