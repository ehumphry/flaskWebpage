# This function takes customer information in the form of a dictionary and a mysql connection and stores it 
# in the customerInfo table
from flask_mysqldb import MySQL

def storeCustomerInformation(customerInfo, mysql):
   
    try:
       
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO customerProfiles (firstName, lastName, address, city, state, zipCode, phone, email, customerId) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s)", (customerInfo["firstName"], customerInfo["lastName"],customerInfo["address"],customerInfo["city"],customerInfo["state"],customerInfo["zipCode"], customerInfo["phone"],customerInfo["email"],customerInfo["customerId"]))
        cursor.execute("INSERT INTO transactions (customerId, transactionId) VALUES ( %s, %s)", (customerInfo["customerId"], customerInfo["transactionId"]))
        mysql.connection.commit()

        cursor.close()

        print("Information Stored Successfully")
    except:
        print("Failed to insert recored into table")

        cursor.close()
    
    #rv = cur.fetchall()
    
    #print( str(rv))

  
    
    