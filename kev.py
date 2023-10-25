What is the difference between float, int, boolean and string types


"""use https://www.online-python.com/ for the below activities, copy and paste this lab into your workbook and make notes along side as you work through the activities"""


Variable, types and print statements


pages_per_book = 135
number_books = 30

#calculate the total number of pages

total_pages = pages_per_book*number_books

#complete a print statement to show how many pages
#print("with " + number_books + " books we'll need " + total_pages + " pages")

#uncomment one statement at a time and see how it works
#f before "", makes the string a formatted string or f string which allows the sytax

#print(f"With", number_books, "books we'll need", total_pages, "pages")
#print(("With {} books we'll need {} pages").format(number_books, total_pages))
#print((f"With {number_books} books we'll need {total_pages} pages"))
#print((f"With {number_books} books\nwe'll need {total_pages} pages"))


# we are going to explore string methods now, go to https://www.w3schools.com/python/default.asp to search for what you need

textbook_name = "network programmability and automation" 

# look at the built-in python functions and methods available for strings and 
# figure how to print the number of characters in the string, this is a function
# complete the print statement
#print ()

#using a built-in python functions, what data type is textbook_name
#print()



# now we will use methods, methods are used on objects
# if we have an object of string class, then we can use the methods associated with strings
# notice the syntax difference between calling functions and using methods

#convert all letters in the string into upper case
#print(textbook_name.upper().islower())

# make all of the first letters of each word uppercase

#verify that all characters in the string are lowercase

#try something weird, convert all of the characters into uppercase and then test if they are all lowercase in the same statement

#check to see if the word "and" is in the textbook_name

#how many letter 'a' are in the string?

#string can be indexed using [], 
# there is only 15 characters availble for listing the book title, print only the first 15 characters
print (textbook_name[0:15])

# print only "etwork"

# print "The name of the book is Network Programmabilty and Automation"






-----------------------------------------------------------

# working with lists, two ways to make a list
# two different ways to make lists

textbook_list = ["network programmability and automation", "automation made simple", "practical ansible", "python for network scripting", "containers in action"]
author_list = list(("Jason Adalman", "Gaurav Narula", "Oluwole Kayoke", "Daisy Chan", "Alan D'Sousa"))

print(author_list)

# how many elements are in the textbook_list and author_list (using a python built-in function)



#check out the methods available for lists
# sort the list alphabetically

# add a new book to the list

# using the if x 'in' [] command, find out if the author is in the author_list and print a response saying that is or is not in the list; alter the string if necessary to do the comparision
title = 'Practical ansible'
if title in textbook_list:
    print (f"'{title}'' is in the list")
else:
    print (f"'{title}' is NOT in the list")
#think about what is happening here, in 

# is "kevin ramdas" in the author_list
author = "kevin ramdas"



# using a for loop print all of the textbooks in the textbook_list, try numbering your list with each entry on a separate online-python

# add a new textbook title to the list "JSON marking up" and a new author to the author_list "Stephanie Verges", you can use a list methods

# Change the second author to "Narula Gaurav"

# add a new third title in th textbook_list called "Scripting the way to success" and a new author named "Aimee Dobresky"

# now we want to create a new list of textbooks that only has network in its name, try using https://www.w3schools.com/python/python_lists_comprehension.asp
network_textbooks = []

# using the code below, what is the difference between, 
new_list = textbook_list
#Vs
new_list2 = textbook_list.copy()

textbook_list [0] = "network automation and programmability"
print("textbook_list \n", textbook_list)
print("new_list \n", new_list)
print("new_list \n", new_list2)


something else you can do, you can split string up in words and store it in a list, and do actions to the string

wordlist_textbook_title = textbook_name.split()



#try the following code, we change a string into a list and then the list back into a string
#textbook_name = "network programmability and automation" 
#wordlist_textbook_title = textbook_name.split("a")
#print(wordlist_textbook_title)
#print("a".join(wordlist_textbook_title))


#now we going to use another data structure called a tuple, you usually stored related pieces of information together

