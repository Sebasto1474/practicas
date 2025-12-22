full_dot = '●'
empty_dot = '○'

def create_character(character_name, strength, intelligence, charisma):
    if type(character_name) != str:
        return "The character name must be a string"
    if character_name == "":
        return "The character should have a name"
    if len(character_name) > 10:
        return "The character name is too long"
    if " " in character_name:
        return "The character name should not contain spaces"
    
    stats = [strength, intelligence, charisma]
    for stat in stats:
        if type(stat) != int:
            return "All stats should be integers"
        if stat < 1:
            return "All stats should be no less than 1"
        if stat > 4:
            return "All stats should be no more than 4"
    if sum(stats) != 7:
        return "The character should start with 7 points"
    
    str_dots = (full_dot*strength)+(empty_dot*(10-strength))
    int_dots = (full_dot*intelligence)+(empty_dot*(10-intelligence))
    char_dots = (full_dot*charisma)+(empty_dot*(10-charisma))
    
    return f"""
{character_name}
STR {str_dots}
INT {int_dots}
CHA {char_dots}
"""
name = "Sanlope"

print(create_character(name,1,4,2))

