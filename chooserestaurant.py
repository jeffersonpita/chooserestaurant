#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import sys, getopt

name, rating, distance, cuisine, price = '', None, None, '', None

# Receive data from params
argumentList = sys.argv[1:]
options = "n:r:d:c:p:"
long_options = ["name=", "rating=", "distance=", "cuisine=", "price="]
try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)

    # checking each argument
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-n", "--name"):
            name = currentValue
        if currentArgument in ("-r", "--rating"):
            rating = int(currentValue)
        if currentArgument in ("-d", "--distance"):
            distance = int(currentValue)
        if currentArgument in ("-c", "--cuisine"):
            cuisine = currentValue
        if currentArgument in ("-p", "--price"):
            price = int(currentValue)
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))

# Print query
print("Query: \nname=%s \nrating=%s \ndistance=%s \ncuisine=%s \nprice=%s " % (name, rating, distance, cuisine, price))



# To print errors
def errorMsg( msg ):
    return {'status':0, 'message':msg }

# Main function, used to wrangle the data
def searchRestaurants( name, rating, distance, cuisine, price ):
    # Prevent errors caused empty values in integer params
    if rating=='': rating = None
    if distance=='': distance = None
    if price=='': price = None

    # Return error messages if rating, distance and price are not integers, None nor empty
    if rating and not isinstance(rating, int):
        return errorMsg("Rating param must be an integer")
    if distance and not isinstance(distance, int):
        return errorMsg("Distance param must be an integer")
    if price and not isinstance(price, int):
        return errorMsg("Price param must be an integer")

    # Load csv's into memory
    restaurants = pd.read_csv("restaurants.csv")
    cuisines = pd.read_csv("cuisines.csv")
    # Merge them using "cuisine_id" as foreign_key
    restaurants = pd.merge(restaurants, cuisines, how='left', left_on = 'cuisine_id', right_on = 'id')
    # Keep only important columns
    restaurants = restaurants[['name_x', 'name_y', 'customer_rating', 'distance', 'price']]
    # Rename columns
    restaurants.columns = ['name', 'cuisine', 'customer_rating', 'distance', 'price']

    # Filter restaurants by name
    if name and len(name)>0:
        restaurants = restaurants[restaurants['name'].str.contains(name)]

    # Filter restaurants by customer_rating (greater than or equal to requested)
    if rating!=None:
        restaurants = restaurants[restaurants['customer_rating']>=rating]

     # Filter restaurants by distance (lower than or equal to requested)
    if distance!=None:
        restaurants = restaurants[restaurants['distance']<=distance]

     # Filter restaurants by price (lower than or equal to requested)
    if price!=None:
        restaurants = restaurants[restaurants['price']<=price]

    # Filter restaurants by cuisine
    if cuisine and len(cuisine)>0:
        restaurants = restaurants[restaurants['cuisine'].str.contains(cuisine)]

    # Sort restaurants by distance ASC, customer_rating DESC and price ASC
    # So the best restaurants are those with lower distance, greater rating and lower price as possible
    restaurants = restaurants.sort_values(by=["distance", "customer_rating", "price"],
                                          ascending=[True, False, True])

    # Filter restaurants to the 5 top choices
    restaurants = restaurants.iloc[0:5]

    return {'status':1, 'data':restaurants }


#example
#result = searchRestaurants( 'Bar', 3, 5, 'It', 20 )
result = searchRestaurants( name, rating, distance, cuisine, price )

if result['status']==1:
    print(result['data'])
else:
    print(result['message'])







# In[ ]:





# In[ ]:





# In[ ]:
