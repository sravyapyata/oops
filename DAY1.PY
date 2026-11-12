# creating multiple objects for a class
class ATM:
    b_name="kphb" # cls attr
    bank_name="HDFC" # cls attr 

    def __init__(self,id,branch_name,machine_location_name,pin_code,machine_number): # pre-defined / in-built method 
        self.pin="1234" # instance var
        self.main_bal=15000
        self.i= id 
        self.b =branch_name
        self.m_l=machine_location_name
        self.p_c=pin_code
        self.m_n=machine_number

    def withdraw(self): # user-defined method
        # print("withdraw method")
        pin=input("enter your pin") # 1310
        amount_to_draw=int(input("enter amount to draw"))

        if pin == self.pin :
            if  amount_to_draw < self.main_bal: # if     16000 < 15000
                print("amount drawn successfully",amount_to_draw)
            else:
                print("in-sufficient funds")
        else:
            print("mismatching pin")    

    def deposit(self):
        # print("deposit method")
        pin=input("enter your pin") # 1310
        amount_to_deposit=int(input("enter amount_to_deposit")) # 5000
        if pin == self.pin:
            self.main_bal +=  amount_to_deposit # 15000 + 5000 = 20000
            print(self.main_bal, "after deposit")
        else:
            print("wrong pin")    

    def bal_check(self):
        # print("bal check method")
        pin=input("enter your pin") # 1310
        if pin == self.pin :
            print("main bal",self.main_bal)
        else:
            print("mismatching pin")    


obj=ATM(1,"AXIX","Kukataplly",500072,"AXIXABCD1234") # obj1

print("choose below to proceed")
print("1. withdraw   2.deposit  3.bal_enquiry")

o=int(input("enter yr option number"))

if o == 1:
    obj.withdraw()
elif o == 2:
    obj.deposit()    
elif o == 3:
    obj.bal_check()
else:
    print("enter proper valid option number")    

# creating multiple objects for same class :-- 
# reusability :-- 
# independent state - independent data for every obj that we can pass to class 

# obj2=ATM(2,"AXIX","Kukatapally",500072,"AXIXABCD1235") # obj2 

# obj3=ATM(3,"AXIX","Kukatapally",500072,"AXIXABCD1236") # obj3


# reusability :-- 
# independent state - independent data for every obj that we can pass to class