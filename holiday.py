# Calculate the user's total holiday cost

username = input("Please enter your name:")
print(f"Welcome {username}, this program will calculate your total holiday cost.")

flight_choice = (input("Please select the city that you would like to visit by typing the city's name-Rome, London or Bucharest:\n"))
num_nights = int(input("Please enter a number for how many nights are you planning to stay at the hotel:\n"))
rental_days = int(input("Please enter a number for how many days you will be hiring a car:\n"))



# Function calculates total price for the nights spent at the hotel
def hotel_cost (nights):
    '''
    Calculates the total cost spent at the hotel
    Parameter:
        nights =  nights spent at the hotels
    Returns:
        total cost
    '''

    return nights * 250

# Returns price per flight per destination
def plane_cost (selected_city):
    '''
    Calculates the price per flight
    Parameter:
        selected_city = destination
    Returns:
        the flight cost
    '''

    if selected_city == "Rome":
        return 100
    if selected_city == "London":
        return 300
    if selected_city == "Bucharest":
        return 50
    else:
        print("The option you have entered is invalid:")

# Function calculates total price for the car rental
def car_rental (days_with_car):
    '''
    Calculates the cost for the car rental
    Parameter:
        days_with_car = total days chosen to rent a car
    Returns:
       total car rental cost
    '''

    return days_with_car * 70

# Function calculates the total holiday cost
def holiday_cost( flight_choice, num_nights, rental_days):
    '''
    Calculates total holiday cost
    Parameters:
        flight_choice, num_night, rental_days = destinations, number of nights, days with car rental
    Returns:
        total holiday cost
    '''
    return plane_cost(flight_choice) + hotel_cost(num_nights) + car_rental(rental_days)

print(f"The total holiday cost is {holiday_cost(flight_choice,num_nights,rental_days)}.\n")
print(f"Where the cost flight is {plane_cost(flight_choice)}.")
print(f"The hotel cost being {hotel_cost(num_nights)}.")
print(f"And the car rental is {car_rental(rental_days)}.")

