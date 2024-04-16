from flask import Flask,make_response,request,jsonify
from flask_migrate import Migrate
from configure_db import db
from restaurant import Restaurant
from pizza import Pizza
from restaurantpizza import RestaurantPizza
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)
@app.route("/restaurants")
def restaurants():   
   
    all_restaurants=[restaurant.to_dict(rules=("-restaurantpizzas",)) for restaurant in Restaurant.query.all()]
    
    if all_restaurants!=None:
       
        return all_restaurants
    elif  all_restaurants==None:
         restaurant_dict={
            "Message":"Restaurant not found"
         }
         response=make_response(restaurant_dict,404)
         return response
@app.route("/restaurants/<int:id>",methods=["GET","DELETE"])
def restaurants_by_id(id):
    restaurant = Restaurant.query.filter(Restaurant.id==id).first()
    if request.method=="GET":        
        if restaurant:             
            restaurant_dict=restaurant.to_dict()      
            
            response=make_response(restaurant_dict,200)
            return response
        elif  restaurant==None:
            message_res=[]
            restaurant_dict={
                "message":"restaurant not found"
            }
            message_res.append(restaurant_dict)
            response=make_response(message_res,404)
            return response
    elif request.method=="DELETE":        
        if restaurant :
            db.session.delete(restaurant)
            db.session.commit()
            response_message={
               "message":"Restaurant deleted successfully"
            }
            response=make_response(response_message)
            return response
        elif restaurant==None:
            response_message={
                "error":"Restaurant not found"
            }
            response=make_response(response_message,404)
            
    return response

@app.route("/pizzas")
def get_all_pizzas():    
    all_pizzas=[pizzas.to_dict(rules=("-restaurantpizzas",)) for pizzas in Pizza.query.all()] 
    return make_response(all_pizzas,200)  
    
    
@app.route("/restaurant_pizza",methods=["POST"])
def post_restaurant_pizzas():
        restaurant_pizza=request.get_json()      
        new_restaurant_pizza=RestaurantPizza(
        price=restaurant_pizza.get("price"),
        pizza_id=restaurant_pizza.get("pizza_id"),
        restaurant_id=restaurant_pizza.get("restaurant_id")
    )
        db.session.add(new_restaurant_pizza)
        db.session.commit()
        #restaurant_pizza_dict=new_restaurant_pizza.to_dict()
        restaurant_pizza_dict=new_restaurant_pizza.to_dict()
        response=make_response(restaurant_pizza_dict,201)
        if response:
            return response
        else:
            response_dict={
                "Error":"Validation errors"
            }
            response=make_response(response_dict)
            return response
        

if __name__=="__main__":
    app.run(        
        port=5555,
        debug=True
    )

