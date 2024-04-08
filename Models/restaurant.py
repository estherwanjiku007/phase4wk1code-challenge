from configure_db import db
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from restaurantpizza import RestaurantPizza
class Restaurant(db.Model,SerializerMixin):
    __tablename__="restaurants"
    
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(49),unique=True)
    address=db.Column(db.String)
    restaurantpizzas=db.relationship("RestaurantPizza",back_populates="restaurant",cascade="all , delete-orphan")
    pizzas=association_proxy("restaurantpizzas","pizza",creator=lambda pizza_obj:RestaurantPizza(pizza=pizza_obj))
    def __repr__(self):
        return f"Restaurant {self.id} {self.name} {self.address}"
