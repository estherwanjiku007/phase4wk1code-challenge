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
      if restaurant!=None:
        restaurant_dict={
            "id":restaurant.id,
            "name":restaurant.name,
            "address":restaurant.address
        }
        all_resturants.append(restaurant_dict)
        response=make_response(all_resturants,200)
        return response
      elif  restaurant==None:
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
            # restaurant_dict={
            #    "id":restaurant.id,
            #    "name":restaurant.name,
            #    "address":restaurant.address,
            #    "pizzas":restaurant.restaurantpizzas
            # }
            
            #print(restaurant_dict)           
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
        if pizza!=None:      
            pizza_dict={
                "id":pizza.id,
                "name":pizza.name,
                "ingredients":pizza.ingredients
                
            }
            all_pizzas.append(pizza_dict)
            response=make_response(all_pizzas,200)        
            return response
        elif pizza==None:
            response_dict={
               "Message":"Pizza not found"
            }
            response=make_response(response_dict,404)
            return response
           
    
@app.route("/restaurant_pizza",methods=["POST"])
def post_restaurant_pizzas():      
        new_restaurant_pizza=RestaurantPizza(
        price=request.form.get("price"),
        pizza_id=request.form.get("pizza_id"),
        restaurant_id=request.form.get("restaurant_id")
    )
        db.session.add(new_restaurant_pizza)
        db.session.commit()
        #restaurant_pizza_dict=new_restaurant_pizza.to_dict()
        restaurant_pizza_dict=new_restaurant_pizza.to_dict()
        response=make_response(restaurant_pizza_dict,201)
        if response.status_code==201:
            return response
        elif response.status_code!=201:
            response_dict={
                "Error":"Validation errors"
            }
            response=make_response(response_dict)
            return response
        #if new_restaurant_pizza !=None:
         
        #  pizza_list=[]
        #  pizza_list.append(new_restaurant_pizza)         
        #  new_restaurant_pizza1=new_restaurant_pizza.pizza_id
        #  new_restaurant_pizza2=new_restaurant_pizza1.to_dict()
        #  response=make_response(new_restaurant_pizza2,201)
         
        #  return response
        # elif new_restaurant_pizza==None:
        #  my_res={
        #     "errors": ["validation errors"]
        # }
        #  response=my_res
    
        # return response

if __name__=="__main__":
    app.run(        
        port=5555,
        debug=True
    )

