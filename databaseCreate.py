import sqlite3

#file whre the database is being created
#db=sqlite3.connect("SongStorage.db")

#create the database and connect it using a function
def createDb():
	db=sqlite3.connect("SongStorage.db")

	#create cursor object and then create the table
	cur=db.cursor()
	tbl="""CREATE TABLE IF NOT EXISTS song (songId  int primary key ,title text not null,
	star text not null,costar text not null , year text not null ,genre text not null)"""
	try:
	 	cur.execute(tbl)
	 	db.commit()
	except:
	 	print("Error while tryng to connect to the server")
