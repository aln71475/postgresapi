import psycopg2
import pandas as pd
from psycopg2.extras import RealDictCursor
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

conn = psycopg2.connect(database="accounts_db",
                        host="localhost",
                        user="john",
                        password="password",
                        port="5432")

cursor = conn.cursor(cursor_factory=RealDictCursor)

# @app.route('/update/fullresultsdf/<email>',methods = ['PUT'])
# def update(email):
#    return email

@app.route('/getdata/fullresultsdf',methods = ['POST', 'GET'])
def getdata1():
   cursor.execute("SELECT * FROM fullresultsdf")
   return cursor.fetchall()

@app.route('/getdata/bypass_df_merged',methods = ['POST', 'GET'])
def getdata2():
   cursor.execute("SELECT * FROM bypass_df_merged")
   return cursor.fetchall()

@app.route('/getdata/newaccounts',methods = ['POST', 'GET'])
def getdata3():
   cursor.execute("SELECT * FROM newaccounts")
   return cursor.fetchall()


@app.route('/update/fullresultsdf/<email>',methods = ['PUT'])
def fullresultsdf1(email):
   x = request.json
   values = (x['id'],x['first_name'],x['last_name'],x['email'],x['type'],x['password'],x['delta_password'],x['recovery_email'],x['email_forwarding'],x['auto_po_seats_scouts'],x['errors_failed'],x['tm_created'],x['tm_password'],x['tm_address'],x['axs_created'],x['axs_password'],x['sg_created'],x['sg_password'],x['tickets_com_created'],x['facebook_created'],x['twitter_created'],x['eventbrite'],x['etix'],x['ticket_web'],x['big_tickets'],x['amazon'],x['secondary_password'],x['seat_scouts_added'],x['seat_scouts_status'],x['team'],x['specific_team'],x['forward_to'],x['forward_email_password'],x['seat_scouts_password'],x['password_matching'],x['disabled'],x['created_by'],x['edited_by'],x['ld_computer_used'],x['created_at'],x['last_opened'],x['comments'],x['phone'],x['tickets_com_password'],x['password_reset'],x['active_tickets_inside'],x['migrated_from'],x['migrated_to'])

   query = "UPDATE fullresultsdf SET id='%s',first_name='%s',last_name='%s',email='%s',type='%s',password='%s',delta_password='%s',recovery_email='%s',email_forwarding='%s',auto_po_seats_scouts='%s',errors_failed='%s',tm_created='%s',tm_password='%s',tm_address='%s',axs_created='%s',axs_password='%s',sg_created='%s',sg_password='%s',tickets_com_created='%s',facebook_created='%s',twitter_created='%s',eventbrite='%s',etix='%s',ticket_web='%s',big_tickets='%s',amazon='%s',secondary_password='%s',seat_scouts_added='%s',seat_scouts_status='%s',team='%s',specific_team='%s',forward_to='%s',forward_email_password='%s',seat_scouts_password='%s',password_matching='%s',disabled='%s',created_by='%s',edited_by='%s',ld_computer_used='%s',created_at='%s',last_opened='%s',comments='%s',phone='%s',tickets_com_password='%s',password_reset='%s',active_tickets_inside='%s',migrated_from='%s',migrated_to='%s' WHERE email='"+email+"'";
   cursor.execute(query,values)
   return ''


@app.route('/update/bypass_df_merged/<email>',methods = ['PUT'])
def bypass_df_merged1(email):
   x = request.json
   values = (x['email'],x['type'],x['password'],x['email_forwarding'],x['errors_failed'],x['tm_password'],x['axs_password'],x['sg_password'],x['tickets_com_created'],x['eventbrite'],x['etix'],x['ticket_web'],x['big_tickets'],x['team'],x['specific_team'],x['forward_to'],x['forward_email_password'],x['disabled'],x['comments'],x['Platform'],x['Card_Number'],x['Expiration'],x['CVV'],x['ADDRESS'],x['CITY'],x['STATE'],x['Zip_Code'],x['Phone'])
   
   query = "UPDATE bypass_df_merged SET email='%s',type='%s',password='%s',email_forwarding='%s',errors_failed='%s',tm_password='%s',axs_password='%s',sg_password='%s',tickets_com_created='%s',eventbrite='%s',etix='%s',ticket_web='%s',big_tickets='%s',team='%s',specific_team='%s',forward_to='%s',forward_email_password='%s',disabled='%s',comments='%s',Platform='%s',Card_Number='%s',Expiration='%s',CVV='%s',ADDRESS='%s',CITY='%s',STATE='%s',Zip_Code='%s',Phone='%s' WHERE email='"+email+"'"
   cursor.execute(query,values)
   return ''

