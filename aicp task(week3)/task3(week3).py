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

# Function to calculate total weekly volume of milk for the herd
def calculate_total_volume(cow_yields):
    total_volume = sum(sum(yields) for yields in cow_yields.values())
    return round(total_volume)

# Function to calculate average yield per cow in a week
def calculate_average_yield(cow_yields):
    total_cows = len(cow_yields)
    total_volume = sum(sum(yields) for yields in cow_yields.values())
    average_yield = total_volume / total_cows if total_cows != 0 else 0
    return round(average_yield)

# Function to identify the most productive cow
def identify_most_productive_cow(cow_yields):
    max_yield = 0
    most_productive_cow = None
    for cow_id, yields in cow_yields.items():
        weekly_yield = sum(yields)
        if weekly_yield > max_yield:
            max_yield = weekly_yield
            most_productive_cow = cow_id
    return most_productive_cow, max_yield

# Function to identify cows with low milk yields
def identify_low_yield_cows(cow_yields):
    low_yield_cows = []
    for cow_id, yields in cow_yields.items():
        days_below_threshold = sum(1 for yield_value in yields if yield_value < MILK_THRESHOLD)
        if days_below_threshold >= MIN_DAYS_FOR_THRESHOLD:
            low_yield_cows.append(cow_id)
    return low_yield_cows

# Test the function
cow_yields = record_yield()
print("\nRecorded milk yields for the week:")
print(cow_yields)

# Calculate and display the total weekly volume of milk for the herd
total_volume = calculate_total_volume(cow_yields)
print(f"\nTotal weekly volume of milk for the herd: {total_volume} litres")

# Calculate and display the average yield per cow in a week
average_yield = calculate_average_yield(cow_yields)
print(f"Average yield per cow in a week: {average_yield} litres")

# Identify and display the most productive cow and its weekly yield
most_productive_cow, max_yield = identify_most_productive_cow(cow_yields)
print(f"\nThe most productive cow is Cow {most_productive_cow} with a weekly yield of {max_yield} litres")

# Identify and display cows with low milk yields
low_yield_cows = identify_low_yield_cows(cow_yields)
if low_yield_cows:
    print("\nCows with low milk yields (less than 12 litres for four or more days):")
    for cow_id in low_yield_cows:
        print(f"Cow {cow_id}")
else:
    print("\nNo cows have a low milk yield.")
