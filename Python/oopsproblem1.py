# Problem Statement:
# -----------------------------
# Create a class Bank with below attributes:
# +string-Name
# +int-account number
# +int-balance

# create __init__ method which takes all parameters in the above sequence .
# The method should set the value of attributes to parameter values inside the method

# Implement the method-findMaxBalance in the bank class .This method will return  the maximum value for balance 
# of all the accounts in the account List of Bank class 

# Instruction:
# -----------------------
# +You would require to write the main section completely ,hence please follow the below instructions for the same
# +You would require to write the main program which is in the line to the sample input description section 
#  mentioned below and to read the data in the same sequence
# +To create the bank objects ,take the input in the below sequence

#     1.To create a list of n Bank objects read the value of n
#     2.To create a list of n Bank objects read values for name,account_no,balance(in this order) and create the 
#       Bank object and add to the list.Repeat this step n times 
#     3.Create the Bank object by passing name,account_no,balance and the list of accounts created in previous step
# +call the method findMaxBalance using the Bank object created in point 3

class Bank:
    def __init__(self,name,accno,accbalance):
        self.name=name
        self.account_no=accno
        self.balance=accbalance

    def findMaxBalance(self,acc_list):
        print(*acc_list,sep='\n')
        if len(acc_list)==0:
            return None
        else:
            max_balance=max(acc_list,key=lambda x:x.balance)
            return max_balance

if __name__=='__main__':
    blist=[]
    n=int(input("Enter the number accounts in the bank:"))
    for i in range(n):
        name=input("Enter account holder name:")
        account_no=int(input("Enter account number:"))
        account_balance=int(input("Enter account balance:"))
        blist.append(Bank(name,account_no,account_balance))

    bankobj=Bank(name,account_no,account_balance)
    records=bankobj.findMaxBalance(blist)

    if records==None:
        print("No Data found")
    else:
        print(records.name)
        print(records.account_no)
