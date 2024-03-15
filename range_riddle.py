# Task 1: Your Mood Today
# Write a program that simulates different moods for each day of the week. Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm". 
# Using the range() function, loop through the days of the week and for each day, randomly select a mood from the list and print it. 
# Ensure that your program includes the use of the random module to select the mood.


import random

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
moods = ['Happy', 'Sad', 'Energetic', 'Calm']

for i in range(len(days)):
    print(f"Day:{days[i]} Mood: {random.choice(moods)}")