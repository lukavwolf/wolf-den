import webbrowser

def menu(): #create menu
    print(" ")
    print("Welcome to Luka's TEST Mortal Kombat App ")
    print("-----------------------------------------")
    print(" ")
    print("1. Mortal Kombat Character Profiles")
    print("2. Mortal Kombat Videos")
    print("3. Mortal Kombat Wallpapers")
    print("4. Mortal Kombat Fatality List")
    print(" ")


    option = input("Please select from the options above: ")
    #type(option)
    print(" ")
        
    #option 1 list / figure way to accept all cases
    if option == "1":
        print(" ")
        list = ["Johnny Cage", "Kano", "Liu Kang", "Raiden", "Scorpion", "Sonya Blade", "Sub-Zero", "Goro", "Shang Tsung", "Reptile",
            "Baraka", "Jade", "Jax", "Kintaro", "Kitana", "Kung Lao", "Mileena", "Noob Saibot", "Shao Kahn", "Smoke", "Chameleon", "Cyrax",
            "Ermac", "Kabal", "Khameleon", "Motaro", "Nightwolf", "Rain", "Sektor", "Sheeva", "Sindel", "Stryker", "Fujin", "Quan Chi",
            "Sareena", "Shinnok", "Jarek", "Kai", "Meat", "Reiko", "Tanya", "Tremor", "Blaze", "Bo'Rai Cho", "Drahmin", "Frost", "Hsu Hao", 
            "Kenshi", "Li Mei", "Mavado", "Mokap", "Moloch", "Nitara", "Ashrah", "Dairou", "Darrius", "Havik", "Hotaru", "Kira", "Kobra",
            "Onaga", "Shujinko", "Daegon", "Taven", "Dark Khan", "Skarlet", "Cassie Cage", "D'Vorah", "Erron Black", "Ferra/Torr", "Jacqui Briggs", 
            "Kotal Khan", "Kung Jin", "Takeda", "Triborg", "Belokk", "Hornbuckle", "Nimbus Terrafaux", "Zebron", "Water God", "No Face", "Tasia",
            "Apep", "Gemini", "Ruutuu", "Director", "Stunt Man", "Noob/Smoke", "Cyber Sub-Zero"]
        print(list)
        print(" ")

        while True: #takes input and returns corresponding webpage
            choice = input("Which Mortal Kombat character would you like to know more about? (Press RETURN to exit to menu) ")
            type(choice)
            print(" ")
            if not choice:
                menu()
            if choice == "Johnny Cage":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Johnny_Cage')
            elif choice == "Kano":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Kano')
            elif choice == "Liu Kang":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Liu_Kang')
            elif choice == "Raiden":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Raiden')
            elif choice == "Scorpion":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Scorpion')
            elif choice == "Sonya Blade":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Sonya_Blade')
            elif choice == "Sub-Zero":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Sub_Zero')
            elif choice == "Goro":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Goro')
            elif choice == "Shang Tsung":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Shang_Tsung')
            elif choice == "Reptile":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Reptile')
            elif choice == "Baraka":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Baraka')
            elif choice == "Jade":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Jade')
            elif choice == "Jax":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Jax')
            elif choice == "Kintaro":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Kintaro')
            elif choice == "Kitana":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Kitana')
            elif choice == "Kung Lao":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Kung_Lao')
            elif choice == "Mileena":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Mileena')
            elif choice == "Noob Saibot":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Noob_Saibot')
            elif choice == "Shao Khan":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Shao_Khan')
            elif choice == "Smoke":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Smoke')
            elif choice == "Chameleon":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Chameleon')
            elif choice == "Cyrax":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Cyrax')
            elif choice == "Ermac":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Ermac')
            elif choice == "Kabal":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Kabal')
            elif choice == "Khameleon":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Khameleon')
            elif choice == "Motaro":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Motaro')
            elif choice == "Nightwolf":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Nightwolf')
            elif choice == "Rain":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Rain')
            elif choice == "Sektor":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Sektor')
            elif choice == "Sheeva":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Sheeva')
            elif choice == "Sindel":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Sindel')
            elif choice == "Stryker":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Stryker')
            elif choice == "Fujin":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Fujin')
            elif choice == "Quan Chi":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Quan Chi')
            elif choice == "Sareena":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Sareena')
            elif choice == "Shinnok":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Shinnok')
            elif choice == "Jarek":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Jarek')
            elif choice == "Kai":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Kai')
            elif choice == "Meat":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Meat')
            elif choice == "Reiko":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Reiko')
            elif choice == "Tanya":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Tanya')
            elif choice == "Tremor":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Tremor')
            elif choice == "Blaze":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Blaze')
            elif choice == "Bo'Rai Cho":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Bo_Rai_Cho')
            elif choice == "Drahmin":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Drahmin')
            elif choice == "Frost":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Frost')
            elif choice == "Hsu Hao":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Hsu_Hao')
            elif choice == "Kenshi":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Kenshi')
            elif choice == "Li Mei":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Li_Mei')
            elif choice == "Mavado":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Mavado')
            elif choice == "Mokap":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Mokap')
            elif choice == "Moloch":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Moloch')
            elif choice == "Nitara":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Nitara')
            elif choice == "Ashrah":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Ashrah')
            elif choice == "Dairou":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Dairou')
            elif choice == "Darrius":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Darrius')
            elif choice == "Havik":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Havik')
            elif choice == "Hotaru":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Hotaru')
            elif choice == "Kira":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Kira')
            elif choice == "Kobra":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Kobra')
            elif choice == "Onaga":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Onaga')
            elif choice == "Shujinko":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Shujinko')
            elif choice == "Daegon":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Daegon')
            elif choice == "Taven":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Taven')
            elif choice == "Dark Khan":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Dark_Khan')
            elif choice == "Skarlet":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Skarlet')
            elif choice == "Cassie Cage":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Cassie_Cage')
            elif choice == "D'Vorah":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/D_Vorah')
            elif choice == "Erron Black":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Erron_Black')
            elif choice == "Ferra/Torr":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Ferra_Torr')
            elif choice == "Jacqui Briggs":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Jacqui_Briggs')
            elif choice == "Kotal Kahn":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Kotal_Khan')
            elif choice == "Kung Jin":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Kung_Jin')
            elif choice == "Takeda":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Takeda')
            elif choice == "Triborg":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Triborg')
            elif choice == "Belokk":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Belokk')
            elif choice == "Hornbuckle":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Hornbuckle')
            elif choice == "Nimbus Terrafaux":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Nimbus_Terrafaux')
            elif choice == "Zebron":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Zebron')
            elif choice == "Water God":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Water_God')
            elif choice == "No Face":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/No_Face')
            elif choice == "Tasia":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Tasia')
            elif choice == "Apep":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Apep')
            elif choice == "Gemini":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Gemini')
            elif choice == "Ruutuu":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Ruutuu')
            elif choice == "Director":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Director')
            elif choice == "Stunt Man":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Stunt_Man')
            elif choice == "Noob/Smoke":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Noob_Smoke')
            elif choice == "Cyber Sub-Zero":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Kuai_Liang')
            
            else:
                print(" ")
                print("Sorry, I do not recognize that character. Please try again.")
                print(" ")

    if option == "2":
        #print("Videos Placeholder")
        list2 = ["Mortal Kombat", "Mortal Kombat 2", "Mortal Kombat 3", "Ultimate Mortal Kombat 3", "Mortal Kombat Trilogy",
        "Mortal Kombat 4", "Mortal Kombat Mythologies", "Mortal Kombat Gold", "Mortal Kombat: Special Forces",
        "Mortal Kombat: Deadly Alliance", "Mortal Kombat: Deception", 
        "Mortal Kombat: Shaolin Monks", "Mortal Kombat: Armageddon", "Mortal Kombat Unchained",
        "Mortal Kombat vs. DC Universe", "Mortal Kombat 9", "Mortal Kombat X"]
        print (list2)
        print(" ")

        while True:
            choice2 = input("Which Mortal Kombat Intro Video would you like to watch? (Press RETURN to exit to menu) ")
            type(choice2)
            print(" ")
            if not choice2:
                menu()
            if choice2 == "Mortal Kombat":
                webbrowser.open("https://www.youtube.com/watch?v=S9uoyTMMWCg")
            elif choice2 == "Mortal Kombat 2":
                webbrowser.open("https://www.youtube.com/watch?v=K09uB5XR5BU")
            elif choice2 == "Mortal Kombat 3":
                webbrowser.open("https://www.youtube.com/watch?v=TLiz4CqqGzY")
            elif choice2 == "Ultimate Mortal Kombat 3":
                webbrowser.open("https://www.youtube.com/watch?v=S9Tsuw3zfK0")
            elif choice2 == "Mortal Kombat Trilogy":
                webbrowser.open("https://www.youtube.com/watch?v=YyLU0z4KGs8")
            elif choice2 == "Mortal Kombat 4":
                webbrowser.open("https://www.youtube.com/watch?v=x6v3O54LIFs")
            elif choice2 == "Mortal Kombat Mythologies":
                webbrowser.open("https://www.youtube.com/watch?v=cjIUHanxsgw")
            elif choice2 == "Mortal Kombat Gold":
                webbrowser.open("https://www.youtube.com/watch?v=H-vc7smKSiI")
            elif choice2 == "Mortal Kombat: Special Forces":
                webbrowser.open("https://www.youtube.com/watch?v=ipIxiaS9kRY")
            elif choice2 == "Mortal Kombat: Deadly Alliance":
                webbrowser.open("https://www.youtube.com/watch?v=W7BS4S-XCHI")
            elif choice2 == "Mortal Kombat: Deception":
                webbrowser.open("https://www.youtube.com/watch?v=0jx3ldJtYC4")
            elif choice2 == "Mortal Kombat: Shaolin Monks":
                webbrowser.open("https://www.youtube.com/watch?v=amKCuzynQb8")
            elif choice2 == "Mortal Kombat: Armageddon":
                webbrowser.open("https://www.youtube.com/watch?v=yNmg66B-SSQ&t=6s")
            elif choice2 == "Mortal Kombat Unchained":
                webbrowser.open("https://www.youtube.com/watch?v=9UkV8TuP9Bk")
            elif choice2 == "Mortal Kombat vs. DC Universe":
                webbrowser.open("https://www.youtube.com/watch?v=4zE8P-e3Cr0")
            elif choice2 == "Mortal Kombat 9":
                webbrowser.open("https://www.youtube.com/watch?v=1VA3NNXG5ds")
            elif choice2 == "Mortal Kombat X":
                webbrowser.open("https://www.youtube.com/watch?v=jSi2LDkyKmI")
            else:
                print(" ")
                print("Sorry, I do not recognize that game. Please try again.")
                print(" ")
                menu()
        
                    
                

    if option == "3": #opens Google wallpaper search / will refine later
        webbrowser.open("https://www.google.com/search?q=mortal+kombat+wallpaper&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjjy9X71v3dAhWjrlQKHZxeD-8Q_AUIDigB&biw=1440&bih=839")
        print(" ")
        menu()
    
    if option == "4": #opens list / access to webpage for fatalities
        
        print(" ")
        list3 = ["Johnny Cage", "Kano", "Liu Kang", "Raiden", "Scorpion", "Sonya Blade", "Sub-Zero", "Goro", "Shang Tsung", "Reptile",
            "Baraka", "Jade", "Jax", "Kintaro", "Kitana", "Kung Lao", "Mileena", "Noob Saibot", "Shao Kahn", "Smoke", "Chameleon", "Cyrax",
            "Ermac", "Kabal", "Khameleon", "Motaro", "Nightwolf", "Rain", "Sektor", "Sheeva", "Sindel", "Stryker", "Fujin", "Quan Chi",
            "Sareena", "Shinnok", "Jarek", "Kai", "Meat", "Reiko", "Tanya", "Tremor", "Blaze", "Bo'Rai Cho", "Drahmin", "Frost", "Hsu Hao", 
            "Kenshi", "Li Mei", "Mavado", "Mokap", "Moloch", "Nitara", "Ashrah", "Dairou", "Darrius", "Havik", "Hotaru", "Kira", "Kobra",
            "Onaga", "Shujinko", "Daegon", "Taven", "Dark Khan", "Skarlet", "Cassie Cage", "D'Vorah", "Erron Black", "Ferra/Torr", "Jacqui Briggs", 
            "Kotal Khan", "Kung Jin", "Takeda", "Triborg"]
        print (list3)
        print(" ")

        while True:
            choice3 = input("Which character Fatality would you like to learn more about? (Press RETURN to exit to menu) ")
            type(choice3)
            print(" ")

            if not choice3: #filler links until fatality list created separately
                menu()
            if choice3 == "Johnny Cage":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Johnny_Cage')
            elif choice3 == "Kano":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Kano')
            elif choice3 == "Liu Kang":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Liu_Kang')
            elif choice3 == "Raiden":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Raiden')
            elif choice3 == "Scorpion":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Scorpion')
            elif choice3 == "Sonya Blade":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Sonya_Blade')
            elif choice3 == "Sub-Zero":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Sub_Zero')
            elif choice3 == "Goro":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Goro')
            elif choice3 == "Shang Tsung":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Shang_Tsung')
            elif choice3 == "Reptile":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Reptile')
            elif choice3 == "Baraka":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Baraka')
            elif choice3 == "Jade":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Jade')
            elif choice3 == "Jax":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Jax')
            elif choice3 == "Kintaro":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Kintaro')
            elif choice3 == "Kitana":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Kitana')
            elif choice3 == "Kung Lao":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Kung_Lao')
            elif choice3 == "Mileena":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Mileena')
            elif choice3 == "Noob Saibot":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Noob_Saibot')
            elif choice3 == "Shao Khan":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Shao_Khan')
            elif choice3 == "Smoke":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Smoke')
            elif choice3 == "Chameleon":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Chameleon')
            elif choice3 == "Cyrax":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Cyrax')
            elif choice3 == "Ermac":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Ermac')
            elif choice3 == "Kabal":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Kabal')
            elif choice3 == "Khameleon":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Khameleon')
            elif choice3 == "Motaro":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Motaro')
            elif choice3 == "Nightwolf":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Nightwolf')
            elif choice3 == "Rain":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Rain')
            elif choice3 == "Sektor":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Sektor')
            elif choice3 == "Sheeva":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Sheeva')
            elif choice3 == "Sindel":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Sindel')
            elif choice3 == "Stryker":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Stryker')
            elif choice3 == "Fujin":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Fujin')
            elif choice3 == "Quan Chi":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Quan Chi')
            elif choice3 == "Sareena":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Sareena')
            elif choice3 == "Shinnok":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Shinnok')
            elif choice3 == "Jarek":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Jarek')
            elif choice3 == "Kai":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Kai')
            elif choice3 == "Meat":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Meat')
            elif choice3 == "Reiko":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Reiko')
            elif choice3 == "Tanya":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Tanya')
            elif choice3 == "Tremor":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Tremor')
            elif choice3 == "Blaze":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Blaze')
            elif choice3 == "Bo'Rai Cho":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Bo_Rai_Cho')
            elif choice3 == "Drahmin":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Drahmin')
            elif choice3 == "Frost":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Frost')
            elif choice3 == "Hsu Hao":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Hsu_Hao')
            elif choice3 == "Kenshi":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Kenshi')
            elif choice3 == "Li Mei":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Li_Mei')
            elif choice3 == "Mavado":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Mavado')
            elif choice3 == "Mokap":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Mokap')
            elif choice3 == "Moloch":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Moloch')
            elif choice3 == "Nitara":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Nitara')
            elif choice3 == "Ashrah":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Ashrah')
            elif choice3 == "Dairou":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Dairou')
            elif choice3 == "Darrius":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Darrius')
            elif choice3 == "Havik":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Havik')
            elif choice3 == "Hotaru":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Hotaru')
            elif choice3 == "Kira":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Kira')
            elif choice3 == "Kobra":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Kobra')
            elif choice3 == "Onaga":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Onaga')
            elif choice3 == "Shujinko":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Shujinko')
            elif choice3 == "Daegon":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Daegon')
            elif choice3 == "Taven":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Taven')
            elif choice3 == "Dark Khan":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Dark_Khan')
            elif choice3 == "Skarlet":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Skarlet')
            elif choice3 == "Cassie Cage":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Cassie_Cage')
            elif choice3 == "D'Vorah":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/D_Vorah')
            elif choice3 == "Erron Black":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Erron_Black')
            elif choice3 == "Ferra/Torr":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Ferra_Torr')
            elif choice3 == "Jacqui Briggs":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Jacqui_Briggs')
            elif choice3 == "Kotal Kahn":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Kotal_Khan')
            elif choice3 == "Kung Jin":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Kung_Jin')
            elif choice3 == "Takeda":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Takeda')
            elif choice3 == "Triborg":
                webbrowser.open('http://mortalkombat.wikia.com/wiki/Triborg')
            
            else:
                print(" ")
                print("Sorry, I do not recognize that character. Please try again.")
                print(" ")

menu() #call menu outside of statement to return to menu after RETURN execution