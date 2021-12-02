

#Coding Advent Calender 02/12/2021


#part1
def one():
    filename = "02.txt"
    with open(filename,'r') as file:
        lst = file.readlines()

    direction = 0
    hmagnitude = 0
    vmagnitude = 0 
    aim = 0
    for line in lst:
        direction,newmagnitude = line.split()
        if direction == "forward":
            hmagnitude += int(newmagnitude)
        elif direction == "down":
            vmagnitude += int(newmagnitude)
        else:
            vmagnitude -= int(newmagnitude)
    total = vmagnitude * hmagnitude
    return total

#part2
def two():
    filename = "02.txt"
    with open(filename) as f:
         lst = [line.strip() for line in f.readlines()]

    horizontal = 0
    depth = 0
    aim = 0

    for i in lst:
        magnitude = int(i[-1])
        if i.startswith("down"):
            aim += magnitude
        elif i.startswith("up"):
            aim -= magnitude
        else:
            horizontal += magnitude
            depth += aim * magnitude

    return (horizontal * depth)

print (one())
print (two())






