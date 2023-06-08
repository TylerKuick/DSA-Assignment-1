# Bubble Sort

def bubbleSort(db):
    bubble_list = []    # Empty List for sorting 
    for key in db:
        bubble_list.append(db[key])     # Add all member objects into the bubble sorting list 
    n = len(bubble_list)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if bubble_list[j+1].getPoints() > bubble_list[j].getPoints():   # When second member has more points than first member
                # Three point switching
                tmp = bubble_list[j+1]  # Second member is put into a temporary holder
                bubble_list[j+1] = bubble_list[j]   # First member is assigned to Second Member's position
                bubble_list[j] = tmp    # Second member is assigned to First Member's position
        # Print Pass Items
        print(f"""
Pass: {n-i}
---------------------------------""")
        for k in bubble_list:   
            print(f"ID: {k.getId()}, Points: {k.getPoints()}")
    
    db = {}     # Reset the db into a empty dictionary
    for i in bubble_list:   
        db[i.getId()] = i   # Set ID as Key and Member object as Value

    # Display Sorted Member Info
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

    return db   # Sorted db
                        


# Selection Sort

def selectionSort(db):
    selection_list = []     # Empty List for sorting 
    for key in db:
        selection_list.append(db[key])      # Add all member objects into the selection sorting list 
    n = len(db) 
    for i in range(n-1):
        smallNdx = i    # Assign the current pass as the smallest index 
        for j in range(i+1, n):
            if selection_list[j].getTier() < selection_list[smallNdx].getTier():
                smallNdx = j
        if smallNdx != i:
            tmp = selection_list[i]
            selection_list[i] = selection_list[smallNdx]
            selection_list[smallNdx] = tmp
        # Print Pass Items
        print(f"""
Pass: {i+1}
---------------------------------""")
        for k in selection_list:
            print(f"ID: {k.getId()}, Tier: {k.getTier()}")
                
    db = {}     # Reset the db into a empty dictionary
    for i in selection_list:
        db[i.getId()] = i      # Set ID as Key and Member object as Value

    # Display Sorted Member Info
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

    return db