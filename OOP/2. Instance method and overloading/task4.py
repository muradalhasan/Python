class Author:
    def __init__(self,name=None):
        self.name=name
        self.book={}
    def addBook(self,name,tye):
        if self.name==None:
            print("A book can not be added without author name")
        else:
            self.book[name]=tye
    def setName(self,name):
        self.name=name
    def printDetail(self):
        print(f"Number of Book(s): {len(self.book)}\nAuthor Name: {self.name}")
        for i,j in self.book.items():
            print(f"{j} : {i}")
a1 = Author()
print("===============================")
a1.addBook("Ice", "Science Fiction")
print("===============================")
a1.setName("Anna Kavan")
a1.addBook("Ice", "Science Fiction")
a1.printDetail()
print("===============================")
a2 = Author("Humayun Ahmed")
a2.addBook("Onnobhubon","Science Fiction")
a2.addBook("Megher Upor Bari", "Horror")
print("===============================")
a2.printDetail()
a2.addBook("Ireena", "Science Fiction")
print("===============================")
a2.printDetail()
print("===============================")
