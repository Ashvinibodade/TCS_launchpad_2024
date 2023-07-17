# Full fledged program with demonstrate
# -Object collaboration concept
# -constructor
# -Members function which access the objects data ,compare/process the two objects data
# -Adding the object into dictionary of objects ,travelling and reading the data from dictionary of objects->
# Creating the objects with the data read from the dictionary of objects and adding the object to lost of objects
# -Traversing the list/dictionary of objects to individual data members

class Book:
    def __init__(self,id,name,technology):
        self.id=id
        self.name=name
        self.technology=technology

class Bookstore:
    def __init__(self,bookdict):
        self.bookdb=bookdict

    def searchbytechnology(self,tech):
        abc=[]
        restech=[]
        flag=0
        # Traversing the dictionary of object
        for ab in self.bookdb.keys():
            # print(self.bookdb[ab].id)
            # print(tech)
            # print(self.bookdb[ab].technology)
            if(tech==self.bookdb[ab].technology):
                print(self.bookdb[ab].technology)
                restech.append(self.bookdb[ab])  #Adding the object to the list of object
                flag=1
        if flag==0:
            abc.append("NULL")
            abc.append("NULL")
            abc.append("NULL")
            abc.append("NULL")
            restech.append(abc)
        return restech
        # return (self.bookdb[ab])
    
    def comparebooks(self,a,b):
        if (a.name==b.name):
            print("Books are same")
        else:
            print("Books are not same")

if __name__=='__main__':
    bookdb={}
    bookcount_master=int(input("Enter count of book:"))
    for i in range(bookcount_master):
        id=input("Enter id for book:")
        name=input("Enter name of book:")
        technology=input("Enter technology of book:")
        bookobj=Book(id,name,technology)
        bookdb.update({i:bookobj})
    
    bookstoreobj=Bookstore(bookdb)
    tech_searchfor=input("Enter technology to search book:")
    restech=bookstoreobj.searchbytechnology(tech_searchfor)
    for k in restech:
        print(k.id)
        print(k.name)
        print(k.technology)

    id1=input("Enter id1 :")
    name1=input("Enter name1:")
    technology1=input("Enter technology1:")
    bookobj1=Book(id1,name1,technology1)

    id2=input("Enter id2:")
    name2=input("Enter name2:")
    technology2=input("Enter technology2:")
    bookobj2=Book(id2,name2,technology2)

    bookstoreobj.comparebooks(bookobj1,bookobj2)
