#program used to collect user input so as to help with user needs in an online bookstore
try:#error handelling
    print('thankyou for contacting droid bookstore '.upper())
    name,gender=input('lets know your NAME, please: '),input('and gender: ')# prompting a user input
    if gender.lower()=='male':
        print(f'\n hello {name}\n i am Pinklosa your assistant today\n how can i help \n ')#personalised message greeting
    else:
        print(f'\n hello {name}\n i am Gerald your assistant today\n how can i help  ')#personalised message greeting
    help_service=input('let us know:')
    print('\n for specifics knowing your age could help us')
    age=int(input('AGE please: '))#the age variable declaration by programer and assigning to be done bu user
    current_year=2024 # initialisation of current year
    birth_year=current_year-age #birth year calculation
    print('so you were born in',birth_year,'interesting')# out putting the birth year
    if birth_year<=2000:
        print('i have quite a number of suggestions i hope you find something from this list')
    else:
        print('i have quite a number of suggestions to interest a young mind')
    print('\n btw i have something else to ask of you \n but trust me this could help')
    number=int(input('\nENTER YOUR FAVOURITE NUMBER: '))#prompting user to input a number then it is passed on to a control statement to check whether its odd or even
    if number%2==0:#even section
        print('it is an even number')
        #nested if to check the category of the number if its below above or equal to 10
        if number>10:#greaterthan
            print('and greaterthan 10')
        elif number<10:#lessthan
            print('and lees than 10')
        else:#otherwise equality check
            print('and it is equal to 10')
    else:#odd section
        print('it is an odd number')
        if number>10:
            print('and greaterthan 10')
        elif number<10:
            print('and lees than 10')
        else:
            print('and it is equal to 10')
    print('\n people in your age bracket and faverite number have actually prefered the following books')
    class Book:
            def __init__(self,title,author,year_published):
                self.title=title
                self.author=author
                self.year_published=year_published

            def describe(self):#creating a method for output displaywith another variable created in its parethesis description
                print('Book title: ',self.title,'\n','The author:',self.author,'\n','Year_published: ',self. year_published,'\n')

        
    book1=Book('things fall apart','chinua achebe','1999') 
    book2=Book('the concubine','chinua achebe','2000')
    book3=Book('jane Erye','charles dickens','1888')
    book4=Book('alien woman','glabiel','1898')
    book5=Book('great expectations','shakesphere','1788')
    book1.describe()
    book2.describe()#displaying the object description in the output section 
    book3.describe()
    book4.describe()
    book5.describe()


    books=[book1,book2,book3,book4,book5]
    #creating a function for sorting books by the year published
    def sort_books_by_year(books):
        if books==[]:#checking for an empty list input
            raise TypeError("Input must be a list.")#if above condition is true this should be an output error
        else:
            return sorted(books, key=lambda book: book.year_published)#otherwise this should be output
            
    print('\n here is a sample of books available sorted by year they were published') 
    #sample input for a list
    books=[book1,book2,book3,book4,book5]
    sort_books_by_year(books)#calling the sorted function which just creates a duplicate of the original list but in a sorted manner
    try: #trying to capture an error  
        sorted_books=sort_books_by_year(books)

    except Exception as e:#the error captured should be kept in a variable e
        print('there is an issue with your entries: ',e)#error captured should be concatenated to the print string and e

    for book in sorted_books:#using a for loop to print items in a list one at a time
        print(book.title,'by ',book.author,'published in',book.year_published)

    #using the while loop to iterate the books and their description in terminal one at a time
    print('sorted by while\n')
    book_number=0
    while book_number < len(sorted_books):
        book=sorted_books[book_number]
        print(book.title,book.author,book.year_published)
        book_number +=1


   #creating a method that prompts a user tho search a book from the existing collection by tittle 
    def search_book_by_title(books,title):#function name and variables in parenthesis
        for book in books:#using the foor loop to iterate a single book from the list but it only displays the book description if the user input matches one of the existing books in the list
            if book.title.lower()==title.lower():#the input should be changed to lowercase
                print('book found')
                print(book.describe())
            else:
                print('book not found')

    while True:#infinite looping to allow the user to have multiple chances to search a book unless the user is no longer interested in searching and inputs exit thats when the loop will be jumped out
        user_search_input=input('would you like to search a book by title to check in our library collection: ')
        if user_search_input=="exit":
            help=input('anything else we could assist with: ')
            if help.lower()=='no':
                print('i hope we were of help to you')
                print(f"thankyou for interacting with droid\n see you soon {name}")
            break

        search_book_by_title(books,user_search_input)#calling the function for use
        

except ValueError:#capture error if the input doesnt match the expected
    print('value input is not a number') # the output incase of an error