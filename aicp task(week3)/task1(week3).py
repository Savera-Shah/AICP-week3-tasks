# Define constants
DAYS_IN_WEEK = 7
MILK_THRESHOLD = 12
MIN_DAYS_FOR_THRESHOLD = 4

# Function to record milk yield for each cow
def record_yield():
    # Dictionary to store milk yields for each cow
    cow_yields = {}
    
    # Prompt for entering data for each day of the week
    for day in range(1, DAYS_IN_WEEK + 1):
        print(f"Day {day}:")
        # Prompt for entering yield for each cow
        for cow_id in range(100, 110):
            yield_input = input(f"Enter milk yield for cow {cow_id} on day {day} (litres): ")
            # Check if input is valid (a float)
            try:
                yield_value = float(yield_input)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue
                
            # Check if cow_id exists in dictionary, if not, create an empty list
            if cow_id not in cow_yields:
                cow_yields[cow_id] = []
                
            # Append yield to the list of yields for the cow
            cow_yields[cow_id].append(yield_value)
    
    return cow_yields

# Function to write milk yields to a file
def write_to_file(cow_yields):
    with open("milk_yields.txt", "w") as file:
        for cow_id, yields in cow_yields.items():
            file.write(f"Cow {cow_id}: {', '.join(map(str, yields))}\n")

# Test the function
cow_yields = record_yield()
print("\nRecorded milk yields for the week:")
print(cow_yields)

# Write the milk yields to a file
write_to_file(cow_yields)
print("Milk yields have been written to milk_yields.txt")
