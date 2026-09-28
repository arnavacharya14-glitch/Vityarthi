# INITIALIZING LISTS AND COUNTERS
L = []       
M = []       
J = []       
mm = 0       
cc = 0       
pp = 0       
i = 1

while i >= 1:
    print("---------------MENU------------------")
    print("1. Type 1 for Member Registration")
    print("2. Type 2 for Book Issue")
    print("3. Type 3 for Book Return")
    print("4. Type 4 to Add book")
    print("5. Type 5 to remove book")
    print("6. Type 6 to view books")
    print("7. Type 7 to search book")
    print("8. Type 8 to exit")
    print("-------------------------------------")
    
    l = int(input("TYPE NUMBER:"))
    
    # 1. MEMBER REGISTRATION
    if(l == 1):
        member = []
        mm = mm + 1
        for k in range(0, 3):
            if(k == 0):
                u = 1
                while u >= 1:
                    a = input("Enter Name: ")
                    t = len(a)
                    if(t == 0):
                        print("Invalid input")
                    else:
                        member.append(a)
                        break
            elif(k == 1):
                u = 1
                while u >= 1:
                    a = input("Enter Email-ID: ")
                    t = len(a)
                    if(t == 0):
                        print("Invalid Input")
                    else:
                        member.append(a)
                        break
            else:
                u = 1
                while u >= 1:
                    a = input("Enter Mobile number: ")
                    t = len(a)
                    if(t == 0):
                        print("Invalid Input")
                    else:
                        member.append(a)
                        break
        print("Assigned Member ID: ", mm)
        member.append(mm)
        L.append(member)
        print(L)
        
    # 2. BOOK ISSUE
    elif(l == 2):
        book = []
        cc = cc + 1
        for k in range(0, 5):
            if(k == 0):
                u = 1
                while u >= 1:
                    a = input("Book Name: ")
                    t = len(a)
                    if(t == 0):
                        print("Invalid Input")
                    else:
                        book.append(a)
                        break
            elif(k == 1):
                u = 1
                while u >= 1:
                    a = input("Book's Author: ")
                    t = len(a)
                    if(t == 0):
                        print("Invalid Input")
                    else:
                        book.append(a)
                        break
            elif(k == 2):
                u = 1
                while u >= 1:
                    a = input("Enter Member's Name- ")
                    t = len(a)
                    if(t == 0):
                        print("Invalid Output")
                    else:
                        book.append(a)
                        break
            elif(k == 3):
                u = 1
                while u >= 1:
                    gg = input("Enter Book ID: ")
                    t = len(gg)
                    if(t == 0):
                        print("Invalid Output")
                    else:
                        book.append(gg)
                        break
            elif(k == 4):
                u = 1
                while u >= 1:
                    yy = input("Date of issue(DDMMYYYY): ")
                    t = len(yy)
                    if(t == 0):
                        print("Invalid Input")
                    else:
                        book.append(yy)
                        break
        print("Assigned ISSUE ID: ", cc)
        book.append(cc)
        M.append(book)
        print(M)
        
    # 3. BOOK RETURN
    elif(l == 3):
        a = int(input("Enter ISSUE ID: "))
        found = 0
        for p in M:
            if(p[5] == a):
                M.remove(p)
                print("Book returned successfully")
                found = 1
                break
        if(found == 0):
            print("Issue ID not found")
        print(M)
        
    # 4. ADD BOOK TO CATALOG
    elif(l == 4):
        books = []
        pp = pp + 1
        for d in range(0, 2):
            if (d == 0):
                u = 1
                while u >= 1:
                    a = input("Enter Book name: ")
                    k = len(a)
                    if (k == 0):
                        print("INVALID OUTPUT")
                    else:
                        books.append(a)
                        break
            elif(d == 1):
                u = 1
                while u >= 1:
                    a = input("Enter Author's Name: ")
                    k = len(a)
                    if(k == 0):
                        print("Invalid output")
                    else:
                        books.append(a)
                        break
        print("Assigned book ID: ", pp)
        books.append(pp)
        J.append(books)
        print(J)
        
    # 5. REMOVE BOOK FROM CATALOG
    elif(l == 5):
        a = int(input("Enter Book ID to remove: "))
        found = 0
        for b in J:
            if(b[2] == a):
                J.remove(b)
                print("Book removed successfully")
                found = 1
                break
        if(found == 0):
            print("Book ID not found")
        print(J)
        
    # 6. VIEW ALL BOOKS
    elif(l == 6):
        print("Library Catalog")
        if len(J) == 0:
            print("No books available.")
        else:
            for b in J:
                print("Name:", b[0], "| Author:", b[1], "| Book ID:", b[2])
                
    # 7. SEARCH BOOK
    elif(l == 7):
        s = input("Enter Book Name to search: ")
        found = 0
        for b in J:
            if(s.lower() in b[0].lower()):
                print("Book Found -> Name:", b[0], "| Author:", b[1], "| Book ID:", b[2])
                found = 1
        if(found == 0):
            print("No matching books found.")
            
    # 8. EXIT
    elif(l == 8):
        print("Exiting...")
        break
        
    else:
        print("Invalid choice! Choose between 1 and 8.")
