# The tasks to be performed are listed in 04-preparation.txt.
# There's one task per line. Each line starts with the one-word name for that task,
# followed by the time that task takes, and finally the names of all the tasks it depends on.

# There's no particular order in the file: tasks can be listed in any order,
# and the dependencies can be listed in any order on each line.
# There are no cycles in the dependencies: no task depends on a task which depends on it (directly or indirectly).

# Part 1
# Given the instructions file in 04-preparation.txt, how long will it take you to complete all the tasks?

class BBQ:
    def __init__(self):
        self.tasks = []
        self.time = 0

    def totalTime(self, input):
        count = 0
        with open(input, 'r') as f:
            for line in f:
                items = line.strip('\n').split(' ')
                count = count + int(items[1])
        return count

mybbq = BBQ()
print(mybbq.totalTime('preperation.txt'))

