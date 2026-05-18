# loops.py

# Example 1: For loop
print("For loop example:")
for i in range(5):  # Loops from 0 to 4
    print("Number:", i)

print("\nWhile loop example:")
# Example 2: While loop
count = 0
while count < 5:
    print("Count is:", count)
    count += 1  # Increment count

print("\nLooping through a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like", fruit)

print("\nBreaking out of a loop:")
for i in range(10):
    if i == 3:
        print("Stopping at 3!")
        break  # Exits the loop
    print(i)

print("\nContinuing a loop (skipping 2):")
for i in range(5):
    if i == 2:
        continue  # Skips this iteration
    print(i)