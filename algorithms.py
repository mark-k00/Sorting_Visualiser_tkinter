#!/usr/bin/env python
import random
import time

#to get the range of values for the combobox sizeEntry
def values():
   values = []
   
   for i in range(1,41):
      values.append(i)
   return values

#to generate the random list comprised of an amount 'n' given by the user in sizeEntry combobox
def numbers(size_entry):
   global random_list
   
   how_many = int(size_entry)
   random_list = []
   
   for i in range(0, how_many):
      n = random.randint(0,100) #We found out how to use randint from stack overflow: https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9
      random_list.append(n)
   return random_list

class Algorithm:
   def __init__(self, data):#, histogram):
      self.data = data
      self.histogram = histogram #to test this class in terminal, comment this and histogram above^

   #Bubblesort Algorithm visualised in histogram
   #We studied this algorithm in first year
   def bubblesort(self):
      i = 0
   
      while i < len(self.data): #while 0 is less than the length of the list random_list
         j = 1 #the position just above position random_list[0]
         while j < len(self.data): #1<length of list so that the while loop is not infinite
            if self.data[j] < self.data[j - 1]: #random_list[1]<a[0] for example position random_list[1]= 6 and random_list[0]=8 therefore random_list[1] is less than random_list[0] and while loop will run
               tmp = self.data[j] #temporary variable set as integer from position random_list[1]
               self.data[j] = self.data[j - 1] #integer from position random_list[1] is replaced with integer from position random_list[0] (which must be a higher number in an earlier place) so that it can be sorted in order of rising numbers
               self.data[j - 1] = tmp #now random_list[0] is given the temporary variable so that there positions are officially swapped and the smaller number should be at an earlier position
    #           self.histogram(self.data)
               print self.data
               time.sleep(0.2)
            j = j + 1 #j turns into 2 so that we can go through the full list
         i = i + 1 #i turns into 1 for same reason as above

   #Selection sort Algorithm visualised in histogram
   #We studied this algorithm in first year
   def selectionsort(self):
      i = 0
   
      while i < len(self.data):
         p = i
         j = i
         while j < len(self.data):
            if self.data[j] < self.data[p]: #if j position is smaller then move up number
               p = j 
            j = j + 1
         tmp = self.data[i]
         self.histogram(self.data)
#         print self.data
         time.sleep(0.2)
         self.data[i] = self.data[p]
         self.data[p] = tmp
         i = i + 1


   #Insertion sort Algorithm visualised in histogram
   #Using research we managed to understand this algorithm and work together to write it up
   #https://www.geeksforgeeks.org/insertion-sort/
   def insertionsort(self):
       i = 0
       while i < len(self.data):
           a = self.data[i] #a is equal to the number at data[i] going up the list
           #Now we move numbers ahead if they are greater than a
           j = i - 1 #j is the number that will be before a
           while j >= 0 and a < self.data[j]: #j cant be -1. Number at space j cant be smaller than number at a
                   self.data[j + 1] = self.data[j] #if number at j is bigger than a then move up
                   j = j - 1 #stop while loop because position j will be smaller number than at a
           self.data[j + 1] = a
           self.histogram(self.data)
#           print self.data
           time.sleep(0.2)
           i = i + 1

#Used to test this file on the terminal, to make sure the algorithms were properly working.
if __name__ == '__main__':
   a = [5,2,8,3,4]
   alg = Algorithm(a)
   #print alg.bubblesort()
   #print alg.selectionsort()
   print alg.bubblesort()
