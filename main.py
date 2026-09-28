L = []
M = []
J = []
mm = 0
cc = 0
pp = 0
i = 1

while i >= 1:
print("Type 1 for Member register")
print("Type 2 for Book Issue")
print("Type 3 for Book Return")
print("Type 4 to Add book")
print("Type 5 to remove book")
print("Type 6 to search book")
print("Type 7 to exit")

l = int(input("enter the type:"))

if(l == 1):
member = []
mm = mm + 1
a = input("enter your name: ")
b= input("enter E-mail id: ")
c= int(input("enter phone no.: "))
L.append(a)
L.append(b)
L.append(c)
print("assigned member ID: ", mm)
member.append(mm)
L.append(member)
print(L)

elif(l == 2):
issued_book = []
cc = cc + 1
for k in range(0, 5):
if(k == 0):
a = input("book Name: ")
issued_book.append(a)
elif(k == 1):
a = input("author name: ")
issued_book.append(a)
elif(k == 3):
gg = input("book id: ")
t = len(gg)
issued_book.append(gg)
elif(k == 2):
a = input("Member Name: ")
issued_book.append(a)
elif(k == 4):
yy = input("issue date: ")
issued_book.append(yy)
print("assigned issue ID: ", cc)
issued_book.append(cc)
M.append(issued_book)
print(M)

elif(l == 3):
a = int(input("issue id: "))
ff = 0
for p in M:
if(p[5] == a):
M.remove(p)
print("Book returned")
ff = 1
break
if(ff == 0):
print("ID not found")
print(M)

elif(l == 4):
all_kitaab = []
pp = pp + 1
for d in range(0, 2):
if (d == 0):
a = input("Enter Book name: ")
all_kitaab.append(a)
elif(d == 1):
a = input("Author Name: ")
all_kitaab.append(a)
print("assigned book ID: ", pp)
all_kitaab.append(pp)
J.append(all_kitaab)
print(J)

elif(l == 5):
a = int(input("Book ID: "))
exist = 0
for b in J:
if(b[2] == a):
J.remove(b)
print("book is removed")
found = 1
break
if(exist == 0):
print("book does not exist")
print(J)

elif(l == 6):
s = input("Book Name: ")
fou_nd = 0
for b in J:
if(s.lower() in b[0].lower()):
print("Name:", b[0], "| Author:", b[1], "| Book ID:", b[2])
found = 1
if(fou_nd == 0):
print("No books found.")

elif(l == 7):
print("exit")
break
else:
print("Invalid ")
