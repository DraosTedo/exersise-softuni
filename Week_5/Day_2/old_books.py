favorite_book = input()
current_book = input()

books_checked = 0
if_books_found = False

while current_book != "No More Books":
    if current_book == favorite_book:
        if_books_found = True
        print(f"You checked {books_checked} books and found it.")
        break

    books_checked += 1
    current_book = input()

if not if_books_found:
    print("The book you search is not here!")
    print(f"You checked {books_checked} books.")
