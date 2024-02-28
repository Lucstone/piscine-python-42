from datetime import datetime

current_date = datetime.now()

# Get time in seconds
sec_since_epoch = (current_date - datetime(1970, 1, 1)).total_seconds()

# Format the month as a three-letter abbreviation
formatted_month = current_date.strftime("%b")

# Use {:,} to include commas every three digits
formatted_seconds = '{:,}'.format(sec_since_epoch)

#sec_since_epoch:.2e get time in scientifique writing
print(f"Seconds since January 1, 1970: {formatted_seconds} or {sec_since_epoch:.2e} in scientific notation")
print(f"{formatted_month} {current_date.day} {current_date.year}")