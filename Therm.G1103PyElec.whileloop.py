#solve Exercise 1 done
number = 10

print(end=" ", "Goodbye")

while number <= 2:
    print(number, end=" ")
    number += 2
print()

#solve Exercise 2 done
number = 10

print("Hello!", end=" ")

while number >= 2:
    print(number, end=" ")
    number -= 2

print()  # To move to the next line after the output

#solve Evercise 3 done
end = 9
sum_of_numbers = 0
current_number = 1
while current_number <= end:
 sum_of_numbers += current_number
 current_number += 1
print("The sum of numbers from 1 to", end, "is:", sum_of_numbers)