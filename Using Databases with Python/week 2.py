import sqlite3

conn = sqlite3.connect('orgUpdate.sqlite')

c = conn.cursor()

c.execute("DROP TABLE IF EXISTS Counts")
c.execute("CREATE TABLE Counts(org text,count INTEGER)")

fhand = open("mbox.txt")

for line in fhand:
    if line.startswith("From:"):
        sList = line.split("@")

        Name = sList[1]
        c.execute("SELECT count FROM Counts WHERE org = ?",(Name,))
        row = c.fetchone()
        if row is None:
            c.execute("INSERT INTO Counts (org,count) VALUES(?,1)",(Name,))
        else:
            c.execute("UPDATE Counts SET count = count+1 WHERE org = ?",(Name,))
        conn.commit()

query = "SELECT org,count FROM Counts ORDER BY count DESC LIMIT 10"
for row in c.execute(query):
    print(str(row[0]),row[1])
c.close()