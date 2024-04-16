### APP

### MODELS:

This App is run through postman and is run using a local host.In this project,there are three models:Restaurant,Pizza and RestaurantPizza.A Pizza has many restaurants and a Restaurant has many Pizzas.RestaurantPizza is responsible for holding the relationship of the two tables.There are tables each having a pluralized name of the associated model and also lowercased.There are also three files for holding the models and an app.py file for running the app.

### TABLES

There are three tables,
1.pizzas table
which contains an id and a name as the columns which is held by the Pizza model.It also has a relationship called restaurantpizzas where we can retreive the related restaurant.
2.restaurants table
This table contains the id and name of a restaurant.It also contains a relationship where we can retreive the pizza related to this restaurant.

3.restaurantpizzas
This table contains an id ,a pizza_id which is a an id that references a pizza instance,a restaurant_id which is an id that references a restaurant instance

### ROUTES

1. restaurants
   This route should return all restaurants in form of json with the id and name of the restaurant in the form
   [
   {
   "address": "Good Italian, Ngong Road, 5th Avenue",
   "id": 1,
   "name": "Dominion_pizza"
   },
   {
   "address": "Westgate Mall, Mwanzi Road, Nrb 100",
   "id": 2,
   "name": "Pizza_Hut"
   },

] 2. restaurants/id
This oute should return a specific restaurant wih the given id .If the restaurant is not found it should return an error message in the form
[
{
"message": "restaurant not found"
}
]

3. pizzas
   This route should return all pizzas in the form of an array with the id,name and ingredients of the pizza in the following form:
   [
   {
   "id": 1,
   "ingredients": "Dough, Tomato Sauce, Cheese",
   "name": "cheese"
   },
   {
   "id": 2,
   "ingredients": " Chillie Sauce, Pepperoni",
   "name": "Pepperroni"
   }
   ]
4. restaurant_pizzas
   In this route, we can only post data.We can create a new RestaurantPizza instannce by providing the price,pizza_id,restaurant_id.This will add a new instance to the database and return a response in the following form if it was created successfully:

{
"price": 5,
"pizza_id": 1,
"restaurant_id": 3
}
I f it was not created successfully,it should return an error message in the following form:

{
"errors": ["validation errors"]
}
