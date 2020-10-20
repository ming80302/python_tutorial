print("Hello, world")

# read the data file
filename ="data/wxobs20170821.txt"

datafile = open(filename, "r")
# read a line
#print(datafile.readline())
#print(datafile.readline())
#print(datafile.readline())

# the other way to read a data file
data = datafile.read()

# DEGUG
#print(data)

# important to close for memory issues
datafile.close()


# for a cleaner version using with as a context manager, automaticly closed after reading it
with open(filename, 'r') as datafile:
    data = datafile.read()

print(data)

