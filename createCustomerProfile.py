import os, sys
import imp
from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
#constants = imp.load_source('modulename', 'constants.py')
import random

def createCustomerProfile(customerInfo):
    
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = '4urP8Y47'
    merchantAuth.transactionKey = '538g4Tg2uMBte3W8' 


    createCustomerProfile = apicontractsv1.createCustomerProfileRequest()
    createCustomerProfile.merchantAuthentication = merchantAuth
    createCustomerProfile.profile = apicontractsv1.customerProfileType(customerInfo["firstName"] + str(random.randint(0, 10000)), customerInfo["lastName"], customerInfo["email"])

    controller = createCustomerProfileController(createCustomerProfile)
    controller.execute()

    response = controller.getresponse()
    
    if (response.messages.resultCode=="Ok"):
        message2 = ("Successfully created a customer profile for %s %s " % (customerInfo["firstName"],customerInfo["lastName"]))
        print("Successfully created customer profile with id: %s" % response.customerProfileId)
    else:
        message2 = ("Failed to create customer payment profile %s" % response.messages.message[0]['text'].text)
        print("Failed to create customer payment profile %s" % response.messages.message[0]['text'].text)

    return response.customerProfileId, message2

if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    createCustomerProfile()