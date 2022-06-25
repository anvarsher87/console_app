
import utils as ut

#---------------------------menu look------------------------------------
UserChoices_1 = '''
Enter:  - 1 to check room #1
        - 2 to check room #2
        - 3 to check room #3
        - 4 to check room #4
        - 5 to check room #5
 Which room do you want to check?:
'''
UserChoices_2 = '''
Enter: - date: Year-Month-Day:  ....-..-..
       For which date do you want to book?
'''

UserChoices_3 = '''
Enter: - time slots  (1ts = 9:00-11:00;  2ts = 11:00-13:00; 
                      3ts = 14:00-16:00; 4ts = 16:00-18:00)
 For which time slot do you want to book?
'''
#---------------------------Booking------------------------------------

def menu():
    
    print("------------------------------------------------------------")
    print("-------Welcome to the room booking console app!-------------")
    print("------------------------------------------------------------")
    
    User_need = input("What do you want to do (check/book/quit)?:" )
    while User_need != 'quit':

      if User_need == 'check':

        user_input_1 = input(UserChoices_1)
        while ut.room_validator(user_input_1) != 1:
          print("Please type correctly")
          user_input_1 = input(UserChoices_1)
          
        user_input_2 = input(UserChoices_2)
        while ut.time_validator(user_input_2) != 1:
          print("Please enter valid date")
          user_input_2 = input(UserChoices_2)

        user_input_3 = input(UserChoices_3)
        while ut.time_slots_validator(user_input_3) != 1:
          print("Please enter correct slot")
          user_input_1 = input(UserChoices_3)

        print("Wait, checking the avilability of the room ... ")
        ut.wait()

        if ut.checking(user_input_1, user_input_2, user_input_3) == True:
          print('The room you have chosen is available for booking!')
        else:
          print('The room you chose for the date and time is already booked')

        # (1, '2022-10-26', '1ts', 1, 'anvar.sher.2', 'anvarsher2@gamil.com')
      elif User_need == 'book':

        UserName  = input("Please enter your user name: ")
        while ut.UserNameValidator(UserName) != 1:
          print("Please enter valid username")
          UserName = input("Please enter your user name: ")
          
        UserEmail = input("Please enter your email: ")
        while ut.UserEmailValidator(UserEmail) !=1:
          print(("Please enter valid Email"))
          UserEmail = input("Please enter your email: ")
        

        user_input_1 = input(UserChoices_1)
        while ut.room_validator(user_input_1) != 1:
          print("Please type correctly")
          user_input_1 = input(UserChoices_1)

        user_input_2 = input(UserChoices_2)
        while ut.time_validator(user_input_2) != 1:
          print("Please enter valid date")
          user_input_2 = input(UserChoices_2)

        user_input_3 = input(UserChoices_3)
        while ut.time_slots_validator(user_input_3) != 1:
          print("Please enter correct slot")
          user_input_3 = input(UserChoices_3)

        print("Wait, checking the avilability of the room ... ")
        ut.wait()
        #(1, '2022-10-26', '1ts', 1, 'anvar.sher.2', 'anvarsher2@gamil.com')

        if ut.checking(user_input_1, user_input_2, user_input_3) == True:
          
          print('The room you have chosen is available for booking!, You are good to go')
          
          new_row_db = [user_input_1, user_input_2, user_input_3, 1, UserName, UserEmail]
          
          ut.insert_into_table(user_input_1, user_input_2, user_input_3, 1, UserName, UserEmail)

          ut.mailto(new_row_db)
        else:
          print('The room you chose for the date and time is already booked. Do you want to quit? or Try again' )

      else:
        print("Please type correctly: check or book or quit")
      User_need = input("What do you want to do (check/book/quit)?:"   )

menu()


