class bikeshop:

    def __init__(self,stock):
        self.stock=stock                  # ya 2 lines stock bana rhi hain
    def displybike(self):
        print("Total Bikes",self.stock)   # ya total bikes show kra ga
    def displayonebikeprice(self):
        print("RS=100")
    def rentForBike(self,q):              # is main ap katni bikes hain wo add karin ga Q sa
        if q<=0:                          # ager zero sa kam yani -1 ho to ya print ho
            print("enter the postive value or greater then zero")
        elif q>self.stock:                # jitna stock ha us ka braber ya kam value add kro
            print("enter the value (less the stock)")
        else:
         self.stock=self.stock-q
         print("total price",q*100)
         print("bikes left",self.stock)

while True:
    obj=bikeshop(100)   #obj bana usi main katni bike avilable hen set ho gya
    uc=int(input('''
1 Disply stocks
2 Rent a bike
3 one bike price
4 Exit    
    '''))

    if uc==1:
        obj.displybike()     # ager uc user input 1 ho to bike show kro
    elif uc==2:              # ager 2 ho to user sa puchco kitna bike cahiya
        n=int(input("enter the qty=--"))
        obj.rentForBike(n)
    elif uc==3:
        obj.displayonebikeprice()
    else:                    # ager input 3 ho to app sa bahr
        break
