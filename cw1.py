

#this main fuction calls all the other problem functions
def main():
    prob1()
    #prob2()




# this function loops untill user quits
def prob1():
    uI= 'Enter a number. Enter q to quit'
    nums= []
    total= 0
    while uI.lower()!='q':
        uI=(input("Enter another number. Enter q to quit"))
        nums.append(uI)

    nums.pop(len(nums)-1)

#the end of the function prints the total of the numbers provided by user
    for x in range(len(nums)-1):
        numbers= int(nums[x])
        total += numbers
    print("your total is: ",total)

# this function takes the numbers provided by user and prints the math results in a dictionary
def prob2():
    num1= int(input("Enter a number"))
    num2= int(input("Enter another number"))

    def do_the_math(x,y):
        sum= x+y
        difference= x-y
        product= x*y
        quotient= x/y

        return {sum,difference,product,quotient}

    print(do_the_math(num1,num2))





















if __name__ == '__main__':
    main()
