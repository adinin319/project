#Dungeon and Dragons 5th Addition Stat Roller.#
#By Andrew Dinin#
import sys
import os
import random
#Ability Scores#
Strength = 3
Dexterity = 1
Constitution = 3
Intelligence = -2
Wisdom = 0
Charisma = 2

#Proficiency Modifier#
Proficiency = 2
#Skills#
Acrobatic = Dexterity
Animal_Handlin = 2
Arcan = Intelligence
Athletic = 5
Deceptio = 2
Histor = Intelligence
Insigh = 0
Intimidatio = 4
Investigatio = Intelligence
Medicin = 0
Natur = Intelligence
Perceptio = 0
Performanc = 2
Persuasio = 2
Religio = Intelligence
Sleight_of_Han = Dexterity
Stealt = 1
Surviva = 0
import random
Role_Type=input('What stat are you rolling?(Please enter associated number)\n1.) Acrobatics\n2.) Animal Handling\n3.) Arcana\n4.) Athletics\n5.) Deception\n6.) History\n7.) Insight\n8.) Intimidation\n9.) Investigation\n10.) Medicine\n'
      '11.) Nature\n12.) Perception\n13.) Performance\n14.) Persuasion\n15.) Religion\n16.) Sleight of Hand\n17.) Stealth\n18.) Survival\n Selection:');
    
if Role_Type == 1:
    import random
    for x in range(1):
         print random.randint(1,21)+Acrobatic
    print
if Role_Type == 2:
    import random
    for x in range(1):
         print random.randint(1,21)+Animal_Handlin
    print
if Role_Type == 3:
    import random
    for x in range(1):
         print random.randint(1,21)+Arcan
    print
if Role_Type == 4:
    import random
    for x in range(1):
         print random.randint(1,21)+5
    print
if Role_Type == 5:
    import random
    for x in range(1):
         print random.randint(1,21)+2
    print
if Role_Type == 6:
    import random
    for x in range(1):
         print random.randint(1,21)-2
    print
if Role_Type == 7:
    import random
    for x in range(1):
         print random.randint(1,21)+0
    print
def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)
if __name__ == "__main__":
    answer = raw_input("Do you want to restart this program ? ")
    if answer.lower().strip() in "y yes".split():
        restart_program()


