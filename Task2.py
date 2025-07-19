
user_input = input("Enter some text to write to output.txt: ")
with open('output.txt', 'w') as file:
    file.write(user_input + '\n')


additional_data = input("Enter additional text to append to output.txt: ")
with open('output.txt', 'a') as file:
    file.write(additional_data + '\n')

# Step 3: Read and display the final content of the file
print("\nFinal content of output.txt:")
with open('output.txt', 'r') as file:
    for line in file:
        print(line.rstrip())