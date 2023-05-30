from Member import * 

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

tiers = ["A", "B", "C"]

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
    Tier: {member.getTier()}
    Points: {member.getPoints()}
    -----------------------------------
            """)
    elif option == 2:    # Add new member 
        # Prompt users for ID
        # Validation: ID length is 4, ID start with "M", ID not in db 
        memID = input("Enter member's ID: ")
        while (len(memID) != 4) or (memID.startswith("M") == False) or (memID in db):   # Loop prompt if validation fails
            if memID in db:
                print("Member ID invalid: ID already exists in database!")  
            else:
                print("Please enter a valid ID with the format M000")
            memID = input("Enter member's ID: ")      

        memName = input("Enter member's name: ")
        memEmail = input("Enter member's email: ")
        
        # Prompt users for Tier, if tier is not a valid tier, prompt again
        memTier = input("Enter member's tier [A, B, C]: ")
        while (memTier.upper() not in tiers): 
            print("Please enter a valid tier (A, B, or C)")
            memTier = input("Enter member's tier [A, B, C]: ")
        memPoints = int(input("Enter member's points: "))

        # Add new member into the db 
        new_member = Member(memID, memName, memEmail, memTier, memPoints)
        db[new_member.getId()] = new_member

    elif option == 3:    # Bubble Sort (Desc)
        bubble_list = []
        n = len(db)
        for key in db:
            bubble_list.append(db[key])
        for i in range(n-1, 0, -1):
            print(f"""
Pass: {n-i}
--------------""")
            for j in range(i):
                if bubble_list[j+1].getPoints() > bubble_list[j].getPoints():
                    tmp = bubble_list[j+1]
                    bubble_list[j+1] = bubble_list[j]
                    bubble_list[j] = tmp
            for k in bubble_list:
                print(f"ID: {k.getId()}, Points: {k.getPoints()}")
                    
        db = {}
        for i in bubble_list:
            db[i.getId()] = i
        for key in db:
            member = db[key]
            print(f"""
    -----------------------------------
    ID: {member.getId()}
    Name: {member.getName()}
    Email: {member.getEmail()}
    Tier: {member.getTier()}
    Points: {member.getPoints()}
    -----------------------------------
            """)

    elif option == 4:    # Selection Sort (Asc)
        selection_list = []
        n = len(db)
        for key in db:
            selection_list.append(db[key])
        for i in range(n-1):
            bigNdx = i
            print(f"""
Pass: {i+1}
--------------------""")
            for j in range(i+1, n):
                if selection_list[j].getTier() > selection_list[bigNdx].getTier():
                    bigNdx = j
            if bigNdx != i:
                tmp = selection_list[i]
                selection_list[i] = selection_list[bigNdx]
                selection_list[bigNdx] = tmp
            for k in selection_list:
                print(f"ID: {k.getId()}, Tier: {k.getTier()}")
            
        db = {}
        for i in selection_list:
            db[i.getId()] = i 
        for key in db:
            member = db[key]
            print(f"""
    -----------------------------------
    ID: {member.getId()}
    Name: {member.getName()}
    Email: {member.getEmail()}
    Tier: {member.getTier()}
    Points: {member.getPoints()}
    -----------------------------------
            """)
            
    elif option == 5:   # Set Test Data / Reset DB 
        db = {}
        member_list = []
        member_list = populateData()
        for i in member_list:   # Adds every member into database with ID as key and Member object as value 
            db[i.getId()] = i 
    else:
        break