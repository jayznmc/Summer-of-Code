# Q1
#
#All instructions and comments begin in the first character of a line: there are no
# whitespace characters before an instruction or comment starts.
#You can assume that all the lines are either comments or valid instructions: there's no
#  need to validate the input file. In particular, there are no blank lines in the file.


#Given the instructions file in 01-mowmaster.txt, how many instructions are there?


def count_instructions(input):
    f = text.readlines()
    count = 0

    for line in f:
        if not line.startswith('#'):
            count = count + 1
    return count

text = open('mowmaster.txt', 'r', encoding='utf8')
print(count_instructions(text))


# Part 2

#All instructions and comments begin in the first character of a line: there are no whitespace characters
#before an instruction or comment starts.
#You can assume that all the lines are either comments or valid instructions: there's no need to validate the input file.
#  In particular, there are no blank lines in the file.
#If the Mowmaster starts at x = 0, y = 0 and facing to the right, if it follows the instructions above
# it will end up at position x = 90, y = -48. As the Mowmaster can only travel in the cardinal directions,
#  it would need to travel 90 + 48 = 138 metres to return to its starting place.

#The instructions are still file in 01-mowmaster.txt.
# After following those instructions, how far would the Mowmaster travel
# to return to its starting point? (Just enter the number of metres, not any units or similar.)


def distance_from_start(input):

    position = (0, 0)
    bearing = [0,0,0,0] #element order is E, S, W, N
    pointer = 0 # start = looking east


    for action in input:
        if action[0] == '#':
            pass
        if action[0] == "A":
            pointer = pointer - 1
            if pointer < 0:
                pointer = 3
        if action[0] == "C":
            pointer = pointer + 1
            if pointer > 3:
                pointer = 0
        if action[0] == "F":
            bearing[pointer] = bearing[pointer] + int(action[1:])
    posX = bearing[0] - bearing[2]
    posY = bearing[1] - bearing[3]
    return(abs(posX)+abs(posY))


text = open('mowmaster.txt', 'r', encoding='utf8')
print(distance_from_start(text))
