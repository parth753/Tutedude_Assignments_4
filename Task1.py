try:
    with open('sample.txt', 'r') as file:
        for line in file:
            print(line.rstrip())
except FileNotFoundError:
    print("Error: 'sample.txt' not found.")