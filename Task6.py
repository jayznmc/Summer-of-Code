# You want people who know each other to sit together. 
# But as each person knows only a few of the attendees directly, 
# you want to make it easy for people to get to know each other.

# On each line, there are two names, indicating that the two people are friends
# Two people are introducable if they have a mutual friend.

# Once two people know each other, they can perform more introductions and hence expand the range of people each of them knows.
# A person's friendship group is In the set of people they will eventually know after following all the possible introductions

# Part 1

# The friendships among your guests are listed in 06-friendships.txt. How many friendship groups are there?
# (The file contains exactly one friendship per line. On each line, there are two names, separated by spaces. 
# Names can have non-letters in them, such as "Ella-Louise", but no name contains a space.)

groups = {}
groupID = 0

for line in open('friendships.txt'):
  #create sets of friendships
  inGroups = {}
  hasFriend = False
  currentGroup = []
  friends = set(line.split())

  for key,group in groups.items():
    # check if friend in a group
    if friends & group:
      if len(currentGroup) == 0:
        groups[key].update(friends)
      currentGroup.append(key)
      
    #not in group - new group created
  if len(currentGroup) == 0:
    groups[groupID] = set(friends)
    groupID += 1

  # Union of sets, to combine 'introducable' friends
  elif len(currentGroup) > 1:
    for i in currentGroup[1:]:
      groups[currentGroup[0]] = groups[currentGroup[0]].union(groups[i])

      #remove orignal group to prevent duplicates
      del groups[i]

print((groups))
print(len(groups))
