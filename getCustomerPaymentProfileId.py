from flask_mysqldb import MySQL

def getCustomerPaymentProfileId(customerId, mysql):
    id = customerId
    try:
       
        cursor = mysql.connection.cursor()
        query = ("SELECT customerPaymentProfileId FROM customerProfiles WHERE customerId ="+ id +";")
        cursor.execute(query)
        result = cursor.fetchone()
        paymentProfileId = result[0]
        print(paymentProfileId)
        cursor.close()

        print("retreived customer payment profile ID " + paymentProfileId)
    except:
        print("Failed to get customer payment profile ID from table ")

        cursor.close()
    
    return paymentProfileId
    