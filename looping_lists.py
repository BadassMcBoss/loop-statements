# Task 1: The for Loop DJ Set
# Using the provided genres list, write a for loop that prints out each genre with a custom message.
# Extend this task by adding a counter that displays the number of the track before the genre.
# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
count = 1

for track in genres:
    print(f"Now playing {count}. {track}. Great choice!")
    count += 1
    
    


# Task 2: The Remix Artist with while
# Convert the for loop from Task 1 into a while loop. 
# Ensure it performs the same function but also includes a condition to stop the loop if a certain genre is played for instance Hip-hop.


# Task 3: Light Show Technician Loop
# Using the range() function, loop through the genres list by index.
# For each genre, print out the track number and a message that the light show is ready.
# Modify the loop to skip a genre if it's not suitable for the light show, for instance Classical genre.