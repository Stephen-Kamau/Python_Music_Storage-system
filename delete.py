import sqlite3
import databaseCreate


#file for deleting the choosen entries
#RUN THE SQL STATEMENT TO DELETE THE SELECTED RECORD
db=sqlite3.connect("SongStorage.db")
def deleteSong(songToDelete):
	try:
		databaseCreate.createDb()
		delete = "DELETE song FROM song WHERE title = ?",(songToDelete,) 
		cur = db.cursor()
		cur.execute(delete)
		db.commit()
		cur.close()
		db.close()
		input("Item deleted, press enter to continue: ")
	except:
		print ("THERE WAS A PROBLEM DELETING THE RECORD")
		input("Press Enter to continue: ")

 
 
#TAKE USER INPUT AND RUN FUNCTION TO DELETE THE SELECTED RECORD
def DeleteItem():
	print ("===============================")
	print ("DELEte  A SONG RECORD:")
	print ("===============================")
	 
	songToDelete = input("\nEnter the title of the DVD to delete:\t")
	delete = "DELETE song FROM song WHERE title = ? "(songToDelete,)
	try:
		cur = db.cursor()
		cur.execute(delete)
		searchResult = cur.fetchall()
		if searchResult[0] == ():
			raise
			
	except:
		print ("THERE WAS A PROBLEM ACCESSING THE RECORD IN THE DATABASE!")
		input("Press Enter to continue: ")
		return

	print( "===============================")
	print ("delete song  RECORD:")
	print( "===============================")
	print ("1 - Title:\t" + modifyResult[0][0])
	print ("2 - Star:\t" + modifyResult[0][1])
	print ("3 - Costar:\t" + modifyResult[0][2])
	print ("4 - Year:\t" + modifyResult[0][3])
	print ("5 - Genre\t"+ modifyResult[0][4])
	print ("===============================")
	input("Press enter to continue: ")

	print("""
			 Are you sure you want to delete? Enter a choice and press enter
		 (Y/y = yes, Anything else = No)
		 """)
		 

	choice = input("\t")
	if (choice == "Y" or choice == "y"):
		deleteSong(songToDelete)
	else:
		c.close()
		db.close()
		input("Item NOT deleted, press enter to continue: ")