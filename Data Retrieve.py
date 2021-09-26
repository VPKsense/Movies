import sqlite3
Mydata=sqlite3.connect('Movie.db')
datacur=Mydata.cursor()
datacur.execute("SELECT * from Movies;")
print("---My Favourite Movies---",end="\n\n")
for i in datacur.fetchall():
    print("Movie: ",i[0])
    print("Actor: ",i[1])
    print("Actress: ",i[2])
    print("Director: ",i[3])
    print("Year: ",i[4])
    print()
aname=input("Enter actor name for movies: ")
datacur.execute("SELECT Name from movies WHERE Actor='"+aname+"';")
mnames=datacur.fetchall()
if(mnames==[]):
    print("No result found")
else:
    print()
    print("These are the movies of "+aname+":")
    for i in mnames:
        print(i[0])
Mydata.close()
