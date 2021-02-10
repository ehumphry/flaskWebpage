from authorizenet import apicontractsv1
from authorizenet.apicontrollers import*
from decimal import*
import json


    


def chargeCard(customerInfo): #takes a dictionary that has customer info

   
    merchantAuth = apicontractsv1.merchantAuthenticationType() #required
    merchantAuth.name ='4urP8Y47' #required
    merchantAuth.transactionKey ='538g4Tg2uMBte3W8' #required
 
    creditCard = apicontractsv1.creditCardType()
    creditCard.cardNumber ="6011000000000012" # this stays this way for testing purposes.
    creditCard.expirationDate ="2021-12" # date only needs to be later than current date.
 
    payment = apicontractsv1.paymentType()
    payment.creditCard = creditCard

    customerAddress = apicontractsv1.customerAddressType()
    customerAddress.firstName = customerInfo["firstName"]
    customerAddress.lastName = customerInfo["lastName"]
    customerAddress.company = customerInfo["company"]
    customerAddress.address = customerInfo["address"]
    customerAddress.city = customerInfo["city"]
    customerAddress.state = customerInfo["state"]
    customerAddress.zip = customerInfo["zipCode"]
    customerAddress.phoneNumber = customerInfo["phone"]
    customerAddress.email = customerInfo["email"]
    
    transactionrequest = apicontractsv1.transactionRequestType()
    transactionrequest.transactionType ="authCaptureTransaction"
    transactionrequest.amount = Decimal (customerInfo["amount"]) #required
    transactionrequest.payment = payment
    transactionrequest.billTo = customerAddress
 
 
    createtransactionrequest = apicontractsv1.createTransactionRequest()
    createtransactionrequest.merchantAuthentication = merchantAuth
    createtransactionrequest.refId ="MerchantID-0001"
 
    createtransactionrequest.transactionRequest = transactionrequest
    createtransactioncontroller = createTransactionController(createtransactionrequest)
    createtransactioncontroller.execute()
 
    response = createtransactioncontroller.getresponse()
    
    if (response.messages.resultCode=="Ok"):
        error = False

        message = ("Transaction ID : %s"% response.transactionResponse.transId)
        print("Transaction ID : %s"% response.transactionResponse.transId)
    else:
        
        message = response.messages.resultCode
        print("response code: %s"% response.messages.resultCode)
    return response.transactionResponse.transId, message
 


# def save_customer():

#     #save customer


# def charge_profile(customer_profile):

#     # create request to charge profile