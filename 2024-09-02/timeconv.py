sec = int(input('Please enter the total seconds: '))

# Compute the number of hours from seconds
hr = sec // 3600
# Compute the seconds that remain
sec = sec % 3600

# Compute the number of minute from seconds
min = sec // 60
# Compute the seconds that remain
sec = sec % 60

print(hr, "hr", min, "min", sec, "sec")