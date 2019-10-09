#Dungeon and Dragons 5th Addition Stat Roller. v3#
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
Rage = 2
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
#exitflag = 'false'
#while exitflag == 'false':
Role=input('|---------{Mori Stat Card}---------|\n'
      '| Strength     = 16                |\n'
      '| Dexterity    = 12                |\n'
      '| Constitution = 16                |\n'
      '| Intelligence = 6                 |\n'
      '| Wisdom       = 10                |\n'
      '| Charisma     = 14                |\n'
      '|-------{Proficiency Skills}-------|\n'
      '| Saves: Strength, Constitution    |\n'
      '|                                  |\n'
      '| Skills: Animal Handling,         |\n'
      '| Athletic, Intimidation, Survival |\n'
      '|----------------------------------|\n'
      '| Acrobatics=1 | Animal Handling=2 |\n'
      '| Arcana=-2    | Athletics=5       |\n'
      '| Deception=2  | History=-2        |\n'
      '| Insight=0    | Intimidation=4    |\n'
      '| Invest=-2    | Medicine=0        |\n'
      '| Nature=-2    | Perception=0      |\n'
      '| Performance=2| Persuasion=2      |\n'
      '| Religion=-2  | Sleight of Hand=1 |\n'
      '| Stealth=1    | Survival=2        |\n'
      '|----------------------------------|\n'
    'What stat are you going rolling?\n1.)Ability Check\n2.)Attack Role\n3.)Deathsaving Throw.\n(Enter answer as associated number.)');
if Role == '1':
               Role_Type=input('What stat are you rolling?(Please enter associated number)\n1.) Acrobatics\n2.) Animal Handling\n3.) Arcana\n4.) Athletics\n5.) Deception\n6.) History\n7.) Insight\n8.) Intimidation\n9.) Investigation\n10.) Medicine\n'
      '11.) Nature\n12.) Perception\n13.) Performance\n14.) Persuasion\n15.) Religion\n16.) Sleight of Hand\n17.) Stealth\n18.) Survival\n Selection:');
               if Role_Type == '1':
                   for x in range(1):
                       y=(random.randint(1,20))
                       z=y + Acrobatic
                   print("You Rolled a :",y,"\nThe Total for Acrobatics Rolled is :",z)
               elif Role_Type == '2':
                   for x in range(1):
                       y=(random.randint(1,20))
                       z=y + Animal_Handlin
                       print("You Rolled a :",y,"\nThe Total for Animal Handling Rolled is :",z)
               elif Role_Type == '3':
                   for x in range(1):
                       y=(random.randint(1,20))
                       z=y + Arcan
                       print("You Rolled a :",y,"\nThe Total for Arcana Rolled is :",z)
               elif Role_Type == '4':
                   for x in range(1):
                       y=(random.randint(1,20))
                       z=y + Athletic
                       print("You Rolled a :",y,"\nThe Total for Athletics Rolled is :",z)
               elif Role_Type == '5':
                   for x in range(1):
                       y=(random.randint(1,20))
                       z=y + Deceptio
                       print("You Rolled a :",y,"\nThe Total for Deception Rolled is :",z)
               elif Role_Type == '6':
                   for x in range(1):
                       y=(random.randint(1,20))
                       z=y + Histor
                       print("You Rolled a :",y,"\nThe Total for History Rolled is :",z)
               elif Role_Type == '7':
                   for x in range(1):
                       y=(random.randint(1,20))
                       z=y + Insigh
                       print("You Rolled a :",y,"\nThe Total for Insight Rolled is :",z)
               elif Role_Type == '8':
                   for x in range(1):
                       y=(random.randint(1,20))
                       z=y + Intimidatio
                       print("You Rolled a :",y,"\nThe Total for Intimidation Rolled is :",z)
               elif Role_Type == '9':
                   for x in range(1):
                       y=(random.randint(1,20))
                       z=y + Investigatio
                       print("You Rolled a :",y,"\nThe Total for Investigation Rolled is :",z)
               elif Role_Type == '10':
                   for x in range(1):
                       y=(random.randint(1,20))
                       z=y + Medicin
                       print("You Rolled a :",y,"\nThe Total for Medicine Rolled is :",z)
               elif Role_Type == '11':
                   for x in range(1):
                       y=(random.randint(1,20))
                       z=y + Natur
                       print("You Rolled a :",y,"\nThe Total for Nature Rolled is :",z)
               elif Role_Type == '12':
                   for x in range(1):
                       y=(random.randint(1,20))
                       z=y + Perceptio
                       print("You Rolled a :",y,"\nThe Total for Perception Rolled is :",z)
               elif Role_Type == '13':
                   for x in range(1):
                       y=(random.randint(1,20))
                       z=y + Performanc
                       print("You Rolled a :",y,"\nThe Total for Performance Rolled is :",z)
               elif Role_Type == '14':
                   for x in range(1):
                       y=(random.randint(1,20))
                       z=y + Persuasio
                       print("You Rolled a :",y,"\nThe Total for Persuasion Rolled is :",z)
               elif Role_Type == '15':
                   for x in range(1):
                       y=(random.randint(1,20))
                       z=y + Religio
                       print("You Rolled a :",y,"\nThe Total for Religion Rolled is :",z)
               elif Role_Type == '16':
                   for x in range(1):
                       y=(random.randint(1,20))
                       z=y + Sleight_of_Han
                       print("You Rolled a :",y,"\nThe Total for Sleight of Hand Rolled is :",z)
               elif Role_Type == '17':
                   for x in range(1):
                       y=(random.randint(1,20))
                       z=y + Stealt
                       print("You Rolled a :",y,"\nThe Total for Stealth Rolled is :",z)
               elif Role_Type == '18':
                   for x in range(1):
                       roll=(random.randint(1,20))
                       z=roll + Surviva
                       print("You Rolled a :",y,"\nThe Total for Survival Rolled is :",z)
               else:
                   print('invalid answer')
elif Role == '2':
    Attack_Type=input('What weapon are you using to attack the enemy?\n1.) Greataxe\n2.) Hatchet\n3.) Other\nSelection:')
    if Attack_Type == '1':
        Raging=input('Are you raging?\n 1.)Yes or 2.)No\n Selection:')
        if Raging=='1':
            for x in range(1):
                y=(random.randint(1,6))
                z=(random.randint(1,6))
                a=y + z + 2 + 3
                print("You dealt",a,"Slashing Damage With Rage.")
        else:
            for x in range(1):
                y=(random.randint(1,6))
                z=(random.randint(1,6))
                a=y+z+3
                print("You dealt",a,"Slashing Damage.")
    elif Attack_Type =='2':
        Raging2=input('Are you raging?\n Yes or No\n Selection:')
        if Raging2=='1':
            for x in range(1):
                y=(random.randint(1,6))
                z=y+2+Strength
                print("You dealt",z,"Slashing Damage With Rage.")
        else:
            for x in range(1):
                y=(random.randint(1,6))
                a=y+3
                print("You dealt",a,"Slashing Damage.")
    else:
        Weapon_Type=input('Is it a finesse weapon?\n1.) Yes\n2.) No\nSelection:')
        if Weapon_Type=='1':
                Weapon_Type2=input('What damage dice is being used?\n1.) D4\n2.) D6\n3.) D8\n4.) D10\n5.) D12\n Selection:')
                if Weapon_Type2== '1':
                    for x in range(1):
                        y=(random.randint(1, 4))
                        z= Dexterity + y
