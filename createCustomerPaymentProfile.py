
import os, sys

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *


def createCustomerPaymentProfile(customerInfo):
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = '4urP8Y47'
    merchantAuth.transactionKey = '538g4Tg2uMBte3W8' 

    creditCard = apicontractsv1.creditCardType()
    creditCard.cardNumber ="6011000000000012" # for the sake of testing this doesn't change
    creditCard.expirationDate ="2021-12" # this too

    payment = apicontractsv1.paymentType()
    payment.creditCard = creditCard

    billTo = apicontractsv1.customerAddressType()
    billTo.firstName = customerInfo["firstName"]
    billTo.lastName = customerInfo["lastName"]

    profile = apicontractsv1.customerPaymentProfileType()
    profile.payment = payment
    profile.billTo = billTo

    createCustomerPaymentProfile = apicontractsv1.createCustomerPaymentProfileRequest()
    createCustomerPaymentProfile.merchantAuthentication = merchantAuth
    createCustomerPaymentProfile.paymentProfile = profile
    customerProfileId = customerInfo["customerId"] # grab the same info from the dictionary but place it in their variable
    print("customerProfileId in createCustomerPaymentProfile. customerProfileId = %s" %customerProfileId)
    createCustomerPaymentProfile.customerProfileId = str(customerProfileId)

    controller = createCustomerPaymentProfileController(createCustomerPaymentProfile)
    controller.execute()

    response = controller.getresponse()

    if (response.messages.resultCode=="Ok"):
        print("Successfully created a customer payment profile with id: %s" % response.customerPaymentProfileId)
        
    else:
        print("Failed to create customer payment profile %s" % response.messages.message[0]['text'].text)

    return response.customerPaymentProfileId

if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    createCustomerPaymentProfile(constants.customerProfileId)