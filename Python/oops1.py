# Simple oops based program with a function which reads the records from the text file.
# Converts the record into individual fields
# creating the object with fields of data read from the file and 
# Adding the object to the list of objects
# Reading the list of objects and displaying the data

class Doctor:
    doctors=[]

    def __init__(self,doc_name,doc_specification,doc_fee):
        self.doc_name=doc_name
        self.doc_specification=doc_specification
        self.doc_fee=doc_fee

    def __str__(self):
        return self.doc_name+'\t'+self.doc_specification+'\t'+str(self.doc_fee)
    
    @classmethod
    def create_docs(cls):
        with open('doctors_list.txt','r+') as doctor:
            d=doctor.readlines()
            for i in d:
                j=i.split('|')
                obj=Doctor(j[0],j[1],j[2])
                Doctor.doctors.append(obj)

if __name__=="__main__":
    Doctor.create_docs()
    for i in Doctor.doctors:
        print(i)