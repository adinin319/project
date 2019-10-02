#Dungeon and Dragons 5th Addition Stat Roller. v2#
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
Proficiency = 2
#Skills#
Acrobatic = Dexterity
Animal_Handlin = Wisdom + Proficiency
Arcan = Intelligence
Athletic = Strength + Proficiency
Deceptio = Charisma
Histor = Intelligence
Insigh = Wisdom
Intimidatio = Charisma + Proficiency
Investigatio = Intelligence
Medicin = Wisdom
Natur = Intelligence
Perceptio = Wisdom
Performanc = Charisma
Persuasio = Charisma
Religio = Intelligence
Sleight_of_Han = Dexterity
Stealt = Dexterity
Surviva = Wisdom + Proficiency
Role_Type=input('What stat are you rolling?(Please enter associated number)\n1.) Acrobatics\n2.) Animal Handling\n3.) Arcana\n4.) Athletics\n5.) Deception\n6.) History\n7.) Insight\n8.) Intimidation\n9.) Investigation\n10.) Medicine\n'
      '11.) Nature\n12.) Perception\n13.) Performance\n14.) Persuasion\n15.) Religion\n16.) Sleight of Hand\n17.) Stealth\n18.) Survival\n Selection:');

if Role_Type == '1':
    import random
    y=(random.randint(1,20))
    z=y + Acrobatic
    print("You Rolled a :",y,"\nThe Total for Acrobatics Rolled is :",z)
elif Role_Type == '2':
    import random
    for x in range(1):
        y=(random.randint(1,20))
        z=y + Animal_Handlin
    print("You Rolled a :",y,"\nThe Total for Animal Handling Rolled is :",z)
elif Role_Type == '3':
    import random
    for x in range(1):
        y=(random.randint(1,20))
        z=y + Acrobatic
    print("You Rolled a :",y,"\nThe Total for Acrobatics Rolled is :",z)
elif Role_Type == '4':
    import random
    for x in range(1):
        y=(random.randint(1,20))
        z=y + Acrobatic
    print("You Rolled a :",y,"\nThe Total for Acrobatics Rolled is :",z)
elif Role_Type == '5':
    import random
    for x in range(1):
        y=(random.randint(1,20))
        z=y + Acrobatic
    print("You Rolled a :",y,"\nThe Total for Acrobatics Rolled is :",z)
elif Role_Type == '6':
    import random
    for x in range(1):
        y=(random.randint(1,20))
        z=y + Acrobatic
    print("You Rolled a :",y,"\nThe Total for Acrobatics Rolled is :",z)
elif Role_Type == '7':
    import random
    for x in range(1):
        y=(random.randint(1,20))
        z=y + Acrobatic
    print("You Rolled a :",y,"\nThe Total for Acrobatics Rolled is :",z)
elif Role_Type == '8':
    import random
    for x in range(1):
        y=(random.randint(1,20))
        z=y + Acrobatic
    print("You Rolled a :",y,"\nThe Total for Acrobatics Rolled is :",z)
elif Role_Type == '9':
    import random
    for x in range(1):
        y=(random.randint(1,20))
        z=y + Acrobatic
    print("You Rolled a :",y,"\nThe Total for Acrobatics Rolled is :",z)
elif Role_Type == '10':
    import random
    for x in range(1):
        y=(random.randint(1,20))
        z=y + Acrobatic
    print("You Rolled a :",y,"\nThe Total for Acrobatics Rolled is :",z)
elif Role_Type == '11':
    import random
    for x in range(1):
       y=(random.randint(1,20))
       z=y + Acrobatic
    print("You Rolled a :",y,"\nThe Total for Acrobatics Rolled is :",z)
elif Role_Type == '12':
    import random
    for x in range(1):
        y=(random.randint(1,20))
        z=y + Acrobatic
    print("You Rolled a :",y,"\nThe Total for Acrobatics Rolled is :",z)
elif Role_Type == '13':
    import random
    for x in range(1):
        y=(random.randint(1,20))
        z=y + Acrobatic
    print("You Rolled a :",y,"\nThe Total for Acrobatics Rolled is :",z)
elif Role_Type == '14':
    import random
    for x in range(1):
        roll=(random.randint(1,20))
        z=roll + Acrobatic
    print("You Rolled a :",y,"\nThe Total for Acrobatics Rolled is :",z)
elif Role_Type == '15':
    import random
    for x in range(1):
        print(random.randint(1,101))
elif Role_Type == '16':
    import random
    for x in range(1):
        print(random.randint(1,101))
elif Role_Type == '17':
    import random
    for x in range(1):
        print(random.randint(1,101))
elif Role_Type == '18':
    import random
    for x in range(1):
        print(random.randint(1,101))
else:
    print ('Please enter a valid number.')

