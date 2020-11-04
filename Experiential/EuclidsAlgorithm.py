# Ankit Das
# 19070122023
# Euclid's Algorithm

#! /usr/bin/env python
# gcd(m,n) is the greatest common divisor of both numbers

def swap(x,y):      # utility function to swap values
    (x,y) = (y,x)
 
def gcd(m,n):
    if m < n:    # ensure m is always greater than n
        swap(m,n)   # if not, swap the values
    
    if(m%n==0): # check if n divides m perfectly
        return n    # if yes, n is the gcd
    
    else:      # otherwise, 
        return(gcd(n,m%n))  # recurse the gcd function with n and m%n 


def main(): # Driver Function
    while(True):
        try:
            print("ENTER FIRST INTEGER: ",end='')
            m = int(input())

            print("ENTER SECOND INTEGER: ",end='')
            n = int(input())

            print("GCD({},{}) = {}".format(m,n,gcd(m,n)))
        
            print("\n\nEXIT? (Y/N)")
            choice = input()
            if(choice == 'y' or choice == 'Y'):
                raise(KeyboardInterrupt)

        except ValueError:
            print("INVALID INPUT! TRY AGAIN")

if __name__=="__main__":
    try:
        main()
    
    except KeyboardInterrupt:
        print("EXITING PROGRAM!")
        exit(0)

    
