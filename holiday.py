# Calculate the user's total holiday cost

username = input("Please enter your name:")
print(f"Welcome {username}, this program will calculate your total holiday cost.")

flight_choice = (input("Please select the city that you would like to visit by typing the city's name-Rome, London or Bucharest:\n"))
num_nights = int(input("Please enter a number for how many nights are you planning to stay at the hotel:\n"))
rental_days = int(input("Please enter a number for how many days you will be hiring a car:\n"))



# Function calculates total price for the nights spent at the hotel
def hotel_cost (nights):
    return nights * 250

# Returns price per flight per destination
def plane_cost (selected_city):
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
    return days_with_car * 70

# Function calculates the total holiday cost
def holiday_cost( flight_choice, num_nights, rental_days):
    #total_cost = (hotel_cost(nights) + plane_cost(selected_city) + car_rental(days_with_car))
    return plane_cost(flight_choice) + hotel_cost(num_nights) + car_rental(rental_days)

print(f"The total holiday cost is {holiday_cost(flight_choice,num_nights,rental_days)}.\n")
print(f"Where the cost flight is {plane_cost(flight_choice)}.")
print(f"The hotel cost being {hotel_cost(num_nights)}.")
print(f"And the car rental is {car_rental(rental_days)}.")

