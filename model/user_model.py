import mysql.connector
import json
from flask import make_response
class user_model():
    def __init__(self):
        try:
            self.con=mysql.connector.connect (host="localhost",user="root",password="1234",database="migmayo")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary = True)
            print("connection successful")
        except:
            print("some error") 

    def user_getall_model(self):
        self.cur.execute("SELECT * FROM order_details")
        result = self.cur.fetchall()
        if len(result)>0:
            return make_response({"payload":result}, 200)
        else:
            return make_response({"message":"No Data Found"}, 204)

    def user_addone_model(self,data):
       #Insert data 
        self.cur.execute(f"INSERT INTO order_details(alphaId, userId, orderId, vendor, Customer_name, Contact_number, Delivery_date_Time, status, remarks, Train_Num_Name, Coach_Seat, PNR, Order_type, orderStatusRemarks, deliveryExecutiveId, isRead, itemDetails, isPrinted, edited, editedText, createdAt, editedType) VALUES('{data['alphaId']}', '{data['userId']}','{data['orderId']}', '{data['vendor']}', '{data['Customer_name']}', '{data['Contact_number']}', '{data['Delivery_date_Time']}', '{data['status']}', '{data['remarks']}', '{data['Train_Num_Name']}', '{data['Coach_Seat']}', '{data['PNR']}', '{data['Order_type']}', '{data['orderStatusRemarks']}', '{data['deliveryExecutiveId']}','{data['isRead']}', '{data['itemDetails']}', '{data['isPrinted']}', '{data['edited']}', '{data['editedText']}', '{data['createdAt']}','{data['editedType']}')")
        return make_response({"message":"User Created Successfully"}, 201)

    def user_update_model(self, data):
        #Update data
        self.cur.execute(f"UPDATE order_details SET userId='{data['userId']}', alphaId = '{data['alphaId']}', vendor='{data['vendor']}', Customer_name='{data['Customer_name']}', Contact_number='{data['Contact_number']}', Delivery_date_Time='{data['Delivery_date_Time']}', status='{data['status']}', remarks='{data['remarks']}', Train_Num_Name='{data['Train_Num_Name']}', Coach_Seat='{data['Coach_Seat']}', PNR='{data['PNR']}', Order_type='{data['Order_type']}', orderStatusRemarks='{data['orderStatusRemarks']}', deliveryExecutiveId= '{data['deliveryExecutiveId']}', isRead='{data['isRead']}', itemDetails='{data['itemDetails']}', isPrinted='{data['isPrinted']}', edited='{data['edited']}', editedText='{data['editedText']}', createdAt='{data['createdAt']}', editedType='{data['editedType']}' WHERE orderId = '{data['orderId']}'")
        if self.cur.rowcount>0:
            return make_response({"message":"User Update Successfully"}, 201)
        else:
            return make_response({"message":"Nothing to Update"}, 202)
        
    def user_delete_model(self, orderId):
        #Delete data
        self.cur.execute(f"DELETE FROM order_details WHERE orderId ={orderId}")
        if self.cur.rowcount>0:
            return make_response({"message":"User Deleted Successfully"}, 200)
        else:
            return make_response({"message":"Nothing to Delete"}, 202)
    
    
    
                 

            
        
