# Column names and column indices to read
columns = {'date':0, 'time':1, 'tempout':2, 'windspeed':7}

# data types for each column 
types = {'tempout':float, 'windspeed':float}

# Initialized my data variable
#data = {'date':[], 'time':[], 'tempout':[]}
data = {}
for column in columns:
    data[column] = []

# read the data file
filename ="data/wxobs20170821.txt"

# datafile = open(filename, "r")
# read a line
# print(datafile.readline())
# print(datafile.readline())
# print(datafile.readline())

# the other way to read a data file
# data = datafile.read()

# important to close for memory issues
# datafile.close()

# for a cleaner version using with as a context manager, automaticly closed after reading it
with open(filename, 'r') as datafile:
    #data = datafile.read()
    # read the first three lines, and discard
    for _ in range(3):
        datafile.readline()

    # read and parse the rest of the file
    for line in datafile:
        #datum = line.split()	# default split according to space, '/t' is for tab
        #data.append(datum)
        split_line = line.split()
        #data['date'].append(split_line[0])
        #data['time'].append(split_line[1])
        #data['tempout'].append(float(split_line[2]))
        for column in columns:
            i = columns[column]
            t = types.get(column, str)
            value = t(split_line[i])
            data[column].append(value)
            
print(data['tempout'])
