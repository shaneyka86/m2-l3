#Problem Statement: You have a list of daily temperatures for one month, 
# and you'd like to extract specific data from it.
#Extract the temperatures for the second week (7 days) of the month (index 7 to index 14).
# Expected Outcome:
#83, 85, 86, 87, 88, 89, 90,

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

second_week=temperatures[7:14]
print(second_week)