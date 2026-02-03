from bookshelf.models import Book

# We ask the database to 'get' the book where the title is '1984'
found_book = Book.objects.get(title="1984")
print(found_book.author) 
# Output: George Orwell
