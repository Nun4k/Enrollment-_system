
reg = {"justine aban": ["1111"], "rogem mark perez": ["1112"], "rona gemm perez": ["1113"], "john smith": ["1114"]}

price = 0
cont = True
try:
    # Name and roll no. input for verification process
    while cont:
        Name = input("Enter name: ")
        name = Name.lower()
        if name not in reg:
            print("No match found.")
        else:
            roll = input("Enter your roll no.: ")
            roll_num = reg[name]
            num = roll_num[0]
            if roll != num:
                print("Verification failed!")
            # Subject input program
            else:
                print(
                    'Choose Subject from the following list.\n 1 PE 01 = 2 UNITS\n 2 CC 101 = 3 UNITS\n 3 CSE 01 = 3 '
                    'UNITS\n 4 CC 102 = 3 UNITS\n 5 GE 01 = 3 UNITS\n 6 NSTP 01 = 2 UNITS\n \n To Choose subject '
                    'enter the name of subject\n 1000 pesos per unit of subject.')
                # def of list, var and dict
                subject_time = []
                enrolled_subject = []
                hour_sched = []
                day_list = {}
                PE_01 = 2  # units
                CC_101 = 3
                CC_102 = 3
                CSE_01 = 3
                GE_01 = 3
                NSTP_01 = 2
                unit_price = 1000
                total_unit = 0
                unit_dict = {"pe 01": 2, "cc 101": 3, "cse 01": 3, "cc 102": 3, "ge 01": 3, "nstp 01": 2}
                add = True
                # Loop for subject and schedule input
                while add:
                    sub = input("\nEnter subject name: ")
                    # Check if user input subject is valid or not
                    if sub.lower() not in ["pe 01", "cc 101", "cse 01", "cc 102", "ge 01", "nstp 01"]:
                        print("Invalid subject name!\n")
                    # Check if user input(subject) has already been entered
                    #elif sub.lower() in enrolled_subject:
                        #print("You already have this subject.")
                    else:
                        # Appending user input to subject list
                        if sub.lower() not in enrolled_subject:
                            enrolled_subject.append(sub.lower())
                        week_day = True
                        # Loop for schedule (weekday and hour/minute) input
                        while week_day:
                            day = input(
                                "Enter which day you want to add your subject\n M  for Monday\n T  for Tuesday\n W  "
                                "for Wednesday\n Th for Thursday\n F  for Friday\n S  for Saturday\n \n Enter Here: ")
                            # check if user input of day is valid or not
                            if day.lower() not in ["m", "t", "w", "th", "f", "s"]:
                                print("\nInvalid input! Please enter the correct letter.\n")
                                week_day = True
                            else:
                                # Program for adding day(as key) in dictionary
                                if day.lower() not in day_list.keys():
                                    day_list.update({day.lower(): []})
                                hour_check = True
                                # Loop for hour input
                                while hour_check:
                                    # Check if user input of hour is valid or not
                                    hour = int(input("Enter the hour only in (24 hour format): "))
                                    if hour > 23 or hour < 0:
                                        print("Invalid hour, enter again: ")
                                        hour_check = True
                                    # Check if user input of hour is already taken for another subject
                                    elif hour in day_list.get(day.lower()):
                                        print("You already have a another subject on that time")
                                        hour_check = True
                                    # check if user input of hours is less than 10 if it is less than 10 then its
                                    # gonna add zero to it (for ex:- 2 = 02)
                                    elif hour < 10:
                                        hr = f"{hour:02d}"
                                        h_r = int(hr) + 1
                                        hrr = f"{h_r:02d}"
                                        # Updating the value(inputted hour) in dictionary(day_list)
                                        value_list = day_list.get(day.lower())
                                        value_list.append(hour)
                                        a_value_list = value_list
                                        day_list[day.lower()] = a_value_list
                                        hour_check = False
                                    # Program for user input hours if it's more than 10
                                    else:
                                        hr = hour
                                        hrr = hour + 1
                                        # updating values(as inputted hour) in dictionary(w_lst)
                                        value_list = day_list.get(day.lower())
                                        value_list.append(hour)
                                        a_value_list = value_list
                                        day_list[day.lower()] = a_value_list
                                        hour_check = False
                                minute_check = True
                                # Loop for minute input
                                while minute_check:
                                    minute = int(input("Enter the minute in (00,15,30,45): "))
                                    # Check if user input minutes is valid or not
                                    if minute not in [0, 15, 30, 45]:
                                        print("Please Enter the minutes in (00,15,30,45): ")
                                        minute_check = True
                                    # Program for saving/changing minutes value
                                    elif minute == 0:
                                        mi = "00"
                                        minute_check = False
                                    else:
                                        mi = minute
                                        minute_check = False

                                # creating dictionary that can store (m,t,w) as key and (complete words) as value
                                a_day_dict = {"m": "Monday", "t": "Tuesday", "w": "Wednesday", "th": "Thursday",
                                              "f": "Friday", "s": "Saturday"}
                                a_day = a_day_dict[day.lower()]
                                week_day = False
                        # Program that can combine whole details on one line for display
                        full = (sub.upper() + ' ' + '(' + str(hr) + ':' + str(mi) + " to " + str(
                            hrr) + ':' + str(mi) + ' on ' + a_day + ')')
                        subject_time.append(full)
                        choice = input('Do you want to add more subject? Y/N :  ')
                        if choice == "y" or choice == "Y":
                            print(
                                ' 1 PE 01 = 2 UNITS\n 2 CC 101 = 3 UNITS\n 3 CSE 01 = 3 UNITS\n 4 CC 102 = 3 UNITS\n 5 '
                                'GE 01 = 3 UNITS\n 6 NSTP 01 = 2 UNITS\n')
                            add = True
                        else:
                            print("\nYou are now enrolled!\n")
                            add = False
                            # Program for unit cost calculation
                            for s in range(0, len(enrolled_subject)):
                                subject_name = enrolled_subject[s]
                                num_of_unit = unit_dict.get(subject_name)
                                total_unit += num_of_unit
                            # program for display all details
                            print("Your name: ", name.title(), "\nYour roll. No. ", roll)
                            print("\nYour Enrolled subject and schedule: ")
                            # program for displaying each subject in each new line
                            for i in range(0, len(subject_time)):
                                print(subject_time[i])
                            price = total_unit * unit_price
                            print("\nTotal price you have to pay is: ", price, 'pesos')


# Program for displaying if any error occurs
except Exception as e:
    print("Error:-\n", e)
