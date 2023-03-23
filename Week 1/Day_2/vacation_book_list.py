num_pages = int(input())
pages_per_hour = int(input())
num_days = int(input())

reading_total_books = num_pages / pages_per_hour
needed_hours = reading_total_books // num_days
print(needed_hours)
