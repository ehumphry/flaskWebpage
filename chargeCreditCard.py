from authorizenet import apicontractsv1
from authorizenet.apicontrollers import*
from decimal import*

def chargeCard():
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name ='4urP8Y47'
    merchantAuth.transactionKey ='538g4Tg2uMBte3W8'
 
    creditCard = apicontractsv1.creditCardType()
    creditCard.cardNumber ="6011000000000012"
    creditCard.expirationDate ="2021-12"
 
    payment = apicontractsv1.paymentType()
    payment.creditCard = creditCard
 
    transactionrequest = apicontractsv1.transactionRequestType()
    transactionrequest.transactionType ="authCaptureTransaction"
    transactionrequest.amount = Decimal ('1.55')
    transactionrequest.payment = payment
 
 
    createtransactionrequest = apicontractsv1.createTransactionRequest()
    createtransactionrequest.merchantAuthentication = merchantAuth
    createtransactionrequest.refId ="MerchantID-0001"
 
    createtransactionrequest.transactionRequest = transactionrequest
    createtransactioncontroller = createTransactionController(createtransactionrequest)
    createtransactioncontroller.execute()
 
    response = createtransactioncontroller.getresponse()
 
    if (response.messages.resultCode=="Ok"):
        print("Transaction ID : %s"% response.transactionResponse.transId)
    else:
        print("response code: %s"% response.messages.resultCode)
 

