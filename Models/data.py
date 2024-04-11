from pizza import Pizza
from restaurant import  Restaurant
from restaurantpizza import  RestaurantPizza
from configure_db import db
from app import app
with app.app_context():
    Pizza.query.delete()
    Restaurant.query.delete()
    RestaurantPizza.query.delete()
    
    cheese=Pizza(name="cheese",ingredients="Dough, Tomato Sauce, Cheese")
    pepperonni=Pizza(name="Pepperroni",ingredients=" Chillie Sauce, Pepperoni")
    db.session.add_all([cheese,pepperonni])
    db.session.commit()

    Dominion_Pizza=Restaurant(name="Dominion_pizza",address="Good Italian, Ngong Road, 5th Avenue",pizzas=[cheese,pepperonni])
    Pizza_Hut=Restaurant(name="Pizza_Hut",address="Westgate Mall, Mwanzi Road, Nrb 100",pizzas=[cheese,pepperonni])
    r1=Restaurant(name="Cerena",address="Moi Avenue")
    db.session.add_all([Dominion_Pizza,Pizza_Hut,r1])
    db.session.commit()
   
    

    rp1=RestaurantPizza(price=25,restaurant_id=3,pizza_id=1)
    db.session.add(rp1)
    db.session.commit()