@app.route('/update/newaccounts/<email>',methods = ['PUT'])
def newaccounts1(email):
   x = request.json
   df = pd.DataFrame(x)
   print(df)
   # values = (x['Email'],x['Platform'],x['Type'],x['Parent_Card'],x['Card_Number'],x['Expiration'],x['CVV'],x['CREATED_BY'],x['ADDRESS'],x['CITY'],x['STATE'],x['Zip_Code'],x['Phone'],x['CARD_ADDED_INTO_TICKETS.COM'])
   # query = "UPDATE newaccounts SET Email='%s',Platform='%s',Type='%s',Parent_Card='%s',Card_Number='%s',Expiration='%s',CVV='%s',CREATED_BY='%s',ADDRESS='%s',CITY='%s',STATE='%s',Zip_Code='%s',Phone='%s',CARD_ADDED_INTO_TICKETSCOM='%s' WHERE email='"+email+"'"
   # cursor.execute(query,values)
   return df



@app.route('/insert/fullresultsdf',methods = ['GET','POST'])
def fullresultsdf():
   counter = 0
   for x in request.json:
      values = (x['id'],x['first_name'],x['last_name'],x['email'],x['type'],x['password'],x['delta_password'],x['recovery_email'],x['email_forwarding'],x['auto_po_seats_scouts'],x['errors_failed'],x['tm_created'],x['tm_password'],x['tm_address'],x['axs_created'],x['axs_password'],x['sg_created'],x['sg_password'],x['tickets_com_created'],x['facebook_created'],x['twitter_created'],x['eventbrite'],x['etix'],x['ticket_web'],x['big_tickets'],x['amazon'],x['secondary_password'],x['seat_scouts_added'],x['seat_scouts_status'],x['team'],x['specific_team'],x['forward_to'],x['forward_email_password'],x['seat_scouts_password'],x['password_matching'],x['disabled'],x['created_by'],x['edited_by'],x['ld_computer_used'],x['created_at'],x['last_opened'],x['comments'],x['phone'],x['tickets_com_password'],x['password_reset'],x['active_tickets_inside'],x['migrated_from'],x['migrated_to'])

      query = "INSERT INTO fullresultsdf (id,first_name,last_name,email,type,password,delta_password,recovery_email,email_forwarding,auto_po_seats_scouts,errors_failed,tm_created,tm_password,tm_address,axs_created,axs_password,sg_created,sg_password,tickets_com_created,facebook_created,twitter_created,eventbrite,etix,ticket_web,big_tickets,amazon,secondary_password,seat_scouts_added,seat_scouts_status,team,specific_team,forward_to,forward_email_password,seat_scouts_password,password_matching,disabled,created_by,edited_by,ld_computer_used,created_at,last_opened,comments,phone,tickets_com_password,password_reset,active_tickets_inside,migrated_from,migrated_to) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
      cursor.execute(query,values)
      counter += 1
   return {"Inserted":str(counter)}

@app.route('/insert/bypass_df_merged',methods = ['GET','POST'])
def bypass_df_merged():
   counter = 0
   for x in request.json:
      values = (x['email'],x['type'],x['password'],x['email_forwarding'],x['errors_failed'],x['tm_password'],x['axs_password'],x['sg_password'],x['tickets_com_created'],x['eventbrite'],x['etix'],x['ticket_web'],x['big_tickets'],x['team'],x['specific_team'],x['forward_to'],x['forward_email_password'],x['disabled'],x['comments'],x['Platform'],x['Card_Number'],x['Expiration'],x['CVV'],x['ADDRESS'],x['CITY'],x['STATE'],x['Zip_Code'],x['Phone'])
      
      query = "INSERT INTO bypass_df_merged (email,type,password,email_forwarding,errors_failed,tm_password,axs_password,sg_password,tickets_com_created,eventbrite,etix,ticket_web,big_tickets,team,specific_team,forward_to,forward_email_password,disabled,comments,Platform,Card_Number,Expiration,CVV,ADDRESS,CITY,STATE,Zip_Code,Phone) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
      cursor.execute(query,values)
      counter += 1
   return {"Inserted":str(counter)}

@app.route('/insert/newaccounts',methods = ['GET','POST'])
def newaccounts():
   counter = 0
   for x in request.json:
      values = (x['Email'],x['Platform'],x['Type'],x['Parent_Card'],x['Card_Number'],x['Expiration'],x['CVV'],x['CREATED_BY'],x['ADDRESS'],x['CITY'],x['STATE'],x['Zip_Code'],x['Phone'],x['CARD_ADDED_INTO_TICKETS.COM'])
      query = "INSERT INTO newaccounts (Email,Platform,Type,Parent_Card,Card_Number,Expiration,CVV,CREATED_BY,ADDRESS,CITY,STATE,Zip_Code,Phone,CARD_ADDED_INTO_TICKETSCOM) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
      cursor.execute(query,values)
      counter += 1
   return {"Inserted":str(counter)}

if __name__ == '__main__':
   app.run()