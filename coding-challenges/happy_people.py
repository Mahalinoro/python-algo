# You have 8 000 000 000Ar cash, you have to make one choice among:
# buy candies, each cost 200Ar, makes 1 people happy and 10 others unhappy
# or
# build a colosseum at 6 000 000 000Ar each, makes 10 000 people happy and 3 000 000 others unhappy
# or
# buy ambulances, each cost 160 000 000Ar, makes 10 000 people happy and 1 000 unhappy

# Which one is the best choice, that maximize the number of unhappy people?

def IAmRich(cash, choices):
    c_choices = {}
    i = 0
    for c in choices:
        c_choices[i] = (cash // c[0]) * c[2]    
        i += 1   
    
    max_unhappy = c_choices[0]
    index = 0
    for c, value in c_choices.items():
        if value > max_unhappy:
            max_unhappy = value
            index = c

    return index