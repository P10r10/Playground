from random import choice, sample


my_tuple = (
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "A", "B", "C", "D", "E"
)

count = 0
roll = ""
while roll != "68C5":
    roll = "".join(sample(my_tuple, k=4))
    count += 1
print(f'The ticket {roll} wins $1.000.000! It took {count} rolls.')
