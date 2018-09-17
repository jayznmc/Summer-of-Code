# Meet the Mowmaster 5000, the very latest in robotic gardening technology
# from a world-leading home-automation/weaponry company. 
# The Mowmaster lets you put your feet up while it trims the grass, bins the cuttings – it can even walk the dog!
# Any resemblance to a small tank is purely coincidental and occasional news reports of mass carnage 
# left in the wake of a summer’s lawnmowing have just made it cheaper to buy.
# As well as a completely autonomous mode in which the Mowmaster blunders around
# a garden trimming grass and scaring small animals, the robot can download stored 
# programs consisting of a series of commands, like this.

#Program counts the number of lines, that do not start with '#'

def count_instructions(input):
    f = text.readlines()
    count = 0

    for line in f:
        if not line.startswith('#'):
            count = count + 1
    return count

text = open('mowmaster.txt', 'r', encoding='utf8')
print(count_instructions(text))
