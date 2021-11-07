# import tkinter

# window = tkinter.Tk()
# window.title("My GUI")
# window.minsize(500, 300)

# # label
# my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "italic"))
# my_label.pack(side="bottom")


# my_label["text"] = "New Text"
# my_label.config(text="New Text")

# Button






# # keep the window open
# window.mainloop() 


# def add(*args):
# 	print(args[1])
# 	sum = 0
# 	for n in args:
# 		sum += n
# 	return sum   


# print(add(3,5,6))

# def calc(e, **kwargs):
# 	print(kwargs)
# 	for key, value in kwargs.items():
# 		print(key, value)
# 	print(kwargs["mul"])

	



# calc(2, add=3, mul=23)


# class Car(object):
# 	"""docstring for Car"""
# 	def __init__(self, **kw):
# 		self.make = kw["make"]
# 		self.model = kw["model"]

# my_car = Car(make="nissan", model="GT-B")
# print(my_car.model)
# print(my_car.make)



from tkinter import *

window = Tk()
window.title("My GUI")
window.minsize(500, 300)
window.config(padx=100, pady=200)

# label
my_label = Label(text="I am a label", font=("Arial", 24, "italic"))
my_label.pack(side="left")


# Button
def button_clicked():
	# print("I got monah"
	new_text = input.get()
	my_label["text"] = new_text  # setting the text to the input from user



button = Button(text="click me", command=button_clicked)
button.pack()


# Entry

input = Entry(width=10)
input.pack()
# input.get()


window.mainloop()



