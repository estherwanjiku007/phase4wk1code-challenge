from configure_db import db
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

class RestaurantPizza(db.Model,SerializerMixin):
    __tablename__="restaurantpizzas"
    id=db.Column(db.Integer,primary_key=True)
    price=db.Column(db.Integer)
    pizza_id=db.Column(db.Integer,db.ForeignKey("pizzas.id"))
    restaurant_id=db.Column(db.Integer,db.ForeignKey("restaurants.id"))
    pizza=db.relationship("Pizza",back_populates="restaurantpizzas")
    restaurant=db.relationship("Restaurant",back_populates="restaurantpizzas")

    def __repr__(self):
        return f"RestaurantPizza {self.price} {self.pizza_id} {self.restaurant_id}"