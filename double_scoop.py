# Task 1: Your Mood Tracker
# Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week.
# Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the times of the day.
# For each time, randomly select a mood from a predefined list and print it.

import random

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
moods = ['Happy', 'Sad', 'Energetic', 'Calm']
tod = ['Morning', 'Afternoon', 'Evening']

for i in range(len(days)):
    for time in tod:
        mood = random.choice(moods)
        
        print(f"Day: {days[i]} Time: {time} Mood: {mood}")