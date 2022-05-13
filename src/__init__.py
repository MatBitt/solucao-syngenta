from my_module import get_cheapest_hotel
from sys import stdin

print("Digite CTRL + D para finalizar")
print("Digite sua entrada:")

for entrada in stdin:
    print(get_cheapest_hotel(entrada))
  
