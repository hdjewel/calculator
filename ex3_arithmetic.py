import arithmetic

def main():

    print "This is a program to do math equations."
    print " "
    print "Input pattern as follows"
    print " addition - add, int, int"
    print " sub - sub, int, int"
    print " multi  - ...."
    print " squ - squ, int"
    print "cube- cube, int"
    print "etc..."
    print "If you want to quit, type 'q'"

   
    while True:
        userInput = raw_input("What kind of calculation would you like to perform?   ")

        tokens = userInput.split(",") #token[pow, 2, 3]
  

        if tokens[0] == 'add':
            print add(int(tokens[1]), int(tokens[2]))
        elif tokens[0] == 'sub':
            print sub(int(tokens[1]), int(tokens[2]))
        elif tokens[0] == 'multi':
            print multiply(int(tokens[1]), int(tokens[2]))
        elif tokens[0] == 'divide':
            print divide(int(tokens[1]), int(tokens[2]))
        elif tokens[0] == 'squ':
            print square(int(tokens[1]))
        elif tokens[0] == 'pow':
            print power(int(tokens[1]), int(tokens[2]))
        elif tokens[0] == 'mod':
            print mod(int(tokens[1]), int(tokens[2]))
        elif tokens[0] == 'cube':
            print cube(int(tokens[1]))
        elif tokens[0] == 'q':
            break
        else:
            print "What do you want to do??"

        #tokens[0] = 'q'
#### the way Nadine, thinking was elif tokens[0] == 'q' ; break...is not good because it's "spag. code"
# doing it the negative way != q, allows the while loop to check 'q' and prevent the "what do you want to do"
#statement from printing. And it gives the while loop 1 exit point

#use int because string is given in raw_input

# setting array to [" "] to initialize the array

main() 