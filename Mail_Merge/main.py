PLACEHOLDER = "[name]"

with open("Mail_Merge/Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()
   
with open("Mail_Merge/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"Mail_Merge/Output/ReadyToSend/letter_for{stripped_name}.txt",'w') as completed_letter:
            completed_letter.write(new_letter)
        

    