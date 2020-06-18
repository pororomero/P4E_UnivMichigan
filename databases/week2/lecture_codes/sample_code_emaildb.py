import sqlite3

# create a file 'emaildb.sqlite' and make a connection to it
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# DROP TABLE removes one or more tables, this will do nothing since were starting from scratch
cur.execute('DROP TABLE IF EXISTS Counts')
# create a table called Counts which contains email (a text) and count (int), dictionary like
cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    # select the count where email is email stored above
    # '?' is a placeholder that will be replaced by email (single tuple, weird syntax)
    # opening a set of records
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    # information we get from database, None if no email found or exists
    row = cur.fetchone()
    if row is None:
        # set email's value to 1
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        # increment the email's value
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    # write it it disk
    conn.commit()

# https://www.sqlite.org/lang_select.html
# reading the database e jus created
# select the top 10 email arranged by count in descending order
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    # email = row[0], count = row[1]
    print(str(row[0]), row[1])

# close the connection
cur.close()
