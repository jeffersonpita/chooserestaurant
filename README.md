# Choose Restaurant
Choose the best restaurant based on restaurants.csv

### USAGE
python chooserestaurant.py -n Bar -r 3 -d 5 -p 20 -c Chinese

-n or --name=
Name of the Restaurant

-r or --rating=
Minimum rating of the restaurant

-d or --distance=
Maximum distance to the restaurant

-p or --price=
Maximum medium price of the restaurant

-c or --cuisine
Restaurant's cuisine's type

####
python chooserestaurant.py --name=Bar --rating=3 --distance=5 --price=20 --cuisine=Chinese
python chooserestaurant.py --name=Bar --rating=3
python chooserestaurant.py

### Code
Original code found at Choose Restaurant.ipynb

def searchRestaurants( name, rating, distance, cuisine, price )

Function searchRestaurants receives the 5 parameters: name, rating, distance,
cuisine, price and returns the 5 top restaurants based on the args.
