# Find Days-Hours-Minutes-Seconnds 

def convert_minutes(total_minutes):
    days = total_minutes // (24 * 60)
    hours = (total_minutes % (24 * 60)) // 60
    minutes = total_minutes % 60
    seconds = 0  # Since the input is in minutes, seconds will always be 0

    return days, hours, minutes, seconds

# Example usage
total_minutes = int(input("Enter the total minutes: "))
days, hours, minutes, seconds = convert_minutes(total_minutes)

print(f"{total_minutes} minutes is equal to {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")


# another way 

def convert_minutes(minutes):
    days = minutes // (24 * 60)
    remaining_minutes = minutes % (24 * 60)
    hours = remaining_minutes // 60
    remaining_minutes %= 60
    seconds = remaining_minutes * 60

    return days, hours, remaining_minutes, seconds

# Example usage
input_minutes = int(input("Enter the number of minutes: "))
days, hours, mins, secs = convert_minutes(input_minutes)

print(f"{input_minutes} minutes is equivalent to {days} days, {hours} hours, {mins} minutes, and {secs} seconds.")