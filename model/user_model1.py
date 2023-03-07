# import mysql.connector
# import json
# class user_model1():
#     def __init__(self):
#         try:
#             self.con=mysql.connector.connect (host="localhost", user="root", password="1234", database="migmayo")
#             self.con.autocommit=True
#             self.cur=self.con.cursor(dictionary = True)
#             print("connection successful")
#         except:
#             print("some error") 

#     def user_restaurant_model(self):
#         self.cur.execute(f"SELECT mayoHN from mayo_user_acc_prefs")
#         result = self.cur.fetchall()
#         print(result)
#         return json.dumps(result)

#     # def user_restitems_model(self):
#     #     self.cur.execute(f'''SELECT mayo_user_acc_prefs.mayoHN,menu_category.itemCategory
#     #                      FROM mayo_user_acc_prefs
#     #                      INNER JOIN menu_category
#     #                      ON mayo_user_acc_prefs.mayoE=menu_category.userEmail''')
#     #     result = self.cur.fetchall()
#     #     print(result)
#     #     return json.dumps(result)  

    
#     def user_menuitems_model(self):
#         self.cur.execute(f"SELECT itemName from menu_items")
#         result = self.cur.fetchall()
#         print(result)
#         return json.dumps(result)
    
#     def user_menucat_model(self):
#         self.cur.execute(f"SELECT itemCategory from menu_category")
#         result = self.cur.fetchall()
#         print(result)
#         return json.dumps(result)
    
#     def user_itemdt_model(self):
#         self.cur.execute(f"SELECT Train_Num_Name from order_details")
#         result = self.cur.fetchall()
#         print(result)
#         return json.dumps(result)
    
#     def user_trainname_model(self):
#         self.cur.execute(f"SELECT Train_Num_Name from order_details")
#         result = self.cur.fetchall()
#         print(result)
#         return json.dumps(result)
    
#     def user_userid_model(self):
#         self.cur.execute(f"SELECT userId from notifications")
#         result = self.cur.fetchall()
#         print(result)
#         return json.dumps(result)
    
#         # def user_addone_model(self,data):
#     #    #Insert data 
#     #     self.cur.execute(f"INSERT INTO mayo_user_acc_prefs(mayoE, vendors, deliveryBoys, optionalName, mayoG, mayoAdd, mayoHC, mayoHN, pageLayout, mayoAutoConfirm, mayoAutoPrint, mayoAutoDeliverOnPrint, mayoEditOrder, optionalVendors, mayoStation, mayoDefaultSorting) VALUES('{data['alphaId']}', '{data['userId']}','{data['orderId']}', '{data['vendor']}', '{data['Customer_name']}', '{data['Contact_number']}', '{data['Delivery_date_Time']}', '{data['status']}', '{data['remarks']}', '{data['Train_Num_Name']}', '{data['Coach_Seat']}', '{data['PNR']}', '{data['Order_type']}', '{data['orderStatusRemarks']}', '{data['deliveryExecutiveId']}','{data['isRead']}', '{data['itemDetails']}', '{data['isPrinted']}', '{data['edited']}', '{data['editedText']}', '{data['createdAt']}','{data['editedType']}')")
#     #     return "User created Sucessfully"

#     # def user_update_model(self, data):
#     #     #Update data
#     #     self.cur.execute(f"UPDATE order_details SET userId='{data['userId']}', orderId = '{data['orderId']}', vendor='{data['vendor']}', Customer_name='{data['Customer_name']}', Contact_number='{data['Contact_number']}', Delivery_date_Time='{data['Delivery_date_Time']}', status='{data['status']}', remarks='{data['remarks']}', Train_Num_Name='{data['Train_Num_Name']}', Coach_Seat='{data['Coach_Seat']}', PNR='{data['PNR']}', Order_type='{data['Order_type']}', orderStatusRemarks='{data['orderStatusRemarks']}', deliveryExecutiveId= '{data['deliveryExecutiveId']}', isRead='{data['isRead']}', itemDetails='{data['itemDetails']}', isPrinted='{data['isPrinted']}', edited='{data['edited']}', editedText='{data['editedText']}', createdAt='{data['createdAt']}', editedType='{data['editedType']}' WHERE alphaId = '{data['alphaId']}'")
#     #     if self.cur.rowcount>0:
#     #         return "User update Sucessfully"
#     #     else:
#     #         return "Nothing to Update"
        
#     # def user_delete_model(self, ):
#     #     #Delete data
#     #     self.cur.execute(f"DELETE FROM order_details WHERE alphaId ='{'alphaId'}'")
#     #     if self.cur.rowcount>0:
#     #         return "User delted Sucessfully"
#     #     else:
#     #         return "Nothing to delete"
    
    
    
                 

            
        
