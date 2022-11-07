from modules import Restaurant, IceCreamStand

# creating instance of restaurant child class icecreamstand
peten_jaatelo = IceCreamStand('peten jäätelo', 'ice cream', ['vanilla', 'chocolate', 'liquorice', 'pear', 'salmiac'])
peten_jaatelo.describe_restaurant()
peten_jaatelo.open_restaurant()
peten_jaatelo.print_flavors()