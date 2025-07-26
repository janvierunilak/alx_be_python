# Define the dictionary with book details
favorite_book ={"Title": "Things fall aprt", "Author": "Chinua Achebe","Genre" : " Historical fiction"
        }
book_genre=favorite_book.get('Genre')

print(f"The book <:: {favorite_book.get('Title')} ::> by ::> {favorite_book.get('Author')} <:: its Genre is >>",book_genre)

   