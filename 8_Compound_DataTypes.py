Fruits = ['apple', 'banana', 'cherry', 'date']
Fruits.append('elderberry')
Fruits.remove('banana')
Fruits.sort()
print(Fruits)
Student = {'Name':'John Doe', 'Age':'25', 'Major':'Computer Science'}
Student['Major'] = 'Electrical Engineering'
Student['Year'] = 'Senior'
print(Student.keys())
print(Student.values())
Books = [{'Title':'Lord of the Rings','Author':'JRR Tolkien','Year':'1947'},{'Title':'Harry Potter','Author':'JK Rowling','Year':'1991'},{'Title':'The Song of Ice and Fire','Author':'GRR Martin','Year':'1988'}]
print(Books[1]['Title'])
print(Books[2]['Year'])
for Book in Books:
    print(f"The title of the book is {Book['Title']} and the author of the book is {Book['Author']}")
Courses = {'Math':['John'],'History':['Ariel', 'Elaine', 'Philip'], 'Chemistry': ['Stella']}
Math_New_Students = ['James', 'Jacqueline', 'Jonah', 'Jasmine', 'Jordan']
Courses['Math'].extend(Math_New_Students)
Courses['History'].pop(2)
for students in Courses['Chemistry']:
    print(students)