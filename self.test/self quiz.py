# TEST 1

# a.) OUTPUT ALL CONTINENTS FROM THE CONTINENTS LIST ONE AFTER ANOTHER

continents = ["Asia", "Europe", "Africa","Antartica", "North America", "S. America", "Australia and Oceania"]
for continent in continents:
    print(continent)
print ("  \n")

# b.) OUTPUT ONLY THE INHABITED CONTINENTS FROM THE LIST

continents = ["Asia", "Europe", "Africa","Antartica", "North America", "S. America", "Australia and Oceania"]
for continent in continents:
    if continent == "Antartica":
        continue
    print (continent)
print ("\n")

# c.) OUTPUT ONLY THE CONTINENTS FROM THE STUFF LIST

fave = ["Asia", "Europe"]
continents = ["Asia", "Europe", "Africa","Antartica", "North America", "S. America", "Australia and Oceania"]
for c in fave:
    if c in continents:
        print (c)
print("\n")

# d.) HOW MANY CONTINENTS ARE INCLUDED IN THE FAVE?

count = []
for c in fave:
  if c in continents:
    count.append(fave)
print (len(count))
#or
count = 0
for c in fave:
  if c in continents:
    count = count + 1
print (count)
print("\n")

# TEST 2 - SIMPLIFY THE CALCULATION OF THE REDUCED PRICES WITH AN IF-ELSEIF-ELSE STRUCTURE
# NOTE!! costing between 0 to 20 thalers(currency) inclusively will be reduced by 20%, 20 to 50 thalers will be reduced 40% and 50 above will be reduced 80%

# a.) Output the new discounted price for the price variable
price = 50
if price <= 20:
   price = price * .8
elif price <= 50:
   price = price * .6
else:
   price = price * .2
print (price)
print ("\n")

# b.) CALCULATE FOR EACH OF THE OLD PRICE AND STORE IT INTO THE NEW PRICE LIST

prices = [2,50,100,30,70,22,19]
new_prices =[]
for price in prices:
  if price <= 20:
    price = price * .8
  elif price <= 50:
     price = price * .6
  else:
     price = price * .2
  new_prices.append(price)
print (new_prices)
print("\n")

# c.) OLD PRICE ARE ONLY DISCOUNTED

chaos = ["old price: 50", "new price: 24", "old price: 44", "new price: 33", "old price: 25", "new price: 33"]
order = []

for word in chaos:
    price = int((word.split(": ")[1]))
    if "old" in word:
      if price <= 20:
        price = price * .8
      elif price <= 50:
        price = price * .6
      else:
        price = price * .2
    order.append(price)
print(order)