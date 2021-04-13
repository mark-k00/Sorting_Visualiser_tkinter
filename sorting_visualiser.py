#!/usr/bin/env python

'''
We used tkinter because its pythons built in gui module
We learned how to use the tkinter gui by watching youtube tutorials: 
https://www.youtube.com/watch?v=_lSNIrR1nZU
And also by using the internet for issues we had for example we used geek for geeks to figure out how to construct a combobox:
https://www.geeksforgeeks.org/combobox-widget-in-tkinter-python/
'''

from tkinter import * #the gui we used to run the program on
from tkinter import ttk #needed for multiple choice box (different sorting algorithm choices)
import algorithms

root = Tk()
root.title("Visual Sorting Algorithm - CA278 Group Project")
root.config(bg = "#f4d06f")

#variables used
selected_alg = StringVar()
size_var = StringVar()

#To generate the random set of numbers and call histogram function to make the histogram
def Generate():
   global data
   
   canvas.delete("all")
   size_entry = size_var.get()
   if size_entry == "":
      print "Select an amount of numbers to sort please!"
      return
   
   data = algorithms.numbers(size_entry)
   Button(UI_frame, text = "Generate Dataset", command = Generate).grid(row = 2,column = 0,padx = 5,pady = 5)
   sorting_alg = Label(UI_frame, text = "What sorting algorithm to use?", bg = "#f4a261").grid(row = 0, column = 2)
   alg_menu = ttk.Combobox(UI_frame, textvariable = selected_alg, values = ["Bubble Sort", "Selection Sort", "Insertion Sort"],state = "readonly")
   alg_menu.grid(row = 1, column = 2, padx = 5,pady = 5)
   alg_menu.current(0)
   sort = Button(UI_frame, text = "Sort Dataset", command = Sort).grid(row = 2,column = 2,padx = 5,pady = 5)
   
   return histogram(data)

#The function to form the random dataset into the histogram
#We found out how to construct a histogram in tkinter by help from stack overflow: https://stackoverflow.com/questions/24319683/put-histogram-in-tkinter-frame
def histogram(sort):
   canvas.delete("all")
   display_height = 200
   display_width = 600
   histogram_width = display_width / len(sort)
   offset = 5
   
   for i, height in enumerate(data): #we used https://realpython.com/python-enumerate/ to find out how to count up the list
      bar_width = (i * histogram_width) + offset
      bar_height = display_height - height
      max_width = (i + 1) * histogram_width + offset
      max_height = display_height
      #to create each bar on the histogram
      canvas.create_rectangle(bar_width, bar_height, max_width, max_height, fill = "#f4a259")
      #for the number text above bars
      canvas.create_text(bar_width + 1, bar_height, anchor=SW, fill="white", text=str(data[i]))
   root.update() #this was used to consistently update histogram in bubblesort function in the other file

#Function to take the input given from algMenu combobox and initiate the sorting with the algorithm.
def Sort():
   global data
   
   sort = Button(UI_frame, text = "Sort Dataset", command = Sort, state = DISABLED).grid(row = 2,column = 2,padx = 5,pady = 5)
   alg = selected_alg.get()
   i = 0

   if alg == "Bubble Sort": 
      sort = algorithms.Algorithm(data, histogram)
      sort.bubblesort()
      canvas.create_text(300,20,fill = "white",font = "Helvetica 12 bold", text = "Bubble sort works by checking one number and the number before it to see which one is bigger!")

   elif alg == "Selection Sort": 
      sort = algorithms.Algorithm(data, histogram)
      sort.selectionsort()
      canvas.create_text(300, 20, fill = "white", font = "Helvetica 12 bold", text = "Selection sort works by finding the smallest element and swapping it with the leftmost unsorted element")

   elif alg == "Insertion Sort": 
      sort = algorithms.Algorithm(data, histogram)
      sort.insertionsort()
      canvas.create_text(300, 20, fill = "white", font = "Helvetica 12 bold", text = "Insertion sort moves the first number up until the next is bigger, it then switches to the next number.")
   
   return

#For starting the programming, receiving the dataset
def Start():
   Button(UI_frame, text = "Generate Dataset", command = Generate).grid(row = 2, column = 0, padx = 5, pady = 5)

#Add on features for a dark mode and light mode functions
def night():
   Button(UI_frame, text = "Light Mode", command = light).grid(row = 2,column = 5,padx = 5,pady = 5)
   root.config(bg = "#000")
   Label(text = "Visual Sorting Algorithm - CA278 Group Project", bg = "#000", font = 'Helvetica 20 bold', foreground = "#fff").grid(row = 0, column = 0)

def light():
   Button(UI_frame, text = "Night Mode", command = night).grid(row = 2,column = 5,padx = 5,pady = 5)
   root.config(bg = "#f4d06f")
   Label(text = "Visual Sorting Algorithm - CA278 Group Project", bg = "#f4d06f", font = 'Helvetica 20 bold').grid(row = 0, column = 0)

#Add on feature to stop the program running
def Reset():
   root.destroy()

#layout in tkinter for the inputs and initiating of the visualising program
UI_frame = Frame(width = 601, height = 250, bg = "#f4a261", padx = 10, pady = 20)
UI_frame.grid(row = 5, column = 0,padx = 10, pady = 20)

#layout in tkinter for the actual visualising of the histogram. This is the box the histogram will be in
canvas = Canvas(root, width = 605, height = 200, bg = "#2F2F2F")
canvas.grid(row = 1, column = 0,padx = 5, pady = 5)
 
#Title of our project
Label(text = "Visual Sorting Algorithm - CA278 Group Project", bg = "#f4d06f", font = 'Helvetica 20 bold').grid(row = 0, column = 0, padx = 5, pady = 5)

#The user interface of the program. (Where we input the algorithms to use)
Label(UI_frame, text = "How many numbers to sort?", bg = "#f4a261").grid(row = 0, column = 0)

Button(UI_frame, text = "Generate Dataset", command = Generate).grid(row = 2, column = 0,padx = 5, pady = 5)
Button(UI_frame, text = "Night Mode", command = night).grid(row = 2, column = 5, padx = 5, pady = 5)
Button(UI_frame, text = "Stop Program", command = Reset).grid(row = 1, column = 5, padx = 5, pady = 5)

#The input for the amount of numbers to sort
size_entry = ttk.Combobox(UI_frame, textvariable = size_var, values = algorithms.values(), state = "readonly").grid(row = 1, column = 0, padx = 5, pady = 5)

root.mainloop()
