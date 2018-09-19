# Barbeques are almost guaranteed to bring out the rain.
# You need to pick a good day, so you've had a look at the rainfall records for around here.
# They're listed in the 02-rainfall.txt file, with one record per line.

#Q1

# The trouble is, the rainfall sensor isn't that reliable and keeps generating data after you've told it not to.
# You've marked the limit of the valid answers with the sentinel value `9999`.
# All the values up to, but not including, the sentinel are the rainfall numbers you're after.
# You should ignore `9999` and all the values afterwards.

def count_valid_records(input):
    count = 0
    for record in input:
        if int(record) >= 9999:
            return count
        else:
            count = count + 1

text = open('rainfall.txt', 'r', encoding='utf8')
print(count_valid_records(text))

