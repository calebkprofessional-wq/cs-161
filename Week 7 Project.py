from time import sleep

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def try_int(prompt):
    """Takes a user input and verifies that it is an integer"""
    while True:
        number = input(prompt)
        try:
            number = int(number)
            return number
        except ValueError:
            print("\nPlease enter a valid number.")
            continue

def lower_upper():
    """Prints the even numbers between a lower and upper bound"""
    #This loop makes sure that the user is entering viable inputs
    while True:
        low_value = try_int("\nEnter a lower bound: ")
        high_value = try_int("\nEnter an upper bound: ")
        if low_value > high_value:
            print("\nYour lower value is greater than your upper value. Try again.")
            continue
        elif low_value == high_value:
            print("\nYour lower value is equal to your upper value. Try again.")
            continue
        else:
            break
    between = []
    current = low_value
    #Weeds out even numbers, and adds them to a list
    while True:
        current = current + 1
        if current < high_value:
            if current % 2 == 0:
                between.append(current)
        else:
            break
    print(f"\nThe even numbers between {low_value} and {high_value} are: {str(between).strip('[]')}")
    sleep(3)

def factors():
    """Prints the factors of a number"""
    number = try_int("\nEnter a positive integer: ")
    factors_list = [number]
    current = number
    #Checks each number from 1 to an input to see if it is a factor of the input
    while True:
        current = current - 1
        if current == 0:
            break
        elif number % current == 0:
            factors_list.append(current)
    factors_list.reverse()
    print(f"\nThe integers that are factors of {number} are: {str(factors_list).strip('[]')}")
    sleep(3)

def name_number():
    """Calculates the sum of the numeric positions of the letters in a name"""
    #Checks that the user input is valid
    while True:
        check = True
        name = input("\nEnter your name: ").strip().lower()
        for i in name:
            if i not in alphabet:
                check = False
                break
        if check:
            break
        else:
            print("\nPlease enter a valid name.")
    total = 0
    #Adds the sum of the numeric positions of the letters in the input
    for i in name:
        number = alphabet.index(i)
        total += number
    print(f"\nThe sum of the numeric positions of the letters in the name {name} is {total}.")
    sleep(3)

def squares_up_to(number,current=1):
    """Takes an integer, and prints all squares of all number from 1 to that input number"""
    #End the function
    if number == 0:
        return
    #Print the next number up squared
    else:
        print(f"{current**2}")
        #Adjust inputs
        current+=1
        number-=1
        #Run function again
        squares_up_to(number,current)

def teepee_sort():
    """Takes a list of numbers and prints the sorted list"""
    input_list = []
    #Makes the list
    while True:
        item = input("\nEnter a number to add to a list, or enter 'stop' to stop: ")
        if item == 'stop':
            break
        else:
            try:
                item = int(item)
                input_list.append(item)
            except ValueError:
                print("\nPlease enter a valid number.")
                continue
    evens = []
    odds = []
    #Sorts list into evens and odds
    for i in input_list:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    #Sorts the list, smallest to largest
    odds.sort()
    evens.sort()
    #Reverses the list of evens
    evens.reverse()
    final = odds + evens
    print(final)
    sleep(3)





def main():
    """Main function"""
    print("\nHello.")
    while True:
        print('''
1. Find the even numbers between a lower and upper bound
2. Find the factors of a number
3. Find the sum of the numeric positions of the letters in a name
4. Print the squares of all numbers up to and including an input number
5. Teepee sort a list of numbers''')
        #Allos the user to choose what to do
        choice = try_int("\nPlease select your choice: ")
        if choice == 1:
            lower_upper()
        elif choice == 2:
            factors()
        elif choice == 3:
            name_number()
        elif choice == 4:
            squares_up_to(try_int("\nPlease enter a positive integer: "))
        elif choice == 5:
            teepee_sort()
        else:
            print("\nPlease enter a valid choice.")
            continue


if __name__ == "__main__":
    main()


