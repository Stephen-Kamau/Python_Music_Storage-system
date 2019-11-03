import sqlite3
import databaseCreate

#this files is for making changes to the database
db=sqlite3.connect("SongStorage.db")

def ModifySong():
	databaseCreate.createDb()
	print ("===============================")
	print ( "MODIFY A the database RECORD:")
	print ("===============================")
	 
	songTitle = input("\nEnter the title of the Song to modify: ")
	 
	search = "SELECT * FROM song WHERE title =?",(songTitle,)
	 
	try:
		c = db.cursor()
		c.execute(search)
		searchResult = c.fetchall()
		if searchResult[0] == ():
			raise

	except:
		print("THERE WAS A PROBLEM ASSECCING THE RECORD IN THE DATABASE")
		input("Press enter to continue")
		return
	try:
		print ("===============================")
		print ("song TO MODIFY:")
		print ("===============================")
		print ("1 - Title:\t" + searchResult[0][0])
		print ("2 - Star:\t" + searchResult[0][1])
		print ("3 - Costar:\t"+ searchResult[0][2])
		print ("4 - Year:\t" +searchResult[0][3])
		print ("5 - Genre:\t"+ searchResult[0][4])
		print ("===============================")
	except:
		print("Error")

		choice = input("Type the number for the field you want to modify and press Enter: ")
		titleChanged = False
		modify = ""
		newvalue = ""
		if choice == 1:
			modify = "title"
			newvalue = input("Enter the new song title name: ")
			titleChanged = True

		elif choice == 2:
			modify = "star"
			newvalue = input("Enter the new song star name: ")

		elif choice == 3:
			modify = "costar"
			newvalue = input("Enter the new song costar name: ")

		elif choice == 4:
			modify = "year"
			newvalue = input("Enter the new song release year: ")

		elif choice == 5:
			modify = "genre"
			print ("""
			 Enter the genre to apply to this song:
			 1 - Drama
			 2 - reggae
			 3 - Rnb
			 4 - Romance
			""")
			entrychoice=int(input("Choose the genre"))

			if entrychoice == 1:
				newvalue = "Drama"

			elif entrychoice == 2:
				newvalue = "Reggae"

			elif entrychoice == 3 :
				newvalue = "Rnb"

			elif entrychoice == 4:
				newvalue = "Romance"

			else:
				print("Error in your choice")
				input("Press enter to return to the main menu:")
				return
		
		update="UPDATE song SET ? = ? WHERE title =?",(modify , newvalue ,songTitle)
		try:
			cur=db.cursor()
			cur.execute(update)
			updated=cur.fetchall()
			db.commit()
			db.close()
		except Exception as e:
			print("ERROr Occurred while updateing the record")
			input("Press enter to continue")
		'''
		print( "===============================")
		print ("MODIFIED RECORD:")
		print( "===============================")
		print ("1 - Title:\t" + updated[0][0])
		print ("2 - Star:\t" + updated[0][1])
		print ("3 - Costar:\t" +updated[0][2])
		print ("4 - Year:\t" +updated[0][3])
		print ("5 - Genre\t"+ updated[0][4])
		print ("===============================")
		input("Press enter to continue: ")
		'''
