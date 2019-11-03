import sqlite3
import csv
import databaseCreate


#FUNCTION TO WRITE ENTIRE DVD LIST TO CSV
db=sqlite3.connect("SongStorage.db")
def WriteCSV():
	content = "SELECT * FROM song"
	 
	try:
		databaseCreate.createDb()
		cur.execute(content)
		output = cur.fetchall()
		cur.close()
		db.close()
	except:
		print ("THERE WAS A PROBLEM ACCESSING THE DATABASE!")
		input("Press Enter to return to the menu: ")
		return

	try:
		print ("===============================")
		print ("EXPORT DATABASE TO CSV:")
		print ("===============================")
		filename = input("Enter base filename (will be given a .csv extension): ")
		filename = filename + ".csv"
		writer = csv.writer(open(filename, "wb"))
		writer.writerow(("TITLE", "STAR NAME", "COSTAR NAME", "YEAR", "GENRE"))
		writer.writerows(output)
		print (filename +"successfully written, press Enter to continue: ")
		input("")
		return
	except:
		print ("ERROR WRITING FILE!")
		input("Press Enter to return to the menu: ")