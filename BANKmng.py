import pickle
import os
class account():
    
    def __init__(self,a,b,c):
        self.name=a
        self.acc=self.accountno()
        self.amount=b
        if c in {'A','a'}:
            self.type='SAVING'
        elif c in {'b','B'}:
           
            self.type='CURRENT'
        
    def accountno(self):
        try:
            file=open("bank.bin",'rb')
            while True:
                    t=pickle.load(file)
        except FileNotFoundError:
            file=open("bank.bin",'wb')
            self.acc=60126446554
            file.close()
            return self.acc
        except EOFError:
            self.acc=t.acc+1
            file.close()
            return self.acc
    def display(self):
        print(self.name)
        print(self.acc,'\t',self.type)
        print(self.amount)
       
def create():
    print("ENTER YOUR NAME")
    k=input()
    print("a.SAVINAG ACCOUNT b.CURRENT ACCOUNT")
    i=input()
    print("ENTER AMOUNT")
    h=float(input())
    while True:
        if h<5000:
            print("Amm. must be greater than 5000 enter again:")
            h=float(input())
        else:
            break
    a=account(k,h,i)
    file=open('bank.bin','ab')
    pickle.dump(a,file)
    file.close()
    account.display(a)
    return a

def deposite():
    print("ENTER ACCOUNT NUMBER")
    acc=int(input())
    print("ENTER AMMOUNT")
    amt=float(input())
    try:
        file=open("bank.bin",'rb')
        file1=open("temp.bin",'ab')
        while True:
            t=pickle.load(file)
            if t.acc==acc:
                t.amount+=amt
            pickle.dump(t,file1)
    except EOFError:
        file.close()
        file1.close()
    os.remove('bank.bin')
    os.rename('temp.bin','bank.bin')
def withdraw():
    print("ENTER ACCOUNT NUMBER")
    acc=int(input())
    print("ENTER AMMOUNT")
    amt=float(input())
    try:
        file=open("bank.bin",'rb')
        file1=open("temp.bin",'ab')
        while True:
            t=pickle.load(file)
            if t.acc==acc:
                t.amount-=amt
            pickle.dump(t,file1)
    except EOFError:
        file.close()
        file1.close()
    os.remove('bank.bin')
    os.rename('temp.bin','bank.bin')
def BalInqry():
    print("ENTER ACCOUNT NUMBER")
    acc=int(input())
    try:
        file=open("bank.bin",'rb')
        while True:
            t=pickle.load(file)
            if t.acc==acc:
                print(t.amount)
                
    except EOFError:
        file.close()
def list():
    try:
        file=open("bank.bin",'rb')
        while True:
            t=pickle.load(file)
            t.display()
            print()
    except:
        print('thank you')
def close():
    print("ENTER ACCOUNT NUMBER")
    acc=int(input())
    try:
        file=open("bank.bin",'rb')
        file1=open('temp.bin','ab')
        while True:
            t=pickle.load(file)
            if t.acc!=acc:
                pickle.dump(t,file1)
            
    except EOFError:
        file.close()
        file1.close()
    os.remove('bank.bin')
    os.rename('temp.bin','bank.bin')
    
print("PLEASE ENTER YOUR CHOICE\n 1.CREATE ACCOUNT\n 2.DEPOSITE AMOUNT\n 3.WITHDRAW AMOUNT\n 4.BALANCE INQUIRY\n 5.VIEW LIST\n 6.CLOSE ACCOUNT\n 7.EXIT\n  ")
while True:
    print('ENTER YOUR CHOICE')
    N=int(input())
    if N==1:
        create()
    elif N==2:
        deposite()
    elif N==3:
        withdraw()
    elif N==4:
        BalInqry()
    elif N==5:
        list()
    elif N==6:
        close()
    elif N==7:
        break
   
    
    
    
    
