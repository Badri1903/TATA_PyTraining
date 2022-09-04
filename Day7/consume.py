import sys

sys.path.append('D:/delhi')

for i in sys.path:
    print(i)

from gurgaon.Mymodule import Product

p1 = Product('Perk', 20)
p1.get_details()