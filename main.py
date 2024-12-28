def main():

    print("Welcome to the Odd or Even Checker!")
    number = int(input ('Please enter any number to test whether it is odd or even:'))
                         
    if (number % 2) == 0:
          print ('The number is even') 
                 
    else: print ('The provided number is odd')


    
if __name__=="__main__":
        main()