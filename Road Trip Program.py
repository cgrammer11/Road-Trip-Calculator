# This segment asks the questions needed for the calcuations
final_destination = input("What was your final destination?: ")
start_odometer = int(input("What was the starting odometer?: "))
end_odometer = int(input("What was the ending odometer?: "))
total_gallons = float(input("How many gallons of gas were used? "))
total_days = float(input("How many days did the trip take?: "))

print("                            ")
print("__--__--__--__--__--__--__--")
print("ROAD TRIP SUMMARY: " + final_destination)
print("__--__--__--__--__--__--__--")
print("                            ")

# this segment calculates and gives a summary of the road trip
compute_total_distance = end_odometer - start_odometer
print("TOTAL DISTANCE: " + str(total_distance) + " miles")
compute_gas_efficiency = total_distance / total_gallons
print("GAS EFFICIENCY: " + str(gas_efficiency) + " MPG")
compute_mpg = total_distance / total_days
print("AVERAGE PACE: " + str(average_pace) + " miles per day")

print("        _______")
print("       //  || \\\\ ")
print(" _____//___||___\\\\____")
print(" )  _          _    \\ ")
print(" |_/ \\________/ \\___|")
print("   \\_/        \\_/")
print("  " + final_destination + " or bust!  ")
