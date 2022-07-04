import os.path
class Tester:
    def create(self):
        print("*****Tester Data******")
        tester=input("enter file name")
        tester=open("tester","x")
        t=open("tester","a")
        self.id=input("Enter id:")
        self.name=input("enter name:")
        self.age=input("enter age:")
        self.sal=input("enter salary:")
        self.desig=input("enter designation:")
        t.write(self.id)
        t.write(self.name)
        t.write(self.age)
        t.write(self.sal)
        t.write(self.desig)
        t.close()
    def display(self):
        print("*****Tester Data******")
        te=open("tester","r")
        print(te.read())
    def list(self):
        print("*************************")
        print("select an operation:")
        print("1.create")
        print("2.display")
        print("3.exit")
class Manager:
    def create(self):
        print("*****Manager Data******")
        manager=input("enter file name")
        manager=open("manager","x")
        m=open("manager","a")
        self.id=input("Enter id:")
        self.name=input("enter name:")
        self.age=input("enter age:")
        self.sal=input("enter salary:")
        self.desig=input("enter designation:")
        m.write(self.id)
        m.write(self.name)
        m.write(self.age)
        m.write(self.sal)
        m.write(self.desig)
        m.close()
    def display(self):
        print("*****Manager Data******")
        mg=open("manager","r")
        print(mg.read())
    def list(self):
        print("*************************")
        print("select an operation:")
        print("1.create")
        print("2.display")
        print("3.exit")
class Developer:
    def create(self):
        print("*****Developer Data******")
        dev=input("enter file name")
        dev=open("dev","x")
        d=open("dev","a")
        self.id=input("Enter id:")
        self.name=input("enter name:")
        self.age=input("enter age:")
        self.sal=input("enter salary:")
        self.desig=input("enter designation:")
        d.write(self.id)
        d.write(self.name)
        d.write(self.age)
        d.write(self.sal)
        d.write(self.desig)
        d.close()
    def display(self):
        print("*****Manager Data******")
        dv=open("dev","r")
        print(dv.read())
    def list(self):
        print("*************************")
        print("select an operation:")
        print("1.create")
        print("2.display")
        print("3.exit")
class Clerk:
    def create(self):
        print("*****Clerk Data******")
        clerk=input("enter file name")
        clerk=open("clerk","x")
        c=open("clerk","a")
        self.id=input("Enter id:")
        self.name=input("enter name:")
        self.age=input("enter age:")
        self.sal=input("enter salary:")
        self.desig=input("enter designation:")
        c.write(self.id)
        c.write(self.name)
        c.write(self.age)
        c.write(self.sal)
        c.write(self.desig)
        c.close()
    def display(self):
        print("*****Clerk Data******")
        cl=open("clerk","r")
        print(cl.read())
    def list(self):
        print("*************************")
        print("select an operation:")
        print("1.create")
        print("2.display")
        print("3.exit")
T=Tester()
D=Developer()
M=Manager()
C=Clerk()

print("*************************")
print("select an operation:")
print("1.create")
print("2.display")
print("3.exit")

while True:
    n=int(input("Enter choice:"))
    print("*************************")
    if(n==1):
        print("1.Enter Tester data")
        print("1.Enter Manager data")
        print("1.Enter Developer data")
        print("1.Enter Clerk data")
        ch=int(input("select an employee to create data:"))
        print("*********************************")
        if(ch==1):
            if os.path.exists("tester"):
                print("you have already created tester data...")
                T.list()
            else:
                T.create()
                T.list()
        elif(ch==2):
            if os.path.exists("manager"):
                print("you have already created manager data...")
                M.list()
            else:
                M.create()
                M.list()
        elif(ch==3):
            if os.path.exists("dev"):
                print("you have already created developer data...")
                D.list()
            else:
                D.create()
                D.list()
        elif(ch==4):
            if os.path.exists("clerk"):
                print("you have already created clerk data...")
                C.list()
            else:
                C.create()
                C.list()
        else:
            print("Please enter valid option....")
            C.list()
    if(n==2):
        print("1.Enter Tester data")
        print("1.Enter Manager data")
        print("1.Enter Developer data")
        print("1.Enter Clerk data")
        n1=int(input("select an employee to display data:"))
        print("*********************************")
        if(n1==1):
            if os.path.exists("tester"):
                T.display()
                T.list()
            else:
                print("Please create tester data...")
                T.create()
                T.display()
                T.list()
        elif(n1==2):
            if os.path.exists("manager"):
                M.display()
                M.list()
            else:
                print("Please create manager data...")
                M.create()
                M.display()
                M.list()
        elif(n1==3):
            if os.path.exists("dev"):
                D.display()
                D.list()
            else:
                print("Please create developer data...")
                D.create()
                D.display()
                D.list()
        elif(n1==4):
            if os.path.exists("clerk"):
                C.display()
                C.list()
            else:
                print("Please create clerk data...")
                C.create()
                C.display()
                C.list()
        else:
            e=int(input("enter 1 to continue otherwise enter 0 to exit:"))
            if(e==1):
                C.list()
            else:
                print("you have choosen to exit...")
                break
    if(n==3):
        print("If you want to exit enter 0 otherwise enter 1 to continue:")
        o=int(input("Enter choice:"))
        if(o==1):
            C.list()
        if(o==0):
            print("Thank you....")
            break
        
