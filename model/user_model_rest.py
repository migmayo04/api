import mysql.connector
import json
from flask import make_response
class user_model_rest():
    def __init__(self):
        try:
            self.con=mysql.connector.connect (host="localhost",user="root",password="1234",database="migmayo")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary = True)
            print("connection successful")
        except:
            print("some error") 

    def user_getall_rest_model(self):
        self.cur.execute("SELECT * FROM mayo_user_acc_prefs")
        result = self.cur.fetchall()
        if len(result)>0:
            return make_response({"payload":result}, 200)
        else:
            return make_response({"message":"No data found"}, 204)
        
    def user_addone_rest_model(self,data):
       #Insert data 
        self.cur.execute(f"INSERT INTO mayo_user_acc_prefs(mayoE, vendors, deliveryBoys, optionalName, mayoG, mayoAdd, mayoHC, mayoHN, pageLayout, mayoAutoConfirm, mayoAutoPrint, mayoAutoDeliverOnPrint, mayoEditOrder, optionalVendors, mayoStation, mayoDefaultSorting) VALUES('{data['mayoE']}', '{data['vendors']}','{data['deliveryBoys']}', '{data['optionalName']}', '{data['mayoG']}', '{data['mayoAdd']}', '{data['mayoHC']}', '{data['mayoHN']}', '{data['pageLayout']}', '{data['mayoAutoConfirm']}', '{data['mayoAutoPrint']}', '{data['mayoAutoDeliverOnPrint']}', '{data['mayoEditOrder']}', '{data['optionalVendors']}', '{data['mayoStation']}','{data['mayoDefaultSorting']}')")
        return make_response({"message":"User Created Successfully"}, 201)

    def user_update_rest_model(self, data):
        #Update data
        self.cur.execute(f"UPDATE mayo_user_acc_prefs SET vendors='{data['vendors']}', deliveryBoys ='{data['deliveryBoys']}', optionalName='{data['optionalName']}', mayoG='{data['mayoG']}', mayoAdd='{data['mayoAdd']}', mayoHC='{data['mayoHC']}', mayoHN='{data['mayoHN']}', pageLayout='{data['pageLayout']}', mayoAutoConfirm='{data['mayoAutoConfirm']}', mayoAutoPrint='{data['mayoAutoPrint']}', mayoAutoDeliverOnPrint='{data['mayoAutoDeliverOnPrint']}', mayoEditOrder='{data['mayoEditOrder']}', optionalVendors='{data['optionalVendors']}', mayoStation= '{data['mayoStation']}', mayoDefaultSorting='{data['mayoDefaultSorting']}' WHERE mayoE = '{data['mayoE']}'")
        if self.cur.rowcount>0:
            return make_response({"message":"User Update Successfully"}, 201)
        else:
            return make_response({"message":"Nothing to Update"}, 202)
        
    def user_delete_rest_model(self, mayoE):
        #Delete data
        self.cur.execute(f"DELETE FROM mayo_user_acc_prefs WHERE mayoE ={mayoE}")
        if self.cur.rowcount>0:
            return make_response({"message":"User Deleted Successfully"}, 200)
        else:
            return make_response({"message":"Nothing to Delete"}, 202)
        
    def user_restitems_model(self):
        self.cur.execute(f'''SELECT mayo_user_acc_prefs.mayoHN,menu_category.itemCategory
                         FROM mayo_user_acc_prefs
                         INNER JOIN menu_category
                         ON mayo_user_acc_prefs.mayoE=menu_category.userEmail''')
        result = self.cur.fetchall()
        if len(result)>0:
            return make_response({"payload":result}, 200)
        else:
            return make_response({"message":"No data found"}, 204)

    def get_user_data(self,phone):
        self.cur.execute(f"SELECT restaurant_connect FROM mayo_connect_users where user_ID={phone}")
        result = self.cur.fetchall()
        if len(result)>0:
            return json.dumps(result)
        else:
            return "No data found"

    def get_menu_cat(self,email):
        query="SELECT itemCategory FROM menu_category where userEmail= %s"
        self.cur.execute(query, (email,))
        result = self.cur.fetchall()
        if len(result)>0:
            return json.dumps(result)
        else:
            return "No data found"  

    def get_user_restid(self,restaurantid):
        self.cur.execute(f"SELECT itemCategory FROM menu_category where userEmail={restaurantid}"),
        result = self.cur.fetchall()
        if len(result)>0:
            return json.dumps(result)
        else:
            return "No data found"
        
    def get_user_itemid(self,email):
        self.cur.execute(f'''SELECT menu_items.itemName,menu_category.itemCategory,menu_items.vendorName 
                          FROM menu_items
                          INNER JOIN menu_category
                          ON menu_items.id=menu_category.id
                          WHERE menu_items.userEmail={email}''')
        result = self.cur.fetchall()
        if len(result)>0:
            return make_response({"payload":result}, 200)
        else:
            return make_response({"message":"No data found"}, 204)
        
    def get_user_login(self,userEmail):
        self.cur.execute(f"SELECT password FROM vendor_api_info where userId={userEmail}"),
        result = self.cur.fetchall()
        if len(result)>0:
            return json.dumps(result)
        else:
            return "No data found"    

    # def get_user_id(self,restaurantid,itemName):
    #     self.cur.execute(f"SELECT itemCategory FROM menu_category where userEmail={restaurantid}, itemCategory={itemName}")
    #     result = self.cur.fetchall()
    #     if len(result)>0:
    #         return json.dumps(result)
    #     else:
    #         return "No data found"    

    # def get_user_restitems(self,email,Category):
    #     self.cur.execute(f'''SELECT menu_items.itemName,menu_category.itemCategory,menu_items.vendorId 
    #                       FROM menu_items
    #                       INNER JOIN menu_category
    #                       ON menu_items.id=menu_category.id
    #                       WHERE menu_items.userEmail={email},{Category}''')
        
    #     result = self.cur.fetchall()
    #     if len(result)>0:
    #         return json.dumps(result)
    #     else:
    #         return "No data found"

    

