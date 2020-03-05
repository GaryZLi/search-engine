directory = 'checkTest/'
with open('check.txt', 'r') as file:
    for line in file:
        line = line.strip()

        with open('DEV/' + line, 'r') as reading, open(line, 'a') as wr:
            # print(directory + line)
            
            # print(reading.read())
            pass

# with open (directory + 'aaaa', 'a') as f:


