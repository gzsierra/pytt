import sys, os, time

# Check Arguments
if len(sys.argv) != 2:
    print("Need an argument")
    print("python " + sys.argv[0] + " [file_name]")
    sys.exit(2)

# Check If EXIST and not EMPTY
file = sys.argv[1]
if not os.path.isfile(file):
    print("File not existing")
    sys.exit(2)
if os.stat(file).st_size == 0:
    print("File empty")
    sys.exit(2)

# Read file line by line and split
# split line TIME1 _ VALUE1
#            TIME2 _ VALUE2
#             ...  _  ...
#
# For each value (line) send to pytt
f = open(file,"r")
for line in f:
    split = line.split()
    print(split)
    time.sleep(5)
    os.system("python pytt.py " + split[0] + " " + split[1])
