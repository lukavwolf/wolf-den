import webbrowser

def menu(): #create menu

    print()
    print("Starbucks TEST App Menu Options")
    print("-------------------------------")
    print("1. Starbucks Card App")
    print("2. Inventory Management System")
    print("3. Pull-To-Thaw App")
    print("4. Time Stamp")
    print("5. Partner Schedule")
    print("6. Partner Hub")
    print("7. My Partner Info")
    print()
    print()

    option = input("Which Option Would You Like To Open?: ")

    if option == "1":
        webbrowser.open("https://app.starbucks.com")
        menu()

    if option == "2":
    #start with a lists of pastry
        pastry_names = ["Butter Croissant", "Chocolate Croissant", "Almond Croissant", "Cheese Danish", "Morning Bun", "Plain Bagel", 
                "Chonga Bagel", "Sprouted Grain Bagel", "Cinnamon Raisin Bagel", "8-Grain Roll", "Coffee Cake", "Blueberry Scone",
                "Cranberry Orange Scone", "Chocolate Chip Cookie", "Confetti Sugar Cookie", "Raccoon Cookie", "Kitchen Sink Cookie",
                "Blueberry Muffin", "Morning Muffin", "Maple Pecan Muffin", "Banana Nut Bread", "Lemon Loaf", "Pumpkin Loaf",
                "Birthday Cake Pop", "Chocolate Cake Pop", "Choclate Chip Cookie Dough Cake Pop", "Double Chocolate Chunk Brownie",
                "Old-Fashioned Glaze Doughnut", "Petite Vanilla Bean Scone", "Pumpkin Scone"]

    # now create a inventory dictionary for our list of pastry
        pastry_inv = { pastry_name:0 for pastry_name in pastry_names }


        def get_pastry():
            print()
            print("Enter Corresponding Pastry Number to Update, or Q to EXIT.")
            print("----------------------------------------------------------")
            print()
            for index, pastry_item in enumerate(pastry_inv.items()): # enumerate gives us the index of the item as well as the key itself for our loop
                print(f"{index}: {pastry_item[0]} - {pastry_item[1]}") # each "item" is a tuple that looks like (key, value)
                print()
            user_pastry_choice = input("Pastry Number: ")
            if not user_pastry_choice.isdigit(): # this checks to make sure every character is 0-9 and doesn't allow negatives
                if str.lower(user_pastry_choice) == "q":
                    print()
                    print("Thank you for updating the inventory.")
                    #return -1 # this will tell us to stop looping
                    print()
                    menu()

            user_pastry_choice_idx = int(user_pastry_choice) # convert to integer so it can be compared against other numbers
            if user_pastry_choice_idx >= len(pastry_names):
                return get_pastry() # try again if the user chose an invalid index
            return user_pastry_choice_idx

        def get_add_amount():
            amt_choice = input("How many would you like to add? ")        
            try:
                amt_choice_val = int(amt_choice)
                return amt_choice_val
            except:
                print("Sorry, only numbers accepted. Enter 0 to cancel.")
                return get_add_amount()

        # start the loop that receives user input
        while True:
            # get the pastry choice from the user
            pastry_index = get_pastry()
            if pastry_index == -1:
                break
            pastry_name = pastry_names[pastry_index]

            print()
            print("Update Inventory for","'", pastry_name, "'")
            print("----------------")
            amt_to_add = get_add_amount()
            pastry_inv[pastry_name] += amt_to_add
            print()
            print(f"{amt_to_add} eaches added!")
            print()

    if option == "3":
        print("Pull To Thaw Placeholder")
        menu()
    
    if option == "4":
        print("Time Stamp Placeholder")
        menu()

    if option == "5":
        webbrowser.open("https://mysite.starbucks.com/MySchedule/Schedule.aspx")
        menu()
    
    if option == "6":
        webbrowser.open("https://partner.starbucks.com/Pages/Home.aspx")
        menu()
    
    if option == "7":
        webbrowser.open("https://mypartnerinfo-ext.starbucks.com/partnerportal")
        menu()

menu()