from Member import * 
from Sort import *
from Functions import *

# Data Structure to store member details 
# Dict: {ID (PK): Member Object, ID: Member Object, ...}
db = {}

# Test data
def populateData():
    memList = []
    newMemA = Member("M002", "steve", "steve@mail.com", "C", 2000)
    memList.append(newMemA)
    newMemA = Member("M007", "strange", "strange@mail.com", "A", 6000)
    memList.append(newMemA)
    newMemA = Member("M001", "peter", "peter@mail.com", "C", 1000)
    memList.append(newMemA)
    newMemA = Member("M005", "tony", "tony@mail.com", "A", 6500)
    memList.append(newMemA)
    newMemA = Member("M004", "banner", "banner@mail.com", "B", 3500)
    memList.append(newMemA)
    newMemA = Member("M006", "clark", "clark@mail.com", "B", 5000)
    memList.append(newMemA)
    newMemA = Member("M003", "bruce", "bruce@mail.com", "B", 3000)
    memList.append(newMemA)
    print("Data populated!\n")
    return memList

# Program 
loop = True
while loop:
    print("""
    Loyalty/Membership System 
    -----------------------------------
    (1). Display all members' records 
    (2). Add a new member
    (3). Sort Members by points (DESC)
    (4): Sort Members by Tier (ASC)
    (5). Populate Data (Reset Database)
    (6). Quit
    -----------------------------------
    """)
    option = int(input("Choose an option [1, 2, 3, 4, 5, 6]: "))
    if option == 1:     # Display Members unsorted
        for i in db:
            member = db[i] 
            print(f"""
    -----------------------------------
    ID: {member.getId()}
    Name: {member.getName()}
    Email: {member.getEmail()}
    Tier: {member.getTier().upper()}
    Points: {member.getPoints()}
    -----------------------------------
            """)

    elif option == 2:    # Add new member 
        db = AddMem(db)  

    elif option == 3:    # Bubble Sort (Desc)
        db = bubbleSort(db)    # Original DB is reassigned to the sorted db that is returned by bubbleSort() func      
        # Display Sorted Member Info
        for key in db:
                member = db[key]
                print(f"""
        -----------------------------------
        ID: {member.getId()}
        Name: {member.getName()}
        Email: {member.getEmail()}
        Tier: {member.getTier().upper()}
        Points: {member.getPoints()}
        -----------------------------------
                """)
    elif option == 4:    # Selection Sort (Asc)
        db = selectionSort(db)  # Original DB is reassigned to the sorted db that is returned by bubbleSort() func      
        # Display Sorted Member Info
        for key in db:
            member = db[key]
            print(f"""
    -----------------------------------
    ID: {member.getId()}
    Name: {member.getName()}
    Email: {member.getEmail()}
    Tier: {member.getTier().upper()}
    Points: {member.getPoints()}
    -----------------------------------
            """)  
    elif option == 5:   # Set Test Data / Reset DB 
        db = {}
        member_list = populateData()
        for i in member_list:   # Adds every member into database with ID as key and Member object as value 
            db[i.getId()] = i 
    else:
        break
