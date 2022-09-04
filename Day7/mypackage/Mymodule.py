gname="Abi"
sports = ['cricket','soccer','tennis','hockey','swimming']
runs = {'tests':18500,'ODI':15200,'T20':2500}

def greet(gst):
    print(f"Greeting {gst},Welcome to the annual meet.......")

class Product:
    prdcntr = 0
    def __init__(self,name,price):
        self.name = name
        self.price = price
        Product.prdcntr +=1
    def get_details(self):
        print(f" Name is {self.name}\n Price is {self.price}")
        print(f" There are  {Product.prdcntr} products added.....")

if __name__ == '__main__':
    kitkat = Product("kitkat",40)
    kitkat.get_details()











