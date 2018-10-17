import webbrowser

def menu():

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
    
        pastry_names = ["Butter Croissant", "Chocolate Croissant", "Almond Croissant", "Cheese Danish", "Morning Bun", "Plain Bagel", 
                "Chonga Bagel", "Sprouted Grain Bagel", "Cinnamon Raisin Bagel", "8-Grain Roll", "Coffee Cake", "Blueberry Scone",
                "Cranberry Orange Scone", "Chocolate Chip Cookie", "Confetti Sugar Cookie", "Raccoon Cookie", "Kitchen Sink Cookie",
                "Blueberry Muffin", "Morning Muffin", "Maple Pecan Muffin", "Banana Nut Bread", "Lemon Loaf", "Pumpkin Loaf",
                "Birthday Cake Pop", "Chocolate Cake Pop", "Choclate Chip Cookie Dough Cake Pop", "Double Chocolate Chunk Brownie",
                "Old-Fashioned Glaze Doughnut", "Petite Vanilla Bean Scone", "Pumpkin Scone"]

   
        pastry_inv = { pastry_name:0 for pastry_name in pastry_names }


        def get_pastry():
            print()
            print("Enter Corresponding Pastry Number to Update, or Q to EXIT.")
            print("----------------------------------------------------------")
            print()
            for index, pastry_item in enumerate(pastry_inv.items()):
                print(f"{index}: {pastry_item[0]} - {pastry_item[1]}")
                print()
            user_pastry_choice = input("Pastry Number: ")
            if not user_pastry_choice.isdigit():
                if str.lower(user_pastry_choice) == "q":
                    print()
                    print("Thank you for updating the inventory.")
                    print()
                    menu()

            user_pastry_choice_idx = int(user_pastry_choice) 
            if user_pastry_choice_idx >= len(pastry_names):
                return get_pastry()
            return user_pastry_choice_idx

        def get_add_amount():
            amt_choice = input("How many would you like to add? ")        
            try:
                amt_choice_val = int(amt_choice)
                return amt_choice_val
            except:
                print("Sorry, only numbers accepted. Enter 0 to cancel.")
                return get_add_amount()

       
        while True:
           
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