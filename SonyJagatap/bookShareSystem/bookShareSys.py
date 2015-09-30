#Book share system
Booklist=[
	{'Name':"Learning Python",
	 'Author':"Mark Lutz",
	 'No':100,
	 'Description':"Powerful Object-Oriented Programming"},
	{'Name':"Python Programming",
	 'Author':"John Zelle",
	 'No':101,
	 'Description':"This book is designed to be used as the primary textbook in a college-level first course in computing."},
	{'Name':"Java A Begnner's Guide",
	 'Author':"Herbert Schildt",
	 'No':102,
	 'Description':"This book begins with the basics, such as how to create, compile, and run a Java program"},
	{'Name':"Effective Java",
	 'Author':"Joshua Bloch",
	 'No':103,
	 'Description':"This book is based on deeper understanding of the Java programming language"},
	{'Name':"MySQL Cookbook",
	 'Author':"Paul Dubois",
	 'No':104,
	 'Description':"Ideal for beginners and professional database and web developers"},
	{'Name':"Learn MySQL",
	 'Author':"Trevor Page",
	 'No':105,
	 'Description':"Learning about Databases and SQL"}
	]

#print Booklist[0].keys()
#print Booklist[1].values()
#print Booklist

def search(name):
	for i in Booklist:
		if i['Name'] == name:
			return i

def showmenu():
	print "*-----------------*"
	print "Book Search System"
	print "*-----------------*"
	print "Booklist     [1]"
	print "Search a Book[2]"
	print "Quit         [3]"

# Main Program
showmenu()
option = raw_input("Enter your choice [1/2/3]:")

if option == '1':
	# Display list of books
	print "List of Books"
	print "Name of Book  ----  Author ----  Description"
	for book in Booklist:
		print book['Name'], "----", book['Author'], "----", book['Description']
elif option == '2':
	bname = raw_input("Enter book title:")
	index = search(bname)
	try:
		assert(index)
	except:
		print "Book Not Found"
	else:
		print index['Name'],"--", index['Author'], "--", index['Description']
else:
	print "Invalid Option"