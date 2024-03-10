def fizzbuzz():
    for i in range(1, 101):
        #Check if the number has no remainder when divided by 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        #Check if number has no remainder for only 3
        elif i % 3 == 0:
            print("Fizz")
        #Check if number has no remainder for only 5
        elif i % 5 == 0:
            print("Buzz")
        #Print number if doesn't apply
        else:
            print(i)