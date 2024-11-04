# Create a template letter using starting_letter.txt 
with open("./Input/Letters/starting_letter.txt") as temp:
    letter_file = temp.read()

# Read each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as names:
    names_list = names.readlines()
    print(len(names_list))

# Replace the [name] placeholder with the actual name.
for name in names_list:
    stripped_name = name.strip()
    individual_letter = letter_file.replace("[name]", stripped_name)
    #Save the letters in the folder "ReadyToSend".
    print(individual_letter)
    
    with open(f"./Output/ReadyToSend/letter_{stripped_name}.docx", mode="w") as f:
        f.write(individual_letter)
    