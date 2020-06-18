import re
file = open('test_mbox-short.txt')
for line in file:
    if line.startswith('From: '):
        print(line.strip())
        organization = re.search('@.+', line).group()[1:]
        print(organization, len(organization))
        