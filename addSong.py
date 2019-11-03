import sqlite3
import os
import random
import databaseCreate

db=sqlite3.connect("SongStorage.db")

def insertSong(title,star,costar,year,genre):
	#sqlite definition
	try:
		databaseCreate.createDb()
		database="""INSERT INTO song (title,star,costar,year,genre) VALUES (?,?,?,?,?)""" ,(title,star,costar,year,genre)
		cur = db.cursor()
		cur.execute(database)
		print("You Have Successful Added An Entry")
		db.commit()
		db.close()
	except Exception as error:
		print(error)
		print("Thre was a problem while processing the entry")
		input("Press enter to continuw")
		return

		#TAKE USER INPUT AND RUN FUNCTION TO INSERT INTO DATABASE
def getInputs():
	print("====================================")
	print("ADD A SONG TO OUR DATABASE")
	print("====================================")
	title=input("Enter the song Title: ")
	star = input("Enter the name of the singer: ")
	costar = input("Enter the name of the song costars: ")
	year=input("Enter the year in which the song was created: ")
	try:
		year=int(year)
		if year <2019:
			print("Please choose the resent year!")
		elif year > 2030:
			print("Please choose the resent year!")
		else:
			year=year
	except:
		print("Please choose the correct for year only:")
	
	opt = input("""choose the genre of the song: 
	 1  Drama 
	 2  reggare  
	 3  rnb 
	 4  romance \n""")

	#get the results for genre
	try:
		opt=int(opt)
		if opt == 1:
			genre ="Drama"

		elif opt == 2:
			genre = "Reggae"

		elif opt == 3:
			genre = "Rnb"

		elif opt == 4:
			genre = "Romance"

		else:
			print("Error! while getting information")
			input("Press enter to continue")
	except:
		print("Only numbers Please!")

		
	#call the insert function
	insertSong(title,star,costar,year,genre)