import random
import time

def linear_search(arr, key):
    # Loop through each value in the data list
    for i in range (len(arr)):
        # Check if value matches key
        if(arr[i] == key):
            # Return index key was found at
            return i
    # Return key not found
    return -1

def sentinel_search(arr, key):
    # Add sentinel value (key) to end of data list
    arr.append(key)

    # Loop through each value in data list until key index is found
    i = 0
    while arr[i] != key:
        i += 1
    
    # Check if key found at sentinel value
    if(i == len(arr) - 1):
        # Return key not found
        return -1
    else:
        # Return index key was found at
        return i

def binary_search(arr, key, left, right):
    while left <= right:
        # Set middle value to middle of two bounds
        middle = (right + left) // 2

        # Check if key is equal to middle value
        if key == arr[middle]:
            # Return middle value
            return middle
        # Cehck if key is greater than or eaual to middle value
        elif key >= arr[middle]:
            # Set lower bound to middle
            left = middle + 1
        # Else if key is less than middle value
        else:
            # Set upper bound to 1 less than middle value
            right = middle - 1
    # Return key not found
    return -1

def ternary_search(arr, key, left, right):
    if(right >= left):
        # Find the middle values 1 and 2
        middle_1 = left + (right - left) // 3
        middle_2 = right - (right - left) // 3

        # Check if key is in either middle value, return index if true
        if(arr[middle_1] == key):
            return middle_1
        if(arr[middle_2] == key):
            return middle_2

        # Check which region key is present in and repeat search in that region
        if(key < arr[middle_1]):
            # Key is between left and middle_1
            return ternary_search(arr, key, left, middle_1 - 1)
        elif(key > arr[middle_2]):
            # Key is between middle_2 and right
            return ternary_search(arr, key, middle_2 + 1, right)
        else:
            # Key is between middle_1 and middle_2
            return ternary_search(arr, key, middle_1 + 1, middle_2 - 1)

    # Return key not found
    return -1

def generate_list(n):
    list = []
    # Add the data to the list
    for i in range (n):
        # Add a random number between 0 and 1000 to the list
        list.append(random.randint(0, 1000))
    return list

def generate_key():
    # Generate random key number
    key = random.randint(0, 1000)
    return key

def linear_search_test(n, number_of_tests):
    print(f"Linear search tests, n = {n}")
    for i in range (number_of_tests):
        list = generate_list(n)
        key = generate_key()

        # Get start time
        start_time = time.time()
        # Run test
        linear_search(list, key)
        # Get end time
        end_time = time.time()
        # Calculate elapsed time
        elapsed_time = end_time - start_time
        # Convert to milliseconds
        elapsed_time_ms = elapsed_time * 1000
        print(f"Test {i + 1} time in milliseconds = {elapsed_time_ms:.3f}")

def sentinel_search_test(n, number_of_tests):
    print(f"Sentinel search tests, n = {n}")
    for i in range (number_of_tests):
        list = generate_list(n)
        key = generate_key()

        # Get start time
        start_time = time.time()
        # Run test
        sentinel_search(list, key)
        # Get end time
        end_time = time.time()
        # Calculate elapsed time
        elapsed_time = end_time - start_time
        # Convert to milliseconds
        elapsed_time_ms = elapsed_time * 1000
        print(f"Test {i + 1} time in milliseconds = {elapsed_time_ms:.3f}")

def binary_search_test(n, number_of_tests):
    print(f"Binary search tests, n = {n}")
    for i in range (number_of_tests):
        list = generate_list(n)
        # Sort the data
        list.sort()

        key = generate_key()

        # Get start time
        start_time = time.time()
        # Run test
        binary_search(list, key, 0, len(list) - 1)
        # Get end time
        end_time = time.time()
        # Calculate elapsed time
        elapsed_time = end_time - start_time
        # Convert to milliseconds
        elapsed_time_ms = elapsed_time * 1000
        print(f"Test {i + 1} time in milliseconds = {elapsed_time_ms:.3f}")

def ternary_search_test(n, number_of_tests):
    print(f"Ternary search tests, n = {n}")
    for i in range (number_of_tests):
        list = generate_list(n)
        # Sort the data
        list.sort()
        
        key = generate_key()

        # Get start time
        start_time = time.time()
        # Run test
        ternary_search(list, key, 0, len(list) - 1)
        # Get end time
        end_time = time.time()
        # Calculate elapsed time
        elapsed_time = end_time - start_time
        # Convert to milliseconds
        elapsed_time_ms = elapsed_time * 1000
        print(f"Test {i + 1} time in milliseconds = {elapsed_time_ms:.3f}")

number_of_tests = 5

# Linear search tests
linear_search_test(1000, number_of_tests)
print()
linear_search_test(5000, number_of_tests)
print()
linear_search_test(10000, number_of_tests)
print()
linear_search_test(50000, number_of_tests)
print()
linear_search_test(100000, number_of_tests)
print()

# Sentinel search tests
sentinel_search_test(1000, number_of_tests)
print()
sentinel_search_test(5000, number_of_tests)
print()
sentinel_search_test(10000, number_of_tests)
print()
sentinel_search_test(50000, number_of_tests)
print()
sentinel_search_test(100000, number_of_tests)
print()

# Binary search tests
binary_search_test(1000, number_of_tests)
print()
binary_search_test(5000, number_of_tests)
print()
binary_search_test(10000, number_of_tests)
print()
binary_search_test(50000, number_of_tests)
print()
binary_search_test(100000, number_of_tests)
print()

# Ternary search tests
ternary_search_test(1000, number_of_tests)
print()
ternary_search_test(5000, number_of_tests)
print()
ternary_search_test(10000, number_of_tests)
print()
ternary_search_test(50000, number_of_tests)
print()
ternary_search_test(100000, number_of_tests)
print()
