from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from chargeCreditCard import chargeCard
from createCustomerProfile import createCustomerProfile
import config
#from Report import get_report



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


            customerInfo = {
                "cardNumber": cardNumber,"exirationDAte": expirationDate, "amount": amount, "firstName": firstName, "lastName": lastName, "company": company, "address": address, "city": city, "state": state, "zipCode": zipCode, "phone": phone, "email": email
                }
            
            message = chargeCard(customerInfo)
            customerProileId, message2 = createCustomerProfile(customerInfo)
            
            #send charge, get transaction ID, create customer profile Id with transaction ID, save contact information from from and customer profile ID from API
        except:
            message = ("Error Collecting Form")
    
    return render_template("newCharge.html", message = message, message2 = message2)  
     # change template from newCharge to notification page

# @app.route("/notification" ) 
# def notification():

#     return render_template("notification.html") 



