import sqlite3
Mydata=sqlite3.connect('Movie.db')
datacur=Mydata.cursor()
try:
    datacur.execute("CREATE TABLE Movies(Name PRIMARY KEY NOT NULL,Actor,Actress,Director NOT NULL,Year INTEGER NOT NULL);")
except:
    Mydata.rollback()
try:
    Name=input("Enter movie name: ")
    Actor=input("Enter Actor name: ")
    Actress=input("Enter Actress name: ")
    Director=input("Enter Director name: ")
    Year=int(input("Enter Year: "))
    if(Name==""):
        Name=None
    if(Director==""):
        author=None
    datacur.execute("INSERT INTO Movies VALUES (?,?,?,?,?);",(Name,Actor,Actress,Director,Year))
    Mydata.commit()
    print("\nData added succesfully")
except:
    Mydata.rollback()
    print("\nError occured while adding! Check your data")
Mydata.close()
