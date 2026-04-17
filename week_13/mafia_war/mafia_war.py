# ==============================
# CLASS: MafiaPerson
# Represents ONE mafia member
# Stores their personal data
# ==============================

class MafiaPerson:
    def __init__(self, first_name, last_name, hp, skill_set):
        self.first_name = first_name  # store first name
        self.last_name = last_name    # store last name
        self.hp = hp                  # store HP as an integer
        self.skill_set = skill_set    # store their skill description
    # This controls how the object prints
    # Called automatically when you print(member)
    def __str__(self):
        return f"{self.first_name} {self.last_name} | HP: {self.hp} | Skill: {self.skill_set}"

# ==============================
# CLASS: MafiaFamily
# Represents a WHOLE mafia family
# Stores a list of members
# ==============================

class MafiaFamily:
    # Creates a new mafia family
    def __init__(self, family_name):
        self.family_name = family_name   # store family name
        self.members = []                # empty list to hold members
    # Add a member to the family list
    def add_member(self, person):
        self.members.append(person)
    # Display all members in the family
    def display_family(self):
        print(f"\n{self.family_name}")
        print("-" * 40)
        # Loop through each member and print them
        for member in self.members:
            print(member)
    # Calculate total HP of the family
    # Used to compare families in battle
    def get_total_hp(self):
        total_hp = 0   # start counter at 0
        # Add each member's HP to total
        for member in self.members:
            total_hp += member.hp
        return total_hp   # send total back


# ==============================
# LOAD GARLIC FAMILY FROM CSV
# ==============================

garlic_family = MafiaFamily("The Garlic Bread Cartel")
file1 = open("week_13\\mafia_war\\mafia_family_1.csv", "r")
# Skip header row using [1:]
for line in file1.readlines()[1:]:
    # Remove newline and split by commas
    parts = line.strip().split(",")
    # Extract values from list
    first_name = parts[0]
    last_name = parts[1]
    hp = int(parts[2])   # convert HP from string → int
    skill = parts[3]
    # Create MafiaPerson object
    person = MafiaPerson(first_name, last_name, hp, skill)
    # Add person to family
    garlic_family.add_member(person)
# CLOSE FILE AFTER LOOP (important!)
file1.close()

# ==============================
# LOAD RIGATONI FAMILY FROM CSV
# ==============================

rigatoni_family = MafiaFamily("Rigatoni Syndicate")
file2 = open("week_13\\mafia_war\\mafia_family_2.csv", "r")
for line in file2.readlines()[1:]:
    parts = line.strip().split(",")
    first_name = parts[0]
    last_name = parts[1]
    hp = int(parts[2])
    skill = parts[3]
    person = MafiaPerson(first_name, last_name, hp, skill)
    rigatoni_family.add_member(person)
file2.close()

# ==============================
# DISPLAY BOTH FAMILIES
# ==============================

garlic_family.display_family()
rigatoni_family.display_family()

# ==============================
# GET TOTAL HP FOR BOTH FAMILIES
# ==============================

garlic_hp = garlic_family.get_total_hp()
rigatoni_hp = rigatoni_family.get_total_hp()
print(f"Garlic Family HP: {garlic_hp}")
print(f"Rigatoni Family HP: {rigatoni_hp}")

# ==============================
# WAR LOGIC
# Compare HP totals to pick winner
# ==============================

print("FIGHT!!!")
if garlic_hp > rigatoni_hp:
    print("Garlic Supremacy")
elif rigatoni_hp > garlic_hp:
    print("Rigatoni Reigns")
else:
    print("Tie")