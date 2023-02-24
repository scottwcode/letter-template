# letter-template
# This program takes a letter template and list of names and uses them to create
# separate letters for each of the names. It also substitutes PLACEHOLDER with the
# name from the invitees_file.
#   Input
#       letter_template_file - ./Input/Letters/starting_letter.txt
#       invitees_file - ./Input/Names/invited_names.txt
#   Output
#       ReadyToSend - <name>_letter.txt

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", "r") as invitees_file:
    invitees_list = invitees_file.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as letter_template_file:
    letter_contents = letter_template_file.read()
    for name in invitees_list:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open("./Output/ReadyToSend/"+stripped_name+"_letter.txt", "w") as letter_file:
            letter_file.write(new_letter)
