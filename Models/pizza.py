from configure_db import db
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from restaurantpizza import RestaurantPizza
class Pizza(db.Model,SerializerMixin):
    __tablename__="pizzas"

    id=db.Column(db.Integer,primary_key=True)    
    name=db.Column(db.String)
    ingredients=db.Column(db.String)
    restaurantpizzas=db.relationship("RestaurantPizza",back_populates="pizza",cascade="all, delete-orphan")
    restaurants=association_proxy("restaurantpizzas","restaurant",creator=lambda restaurant_obj:RestaurantPizza(restaurant=restaurant_obj))
    def __repr__(self): 
        return f"Pizza {self.id} {self.name} {self.ingredients}"
