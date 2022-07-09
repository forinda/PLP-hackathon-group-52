"""
Personality test program - Task One (Day 2)
Book Club Points Serendipity Booksellers has a book club that awards points to its
customers based on the number of books purchased each month. The points are awarded
as follows:
• If a customer purchases 0 books, he or she earns 0 points.
• If a customer purchases 1 book, he or she earns 6 points.
• If a customer purchases 2 books, he or she earns 16 points.
• If a customer purchases 3 books, he or she earns 32 points.
• If a customer purchases 4 or more books, he or she earns 60 points.
Write a program that asks the user to enter the number of books that he or she has
purchased this month and displays the number of points awarded
"""
books_purchased = int(input("Enter the number of books purchased: "))
if(books_purchased<=0):
  points = 0
elif(books_purchased==1):
  points = 6
elif(books_purchased==2):
  points = 16
elif(books_purchased==3):
  points = 32
else:
  points = 60
print("points awarded: ",points)