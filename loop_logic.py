# Task 1: Loop Condition Exploration
# Write a while loop with a condition that will never be true (an infinite loop). 
# Inside the loop, print a statement. 
# Then, use a break statement to exit the loop after 5 iterations.

count = 0

while 1 == 1:
    print("Neverending...!")
    count += 1
    if count == 5:
        print("The End")
        break

# Task 2: Conditional Exit
# Modify the infinite loop from Task 1 to include a condition that will eventually be true and remove the break statement.
# The loop should terminate naturally once the condition is met.

count = 0

while count < 5:
    print("Neverending...!")
    count += 1
    if count == 5:
        print("The End")