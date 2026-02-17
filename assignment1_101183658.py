"""
Author: <Salman Alamin>
Assignment: #1
"""

# Step b: Create 4 variables
gym_member = "Alex Alliton" #string
preferred_weight_kg = 20.5 #float
highest_reps = 25 #integer
membership_active = True #boolean
# Step c: Create a dictionary named workout_stats
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (40, 35, 50),
    "Taylor": (25, 30, 60)
}
# Step d: Calculate total workout minutes using a loop and add to dictionary
friends = list(workout_stats.keys())

for friend in friends:
    minutes = workout_stats[friend]
    
    total = 0
    for minute in minutes:
        total = total + minute
    
    workout_stats[friend + "_Total"] = total
# Step e: Create a 2D nested list called workout_list
workout_list = []

for friend in workout_stats:
    if "_Total" not in friend:
        minutes_tuple = workout_stats[friend]
        minutes_list = list(minutes_tuple)  # convert tuple to list
        workout_list.append(minutes_list)
# Step f: Slice the workout_list
print("Yoga and Running minutes for all your friends:")
for row in workout_list:
    print(row[0:2])  

print("Weightlifting minutes for last two friends:")
last_two = workout_list[-2:] 

for row in last_two:
    print(row[2])  

# Step g: Check if any friend's total >= 120
for key in workout_stats:
    if "_Total" in key:
        if workout_stats[key] >= 120:
            name = key.replace("_Total", "")
            print("Great job staying active,", name + "!")

# Step h: User input to look up a friend
friend_name = input("Enter a friend's name: ")

if friend_name in workout_stats:
    minutes = workout_stats[friend_name]
    total = workout_stats[friend_name + "_Total"]
    
    print(friend_name + "'s Workout Minutes:")
    print("Yoga:", minutes[0], "minutes")
    print("Running:", minutes[1], "minutes")
    print("Weightlifting:", minutes[2], "minutes")
    print("Total:", total, "minutes")
else:
    print("Friend", friend_name, "not found in the records.")

# Step i: Friend with highest and lowest total workout minutes
highest_total = 0
lowest_total = None
highest_name = ""
lowest_name = ""

for key in workout_stats:
    if "_Total" in key:
        total = workout_stats[key]
        name = key.replace("_Total", "")
        
        if total > highest_total:
            highest_total = total
            highest_name = name
        
        if lowest_total is None or total < lowest_total:
            lowest_total = total
            lowest_name = name

print("Friend with highest total workout minutes:", highest_name)
print("Friend with lowest total workout minutes:", lowest_name)
