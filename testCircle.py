# class circle1:
#     def __init__(self, radius):
#         self.__radius = radius
#     def setRadius(self, newValue):
#         if newValue >= 0:
#             self.__radius = newValue
#         else:
#             raise ValueError("Value must be positive")
#     def area(self):
#         return 3.14159 * (self.__radius ** 2)

# class circle2:
#     def __init__(self, radius):
#         self.__radius = radius    
    
#     def __setRadius(self, newValue):
#         if newValue >= 0:
#             self.__radius = newValue
#         else:
#             raise ValueError("Value must be positive")
#     radius = property(None, __setRadius)

    
#     @property
#     def area(self):
#         return 3.14159 * (self.__radius ** 2)

from tkinter import *
from tkinter.messagebox import showinfo

class MyGui(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        button = Button(self, text='press', command = self.reply)
        button.pack()
    def reply(self):
        showinfo(title = 'popup', message='button pressed')

if __name__ == '__main__':
    window = MyGui()
    window.pack()
    window.mainloop()




    
    