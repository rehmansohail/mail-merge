#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

names_file = open("./Input/Names/invited_names.txt")
names = names_file.readlines()
names2=[]
for i in range(len(names)):
    if i==len(names)-1:
        names2.append(names[i])
        continue
    names2.append(names[i][:-1])
# print(names2)            #list with /n removed

letter_file = open("./Input/Letters/starting_letter.txt")
letter = letter_file.read()

for name in names2:
    file = open("./Output/ReadyToSend/%s.txt" %name,mode="w")
    content = letter.replace("[name]",name)
    file.write(content)
    

