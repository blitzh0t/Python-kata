import random

#seed a temporary array. not very efficient
def fill_array(array_size):
    temp_array = []
    for i in range(0,array_size):
        while True:
            rand_int = random.randint(0,array_size)
            if rand_int not in temp_array:
                temp_array.append(rand_int)
                break
    return temp_array

#Convert List to a Set. Input array is unordered and unique which makes a Set suitable for efficient member checking
#To find the missing number , get the difference between two sets            
def find_missing_number(input_array):
    array_range = list(range(1,(len(input_array) + 1)))   #seed a list using range
    print("Range[1 - N] " + str(array_range))
    print("Input Array: " + str(input_array))
    set_difference = set(array_range) - set(input_array)
    return set_difference

def main():
    print("Enter an integer for array size")
    while True:
        try:
            input_array_size = int(input())
        except ValueError:
            print("input is not an integer. Try again")
        else:
            break
    input_array = fill_array(input_array_size)
    missing_number = find_missing_number(input_array)
    print("Missing number is : " + str(missing_number)[1:-1])

if __name__ == "__main__":
    main()