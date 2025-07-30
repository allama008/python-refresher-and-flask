"""
numbers = [1, 3, 5]
doubled = []

for num in numbers:
    doubled.append(num * 2)

# OR doubled = [num * 2 for num in numbers]

"""

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = []

for friend in friends:
    if friend.startswith("S"):
        starts_s.append(friend)

# OR starts_s = [friend for friend in friends if friend.startswith("S")]

print(starts_s)