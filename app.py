from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from chargeCreditCard import chargeCard
from createCustomerProfile import createCustomerProfile
from storeCustomerInformation import storeCustomerInformation
from deleteCustomerProfile import deleteCustomerProfile
import config




app = Flask(__name__,
            instance_relative_config=False,
            template_folder="templates",
            static_folder="static")
app.config['MYSQL_HOST'] = config.host
app.config['MYSQL_USER'] = config.user
app.config['MYSQL_PASSWORD'] = config.password
app.config['MYSQL_DB'] = config.database

mysql = MySQL(app)
app.secret_key = config.secretKey

@app.route("/") #manage customers page
def index():
    gotData = " "
    cursor = mysql.connection.cursor()
    query = "SELECT firstName AS first, lastName AS last, customerId AS id FROM customerProfiles;"
    cursor.execute(query)
    report = cursor.fetchall()
    cursor.close()
    


    return render_template("index.html", hasData = gotData, data = report)

@app.route("/newCharge", methods=['POST', 'GET']) 
def newCharge():

    
    return render_template("newCharge.html")  
     # change template from newCharge to notification page


# @app.route('/queryTest')
# def users():
#     cur = mysql.connection.cursor()
#     query = "SELECT firstName AS first, lastName AS last, customerId AS id FROM customerProfiles;"
#     cur.execute(query)
#     data = cur.fetchall()
#     gotData = True
    
#     print (data)
#     return render_template("index.html", gotData = hasData, data = data  ) 



# This takes the information from newCharge and returns it on a a seperate page if the transaction was
# successful

@app.route('/notification', methods=['POST', 'GET'])
def notification():
    message = " "
    message2 = " "
    customerInfo = {
        "description": " "
    }
    if request.method == 'POST':
        try:
            customerInfo["cardNumber"] = request.form['cardNumber']
            
            customerInfo["expirationDate"] = request.form['expirationDate']
            
            customerInfo["amount"] = request.form['amount']

            customerInfo["description"] = request.form['description']
            
            customerInfo["firstName"]  = request.form['firstName']
            
            customerInfo["lastName"] = request.form['lastName']
            
            customerInfo["company"] = request.form['company']
           
            customerInfo["address"] = request.form['address']
            
            customerInfo["city"] = request.form['city']
            
            customerInfo["state"]= request.form['state']
            
            customerInfo["zipCode"] = request.form['zipCode']
           
            customerInfo["phone"] = request.form['phone']
            
            customerInfo["email"] = request.form['email']
           
            #if there is time, add description field for customer profile, for now it is set for No Description in createCustomer.py line 25


            # customerInfo = {
            #     "cardNumber": cardNumber,"exirationDAte": expirationDate, "amount": amount, "firstName": firstName, "lastName": lastName, "company": company, "address": address, "city": city, "state": state, "zipCode": zipCode, "phone": phone, "email": email
            #     }
            #if there is time, assign form information directly to the dictionary
            transactionId, message = chargeCard(customerInfo) #calls chargeCard API and returns transactionId
            customerId, message2 = createCustomerProfile(customerInfo) #calls createCustomerProfile API and returns customer profileId
            customerInfo["transactionId"] = transactionId # append new info to the customerInfo dictionary
            customerInfo["customerId"] = customerId # append new info to the customerInfo dictionary
            print(customerInfo["transactionId"])
            print(customerInfo["customerId"])
             
            storeCustomerInformation(customerInfo, mysql) #send dictionary and sql connection to storeCustomerInformation function

                  
        except:
            message = ("Error Collecting Form")

            

    return render_template("notification.html", message = message, message2 = message2)

@app.route('/deleteProfile', methods=['GEt','POST'])
def deleteProfile():
    message = " "
    message2 = " "
    if request.method == 'POST':
        try: 
            message = "Were not doing anything yet. "
            message2 = "The functions don't work properly"
            customerId = request.form.get("customerId")
            print(customerId)
            message = deleteCustomerProfile(customerId)


        except:
            message = "Error Collecting Customer ID"
            
        
        try:
            cursor = mysql.connection.cursor() 
            query1 = ("DELETE FROM transactions WHERE customerId = "+ customerId+";")
            query2 = ("DELETE FROM customerProfiles WHERE customerId = "+ customerId+";")
            cursor.execute(query1)
            cursor.execute(query2)
            mysql.connection.commit()
            cursor.close()
            message2 = ("Customer "+ customerId + " has been deleted from local database")
    

       
        except:
            message = " "
            message2 = "Select a valid customer"

    return render_template("notification.html", message = message, message2 = message2)

if __name__ == '__main__':
    app.run(debug=True)

