from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from chargeCreditCard import chargeCard
from createCustomerProfile import createCustomerProfile
from storeCustomerInformation import storeCustomerInformation
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
    customerTable = " "
    #call function to query customerProfiles table, returns boolean and a list
    #use templates to print off entries with buttons


    return render_template("index.html")

@app.route("/newCharge", methods=['POST', 'GET']) 
def newCharge():
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
    
    return render_template("newCharge.html", message = message, message2 = message2)  
     # change template from newCharge to notification page


# @app.route('/queryTest')
# def users():
#     cur = mysql.connection.cursor()
#     cur.execute('''SELECT * FROM users''')
#     rv = cur.fetchall()
#     return str(rv)

if __name__ == '__main__':
    app.run(debug=True)

