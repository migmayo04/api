from app import app
from model.user_model_rest import user_model_rest
from flask import request
obj = user_model_rest()

@app.route("/user/getall_rest")
def user_getall_rest_controller():
    return obj.user_getall_rest_model()

@app.route("/user/addone_rest", methods=['POST'])
def user_addone_rest_controller():
    return obj.user_addone_rest_model(request.form)

@app.route("/user/update_rest", methods=['PUT'])
def user_update_rest_controller():
    return obj.user_update_rest_model(request.form)

@app.route("/user/delete/<mayoE>", methods=['DELETE'])
def user_delete_rest_controller(mayoE):
    return obj.user_delete_rest_model(mayoE)

@app.route("/user/restitems")
def user_restitems_controller():
    return obj.user_restitems_model()

@app.route("/user/get_user_data", methods=['GET'])
def get_user_data():
    phone = request.args.get("phone")
    return obj.get_user_data(phone)

@app.route("/user/get_menu_cat", methods=['GET'])
def get_menu_cat():
    email = request.args.get("email")
    return obj.get_menu_cat(email)

@app.route("/user/get_user_restid", methods=['GET'])
def get_user_restid():
    restaurantid = request.args.get("restaurantid")
    return obj.get_user_restid(restaurantid)

@app.route("/user/get_user_itemid", methods=['GET'])
def get_user_itemid():
    email = request.args.get("email")
    return obj.get_user_itemid(email)

@app.route("/user/get_user_login", methods=['GET'])
def get_user_login():
    userEmail = request.args.get("userEmail")
    return obj.get_user_login(userEmail)

# @app.route("/user/get_user_id", methods=['GET'])
# def get_user_id():
#     restaurantid= request.args.get("restaurantid"),
#     itemName= request.args.get("itemName")   
#     return obj.get_user_id(restaurantid,itemName)
    









