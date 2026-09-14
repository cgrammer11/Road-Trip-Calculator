# This segment asks the questions needed for the calcuations
final_destination = input("What was your final destination?: ")
start_odometer = int(input("What was the starting odometer?: "))
end_odometer = int(input("What was the ending odometer?: "))
total_gallons = float(input("How many gallons of gas were used? "))
total_days = float(input("How many days did the trip take?: "))

print("__--__--__--__--__--__--__--")
print("ROAD TRIP SUMMARY: " + final_destination)
print("__--__--__--__--__--__--__--")

# this segment calculates and gives a summary of the road trip
total_distance = end_odometer - start_odometer
print("TOTAL DISTANCE: " + str(total_distance) + " miles")
gas_efficency = total_distance / total_gallons
print("GAS EFFICENCY: " + str(gas_efficency) + " MPG")
average_pace = total_distance / total_days
print("AVERAGE PACE: " + str(average_pace) + " miles per day")

print("        _______")
print("       //  || \\\\ ")
print(" _____//___||___\\\\____")
print(" )  _          _    \\ ")
print(" |_/ \\________/ \\___|")
print("   \\_/        \\_/")
print("  " + final_destination + " or bust!  ")
