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
    all_resturants=[]
    Restaurant.query.all()
    for restaurant in Restaurant.query.all():
        restaurant_dict={
            "id":restaurant.id,
            "name":restaurant.name,
            "address":restaurant.address
        }
        all_resturants.append(restaurant_dict)
    response=make_response(all_resturants,200)
    return response

@app.route("/restaurants/<int:id>",methods=["GET","DELETE"])
def restaurants_by_id(id):
    if request.method=="GET": 
          
       restaurant=Restaurant.query.filter(Restaurant.id==id).first()
       if restaurant:
        restaurant_dict={
            "id":restaurant.id,
            "name": restaurant.name,
            "address":restaurant.address,
            "pizzas":restaurant.pizzas
        }
        response=make_response(restaurant_dict,200)
       else:

        myres={
        "error":"restaurant not found"
    }
        response=make_response(myres,200)    
    elif request.method=="DELETE":
        restaurant=Restaurant.query.filter(Restaurant.id==id)
        if restaurant:
            db.session.delete(restaurant)
        db.session.commit()
        response=make_response(restaurant,200)
        return response
    else:
        response={
            "error":"Resaturant not found"
        }

    return response

# @app.route("/DELETE/restaurants/<int:id>")
# def delete_restaurant(id):
#     restaurant=restaurants_by_id(id)
#     if restaurant:
#         db.session.delete(restaurant)
#         db.session.commit()
#         response=make_response(restaurant,200)
#         return response
#     else:
#         response={
#             "error":"Resaturant not found"
#         }
#     return response,response.status_code
@app.route("/pizzas")
def get_all_pizzas():    
       all_pizzas=[]       
       for pizza in Pizza.query.all():
        pizza_dict={
            "id":pizza.id,
            "name":pizza.name,
            "ingredients":pizza.ingredients
            
        }
        all_pizzas.append(pizza_dict)
        response=make_response(all_pizzas,200)
        return response
    # elif request.method=="POST":
    #    new_restaurant_pizza=RestaurantPizza(
    #     price=request.form.get("price"),
    #     pizza_id=request.form.get("pizza_id"),
    #     restaurant_id=request.form.get("restaurant_id")
    # )
    #    db.session.add(new_restaurant_pizza)
    #    db.session.commit()
    #    restaurant_pizza_dict=new_restaurant_pizza.to_dict()
    
    #    if restaurant_pizza_dict:
    #     response=make_response(restaurant_pizza_dict,201)
        
    #    else:
    #     my_res={
    #         "errors": ["validation errors"]
    #     }
    #     response=my_res        
    #    return response,response.status_code       
    # return response
@app.route("/restaurant_pizza")
def post_restaurant_pizzas():
    new_restaurant_pizza=RestaurantPizza(
        price=request.form.get("price"),
        pizza_id=request.form.get("pizza_id"),
        restaurant_id=request.form.get("restaurant_id")
    )
    db.session.add(new_restaurant_pizza)
    db.session.commit()
    restaurant_pizza_dict=new_restaurant_pizza.to_dict()
    
    if restaurant_pizza_dict:
        response=make_response(restaurant_pizza_dict,201)
        return response
    else:
        my_res={
            "errors": ["validation errors"]
        }
        response=my_res
    
    return response,response.status_code

if __name__=="__main__":
    app.run(
        host="localhost",
        port=5555,
        debug=True
    )

