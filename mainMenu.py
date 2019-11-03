import databaseCreate
import addSong
import searches
import modify
import delete
import csvReport
import sqlite3
 

#call the database first
databaseCreate.createDb()
#MAIN MENU
#db=sqlite3.connect("SongStorage.db")
def Menu():
	#os.system(‘cls’)
	print ("""
	 ================================
	 DVD DATABASE
	 ================================
	 1 - Add a song details to the database
	 2 - Search inventory
	 3 - Modify song record
	 4 - Delete song record
	 5 - Export listing to CSV
	 6 - Exit
	 ================================
	 """)
	choice = int(input("Enter a choice and press enter: "))
	#return choice
	 
	#TAKE CHOICE AND LAUNCH MODULE
	#choice = Menu()
	if choice == 1:
		addSong.getInputs()
	elif choice == 2:
		searches.searchLookup()
	elif choice == 3:
		modify.ModifySong()
	elif choice == 4:
		delete.DeleteItem()
	elif choice == 5:
		csvReport.WriteCSV()
	elif choice == 6:
		pass
	else:
		print("You have selected unwanted option")

Menu()