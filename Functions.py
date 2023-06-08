from Member import *

def AddMem(db):
    tiers = ["A", "B", "C"]
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