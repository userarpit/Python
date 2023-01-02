import sys

print("Number of arguments",len(sys.argv))
print("Arguments are",sys.argv)

print(sys.version)

for line in sys.stdin:
    if line.rstrip() == 'q':
        break
    else:
        print(line)
print("Exit")

print("arpit", file = sys.stderr) 