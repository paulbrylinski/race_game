import random

car_dictionary = {
    "2021 Mustang GT":
    {
        "zero_sixty": 4.2,
        "quarter_mile": 12.2
    },
    "2021 Camaro SS":
    {
        "zero_sixty": 4.0,
        "quarter_mile": 12.2
    },
    "2021 Honda Civic Type R":
    {
        "zero_sixty": 5.0,
        "quarter_mile": 12.7
    },
    "2021 Subaru WRX STI":
    {
        "zero_sixty": 4.4,
        "quarter_mile": 13.2
    },
    "2021 Dodge Challanger R/T":
    {
        "zero_sixty": 4.8,
        "quarter_mile": 13.2
    }
}
car_list = list(car_dictionary.keys())


while True:
    print("Choose the NUMBER of the Car To Race Against The Computer")
    print("1.", car_list[0])
    print("2.", car_list[1])
    print("3.", car_list[2])
    print("4.", car_list[3])
    print("5.", car_list[4])
    car_choice = input("What Number Car Do You Choose?: ")
    if car_choice == "1":
        print("You Choose:", car_list[0])
        user_car = car_list[0]
        user_zero_sixty = car_dictionary['2021 Mustang GT']['zero_sixty']
        user_quarter_mile = car_dictionary['2021 Mustang GT']['quarter_mile']
        break
    elif car_choice == "2":
        print("You Choose:", car_list[1])
        user_car = car_list[1]
        user_zero_sixty = car_dictionary['2021 Camaro SS']['zero_sixty']
        user_quarter_mile = car_dictionary['2021 Camaro SS']['quarter_mile']
        break
    elif car_choice == "3":
        print("You Choose:", car_list[2])
        user_car = car_list[2]
        user_zero_sixty = car_dictionary['2021 Honda Civic Type R']['zero_sixty']
        user_quarter_mile = car_dictionary['2021 Honda Civic Type R']['quarter_mile']
        break
    elif car_choice == "4":
        print("You Choose:", car_list[3])
        user_car = car_list[3]
        user_zero_sixty = car_dictionary['2021 Subaru WRX STI']['zero_sixty']
        user_quarter_mile = car_dictionary['2021 Subaru WRX STI']['quarter_mile']
        break
    elif car_choice == "5":
        print("You Choose:", car_list[4])
        user_car = car_list[4]
        user_zero_sixty = car_dictionary['2021 Dodge Challanger R/T']['zero_sixty']
        user_quarter_mile = car_dictionary['2021 Dodge Challanger R/T']['quarter_mile']
        break
    else:
        print("Incorrect Input, Choose Again\n")

computer_choice = random.choice(car_list)
print("\nThe Computer Chooses:", computer_choice, "\n")
if computer_choice == car_list[0]:
    cpu_car = car_list[0]
    cpu_zero_sixty = car_dictionary['2021 Mustang GT']['zero_sixty']
    cpu_quarter_mile = car_dictionary['2021 Mustang GT']['quarter_mile']
elif computer_choice == car_list[1]:
    cpu_car = car_list[1]
    cpu_zero_sixty = car_dictionary['2021 Camaro SS']['zero_sixty']
    cpu_quarter_mile = car_dictionary['2021 Camaro SS']['quarter_mile']
elif computer_choice == car_list[2]:
    cpu_car = car_list[2]
    cpu_zero_sixty = car_dictionary['2021 Honda Civic Type R']['zero_sixty']
    cpu_quarter_mile = car_dictionary['2021 Honda Civic Type R']['quarter_mile']
elif computer_choice == car_list[3]:
    cpu_car = car_list[3]
    cpu_zero_sixty = car_dictionary['2021 Subaru WRX STI']['zero_sixty']
    cpu_quarter_mile = car_dictionary['2021 Subaru WRX STI']['quarter_mile']
elif computer_choice == car_list[4]:
    cpu_car = car_list[4]
    cpu_zero_sixty = car_dictionary['2021 Dodge Challanger R/T']['zero_sixty']
    cpu_quarter_mile = car_dictionary['2021 Dodge Challanger R/T']['quarter_mile']


def zero_sixty():
    print("Your", user_car, "Goes 0-60mph in", user_zero_sixty, "seconds!")
    print("The Computer's", cpu_car, "Goes 0-60mph in",
          cpu_zero_sixty, "seconds!\n")
    if cpu_zero_sixty < user_zero_sixty:
        print("You Lose!")
    elif cpu_zero_sixty == user_zero_sixty:
        print("It's a tie!")
    else:
        print("You Win!")


def quarter_mile():
    print("Your", user_car, "Goes a Quarter Mile in",
          user_quarter_mile, "seconds!")
    print("The Computer's", cpu_car, "Goes a Quarter Mile in",
          cpu_quarter_mile, "seconds!\n")
    if cpu_quarter_mile < user_quarter_mile:
        print("You Lose!")
    elif cpu_quarter_mile == user_quarter_mile:
        print("It's a tie!")
    else:
        print("You Win!")


def race_selection():
    while True:
        print("1. Race in 0-60 Seconds")
        print("2. Race a Quarter Mile")
        race = input("Choose the number of your race!: ")
        if race == "1":
            print("You selected 0-60 Seconds\n")
            zero_sixty()
            break
        elif race == "2":
            print("You selected a Quarter Mile\n")
            quarter_mile()
            break
        else:
            print("Incorrect key, Choose 1 or 2\n")


print(user_car, "vs", cpu_car)
print("\nRace Options:")
race_selection()
