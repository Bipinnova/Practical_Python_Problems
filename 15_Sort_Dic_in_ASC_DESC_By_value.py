# Write a Python script to sort (ascending and descending) a dictionary by 
# value.


released = {'Python 3.6': 2017, 'Python 1.0': 2002, 'Python 2.3': 2010}

# Sort by value ascending
print("Ascending by value:")
for key, value in sorted(released.items(), key=lambda item: item[1]):
    print(key, value)

# Sort by value descending
print("\nDescending by value:")
for key, value in sorted(released.items(), key=lambda item: item[1], reverse=True):
    print(key, value)
