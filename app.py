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
    return render_template("index.html")

@app.route("/newCharge", methods=['POST', 'GET']) 
def newCharge():
    message = " "
    message2 = " "
    if request.method == 'POST':
        try:
            cardNumber = request.form['cardNumber']
            print(cardNumber)
            expirationDate = request.form['expirationDate']
            print(expirationDate)
            amount = request.form['amount']
            print(amount)
            firstName = request.form['firstName']
            print(firstName)
            lastName = request.form['lastName']
            print(lastName)
            company = request.form['company']
            print(company)
            address = request.form['address']
            print(address)
            city = request.form['city']
            print(city)
            state = request.form['state']
            print(state)
            zipCode = request.form['zipCode']
            print(zipCode)
            phone = request.form['phone']
            print(phone)
            email = request.form['email']
            print(email)
            #if there is time, add description field for customer profile, for now it is set for No Description in createCustomer.py line 25


            customerInfo = {
                "cardNumber": cardNumber,"exirationDAte": expirationDate, "amount": amount, "firstName": firstName, "lastName": lastName, "company": company, "address": address, "city": city, "state": state, "zipCode": zipCode, "phone": phone, "email": email
                }
            
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

