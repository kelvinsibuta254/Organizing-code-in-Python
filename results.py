def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num **0.5)+1):
        if num % i ==0:
            return False
    return True
    #Find and store numbers in results.txt file
with open("results.txt", "w") as result_file:
    for number in range(1, 251):
        if is_prime(number):
            result_file.write(str(number)+ "\n")
print("Prime numbers between 1 and 250 have been saved in results.txt.")