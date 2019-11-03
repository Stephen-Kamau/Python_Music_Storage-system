#searches file

import sqlite3
import os
import databaseCreate

#seacrh function
db=sqlite3.connect("SongStorage.db")
def searchSong(searchBy , searchText):
	databaseCreate.createDb()
	db =  """SELECT * FROM song  WHERE ? = ? """(searchBy ,searchText)

	try:
		cur = db.cursor()
		cur.execute(db)
		output=cur.fetchall()
		db.close()
	except Exception as e:
		raise e
		print("There was a problem while accessing our systems")
		input("press Enter to continue")
		return

	print("===================================")
	print("SEARCHED RESULTS ARE HERE:")
	print("===================================")
	if output == ():
		print("NO RECORDS FOUND")
		print("===================================")

	else:
		for entry in output:
			print("Title:  " + entry[0])
			print("Star:  " + entry[0])
			print("Costar:  " + entry[0])
			print("Year:  " + entry[0])
			print("Genre:  " + entry[0])

			print("===================================")
	input("Press enter to continue")

#take user inputs and run the function above to query the database
def searchLookup():
	print ("""
	 ===============================
	 DVD LOOKUP:
	 ===============================
	 Enter the criteria to look up by:
	 1 - Song title
	 2 - Star
	 3 - Costar
	 4 - Year released
	 5 - Genre""")

	choice = input("\nType a number and press enter: ")
	try:
		choice = int(choice)
		if choice == 1:
			searchBy = "title"
			searchText = input("Enter the song title to search for: ")

		elif choice == 2:
			searchBy = "star"
			searchText = input('Enter the song star name to search for: ')
		 
		elif choice == 3:
			searchBy = "costar"
			searchText = input("Enter the song costar name to search for: ")

		elif choice == 4:
			searchBy = "year"
			searchText = input("Enter the song release year to search for: ")

		elif choice == 5:
			searchby = "genre"
			print ("""
			 Enter the genre to search for:
			 1 - Drama
			 2 - reggae
			 3 - Rnb
			 4 - Romance
			""")
			entrychoice=input("Your value please!\t")
			try:
				entrychoice = int(entrychoice)
				if entrychoice == 1:
					searchText = "Drama"
				elif entrychoice == 2:
					searchText = "Reggae"

				elif entrychoice == 3 :
					searchText = "Rnb"
				elif entrychoice == 4:
					searchText = "Romance"

				else:
					print("Error in your choice")
					input("Press enter to return to the main menu:")
					
			except:
				print("Please enter only numbers please!")

	except:
		print("Choose an integer please!")
	searchSong(searchBy , searchText)

